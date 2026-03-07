from dataclasses import dataclass
import re

@dataclass
class StrategySpec:
    symbol: str
    timeframe: str
    direction: str
    entry: str
    exit: str
    sl: float | None = None
    tp: float | None = None


def parse_prompt(prompt: str) -> StrategySpec:
    # naive parser for demo
    symbol = re.search(r"([A-Z]{3,6}USDT)", prompt)
    timeframe = re.search(r"(\d+[mhd])", prompt)
    sl = re.search(r"SL\s*(\d+\.?\d*)%", prompt, re.I)
    tp = re.search(r"TP\s*(\d+\.?\d*)%", prompt, re.I)
    direction = "long" if "long" in prompt.lower() else "both"

    # support RSI / MACD keywords
    entry = "EMA20/50 cross"
    if "RSI" in prompt.upper():
        entry = "RSI"
    if "MACD" in prompt.upper():
        entry = "MACD"

    return StrategySpec(
        symbol=symbol.group(1) if symbol else "BTCUSDT",
        timeframe=timeframe.group(1) if timeframe else "1h",
        direction=direction,
        entry=entry,
        exit="reverse cross",
        sl=float(sl.group(1)) if sl else None,
        tp=float(tp.group(1)) if tp else None,
    )


def parse_file(path: str) -> StrategySpec:
    # supported: JSON with fields matching StrategySpec
    import json
    with open(path, "r") as f:
        data = json.load(f)
    return StrategySpec(**data)


def _normalize_ocr(text: str) -> str:
    # common OCR cleanup
    t = text.upper()
    t = t.replace("0/", "O/")
    t = t.replace("O/", "0/")
    t = t.replace("SL", "SL ")
    t = t.replace("TP", "TP ")
    t = t.replace("LONGONLY", "LONG ONLY")
    return t


def parse_image(path: str) -> StrategySpec:
    # OCR screenshot to text, then parse prompt (with second-pass cleanup)
    try:
        import pytesseract
        from PIL import Image
    except Exception as e:
        raise RuntimeError("pytesseract/PIL missing. Install tesseract + pytesseract.") from e
    raw = pytesseract.image_to_string(Image.open(path))
    spec = parse_prompt(raw)
    # second pass if TP or SL missing
    if spec.tp is None or spec.sl is None:
        cleaned = _normalize_ocr(raw)
        spec = parse_prompt(cleaned)
    return spec
