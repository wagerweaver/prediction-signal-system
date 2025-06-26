# 📦 dispatch/ — Telegram Signal Dispatch Layer

**Handles automated delivery of trade signals to Telegram.**  
This module ensures reliable and secure formatting and posting of signals from the Codex system to your specified channel or group.

---

## 🔍 Purpose

To streamline and automate the sending of finalized trade alerts — formatted by the `formatter/` layer — into Telegram channels, maintaining consistent structure and delivery.

---

## 📁 Files

| File                   | Description                                      |
|------------------------|--------------------------------------------------|
| `live_dispatch.py` | Core dispatch logic: connects to Telegram Bot API and sends preformatted messages |

---

## ⚙️ Features

- ✅ Seamless integration with `formatter/` signal output  
- ✅ Clean, bold message formatting with emoji and HTML tags  
- ✅ Easy integration inside Codex  
- ✅ Minimal setup — just a bot token and chat ID  
- ✅ Built for future scaling to other platforms (Discord, Slack)

---

## 🚀 How to Use

```python
from telegram_dispatcher import send_telegram_signal

send_telegram_signal(
    chat_id='@YourChannelName',
    message_payload="""
        📊 <b>Signal:</b> TSLA (Stocks)
        🎯 <b>Target:</b> $346.90
        🛑 <b>Stop Loss:</b> $360.69
        💰 <b>Entry:</b> $353.01
        📈 <b>R/R:</b> 0.89 | <b>Leverage:</b> 4x
        ⏳ <b>Timeframe:</b> Close-to-Close (1D)
        ⚠️ Volatility: ✅ ATR normal
    """,
    bot_token='123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
)
