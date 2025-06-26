# 🧩 Signal Formatter Module

This module transforms raw prediction outputs from the engine into clear, risk-aware trade signals ready for dispatch to Telegram or other platforms.

---

## 📂 File

- `signal_formatter.py` — Core formatter logic for stop loss, take profit, RR ratio, leverage, and output formatting.

---

## 🎯 Purpose

Prediction outputs are often raw and direction-only. This formatter ensures that:

- Each signal has a structured stop loss and take profit  
- Risk-reward logic is consistent with trading strategy  
- Leverage guidance is dynamically assigned  
- Telegram-formatted messages are clean, clear, and automated  

---

## 🧠 How It Works

### ✅ Inputs Expected:

```python
{
    'symbol': 'TSLA',
    'entry_price': 353.01,
    'predicted_close': 346.90,
    'r2_score': 0.997,
    'confidence_tier': 2,
    'asset_class': 'stocks',
    'atr': 5.12
}
```

### 📤 Output Generated:

```python
{
    'symbol': 'TSLA',
    'entry_price': 353.01,
    'stop_loss': 360.69,
    'take_profit': 346.90,
    'risk_reward_ratio': 0.89,
    'confidence_tier': 2,
    'leverage_recommendation': '4x',
    'timeframe': 'Close-to-Close (Daily)',
    'volatility_note': '✅ ATR within acceptable range. Trade valid.',
    'formatted_telegram_signal': '<pre>...</pre>'
}
```

---

## 📈 Leverage Logic

| Confidence Tier | R² Score      | Predicted Move | Leverage |
|-----------------|---------------|----------------|----------|
| 1               | ≥ 0.999       | ≥ 1.5%         | 7x       |
| 2               | ≥ 0.995       | ≥ 1.0%         | 4x       |
| 3               | ≥ 0.990       | ≥ 0.5%         | 2x       |
| 4–5             | Below 0.990   | < 0.5%         | Skip     |

---

## 🖥️ Telegram Signal Output Example

```html
📊 <b>Signal:</b> TSLA (Stocks)  
🎯 <b>Target:</b> $346.90  
🛑 <b>Stop Loss:</b> $360.69  
💰 <b>Entry:</b> $353.01  
📈 <b>R/R:</b> 0.89 | <b>Leverage:</b> 4x  
⏳ <b>Timeframe:</b> Close-to-Close (1D)  
⚠️ Volatility: ✅ ATR normal
```

---

## 🛡️ Validation Logic

- **SL/TP Check:** Ensures that SL > Entry > TP for short trades, or SL < Entry < TP for long trades.  
- **Volatility Gate:** Uses 1.5× ATR to define SL range. Invalidates trades if ATR exceeds tolerance window.  
- **RR Guard:** Flags signals with RR < 1.0 as low quality (optional filter for future use).  

---

## 🔮 Future Enhancements

- Support multi-TP targets (TP1, TP2, TP3)  
- Add numeric confidence scoring  
- Integrate with Telegram bot for auto-posting  
- Add RR minimum filter threshold logic  
- Dynamic timeframe adaptability (C2C, intraday, swing)  

---

## ✅ Summary

The `signal_formatter.py` module brings safety, structure, and clarity to every trade idea.  
It aligns Telegram signals with the model’s original forecast and ensures all trades follow defined risk standards.

If this module is kept in sync with the engine, signal quality and trader trust will both increase.
