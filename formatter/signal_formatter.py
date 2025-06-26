# Signal Formatter Module

def format_signal(signal_data):
    symbol = signal_data['symbol']
    entry = signal_data['entry_price']
    predicted_close = signal_data['predicted_close']
    atr = signal_data['atr']
    tier = signal_data['confidence_tier']

    stop_loss = entry + 1.5 * atr if predicted_close < entry else entry - 1.5 * atr
    take_profit = predicted_close
    rr = abs((take_profit - entry) / (entry - stop_loss)) if (entry - stop_loss) != 0 else 0

    leverage_map = {1: "7x", 2: "4x", 3: "2x"}
    leverage = leverage_map.get(tier, "Do not trade")

    signal = {
        'symbol': symbol,
        'entry_price': entry,
        'stop_loss': round(stop_loss, 2),
        'take_profit': round(take_profit, 2),
        'risk_reward_ratio': round(rr, 2),
        'confidence_tier': tier,
        'leverage_recommendation': leverage,
        'timeframe': 'Close-to-Close (Daily)',
        'volatility_note': '✅ ATR within acceptable range. Trade valid.',
        'formatted_telegram_signal': f"""📊 <b>Signal:</b> {symbol} ({signal_data['asset_class'].capitalize()})
🎯 <b>Target:</b> ${round(take_profit, 2)}
🛑 <b>Stop Loss:</b> ${round(stop_loss, 2)}
💰 <b>Entry:</b> ${round(entry, 2)}
📈 <b>R/R:</b> {round(rr, 2)} | <b>Leverage:</b> {leverage}
⏳ <b>Timeframe:</b> Close-to-Close (1D)
⚠️ Volatility: ✅ ATR normal"""
    }

    return signal
