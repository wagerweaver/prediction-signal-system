# 🛡️ Risk Management Module

This module applies essential safety checks and filters to ensure trade signals meet minimum risk criteria before being dispatched.

---

## 📂 File

- `risk_management_bot.py` — Core logic for filtering signals based on risk-reward ratio, R² confidence, ATR volatility, and predicted move thresholds.

---

## 🎯 Purpose

To enforce strict baseline checks so only high-quality signals (aligned with risk and model confidence rules) are passed forward. This protects against low-conviction or unsafe trades.

---

## 🧠 How It Works

### ✅ Inputs Expected:

```python
{
    'symbol': 'BTCUSD',
    'entry_price': 105000.00,
    'predicted_close': 107000.00,
    'atr': 1500.00,
    'r2_score': 0.996,
    'confidence_tier': 2,
    'risk_reward_ratio': 1.33
}
```

### 📤 Output Behavior:

- **Valid Signal:** Returned with `risk_flag` message
- **Invalid Signal:** Returns `None`, with reason logged

```python
# Valid example
{
    ...,
    'risk_flag': '✅ Signal passed risk filter.'
}

# Invalid example
{
    ...,
    'risk_flag': '❌ Signal filtered: R/R < 1.0'
}
```

---

## 📈 Risk Criteria

| Check                     | Rule Description                                           |
|--------------------------|------------------------------------------------------------|
| R/R Filter                | Must be ≥ 1.0                                              |
| Confidence Filter         | R² score ≥ 0.990 required                                  |
| Minimum Move Threshold    | Predicted move must be ≥ 0.3%                              |
| ATR Volatility Check      | ATR must not exceed 1.5× its rolling average (future)      |
| Confidence Tier Filter    | Only Tier 1–3 allowed (Tier 4–5 are filtered)              |

---

## 🔮 Future Enhancements

| Feature                           | Benefit                                      |
|----------------------------------|----------------------------------------------|
| Custom R/R threshold setting     | Allow user-tuned aggressiveness              |
| Macro/sentiment integration      | Add contextual risk overlays                 |
| Signal logging and analytics     | Track how many signals were filtered and why |
| Manual override capability       | Let admins bypass rules in urgent cases      |

---

## ✅ Summary

The `risk_management_bot.py` module serves as the system’s risk gatekeeper. It blocks low-conviction or structurally flawed trades before they can be dispatched, preserving system credibility and protecting users. This is a core integrity layer of the full signal infrastructure.
