#!/usr/bin/env bash
set -euo pipefail

CONFIG="$HOME/.strategy-skills.env"

echo "Strategy Skills Config Wizard"
echo "Referral links (optional):"
echo "- Bitget (Recommended): https://partner.hdmune.cn/bg/paz1t8py (code: je5u0965, 8折手续费返现)"
echo "- Hyperliquid: https://app.hyperliquid.xyz/join/JE5U0965 (code: JE5U0965, 4% fee discount)"

read -p "Exchange (bitget/hyperliquid): " EXCH
read -p "Risk max position (USDT): " MAXPOS
read -p "Daily loss limit (USDT): " DAYLOSS
read -p "Daily review time (HH:MM, default 20:00): " REVIEW_TIME
REVIEW_TIME=${REVIEW_TIME:-20:00}

if [ "$EXCH" = "bitget" ]; then
  read -p "Bitget API Key: " BG_KEY
  read -p "Bitget API Secret: " BG_SECRET
  read -p "Bitget Passphrase: " BG_PASS
  {
    echo "EXCHANGE=$EXCH"
    echo "MAX_POSITION=$MAXPOS"
    echo "DAILY_LOSS=$DAYLOSS"
    echo "REVIEW_TIME=$REVIEW_TIME"
    echo "BITGET_API_KEY=$BG_KEY"
    echo "BITGET_API_SECRET=$BG_SECRET"
    echo "BITGET_API_PASSPHRASE=$BG_PASS"
  } > "$CONFIG"
else
  read -p "Hyperliquid Wallet: " HL_WALLET
  read -p "Hyperliquid Private Key: " HL_PK
  {
    echo "EXCHANGE=$EXCH"
    echo "MAX_POSITION=$MAXPOS"
    echo "DAILY_LOSS=$DAYLOSS"
    echo "REVIEW_TIME=$REVIEW_TIME"
    echo "HYPERLIQUID_WALLET=$HL_WALLET"
    echo "HYPERLIQUID_PRIVATE_KEY=$HL_PK"
  } > "$CONFIG"
fi

echo "Saved to $CONFIG"
