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

    return StrategySpec(
        symbol=symbol.group(1) if symbol else "BTCUSDT",
        timeframe=timeframe.group(1) if timeframe else "1h",
        direction=direction,
        entry="EMA20/50 cross",
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
