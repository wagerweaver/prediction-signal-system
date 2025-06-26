# Risk Management Bot

def apply_risk_filter(signal_data):
    predicted_move = abs(signal_data['predicted_close'] - signal_data['entry_price']) / signal_data['entry_price']
    atr = signal_data['atr']
    r2_score = signal_data['r2_score']

    if predicted_move < 0.003 or r2_score < 0.990 or atr > 1.5 * atr:
        signal_data['risk_flag'] = '❌ Signal filtered out due to low move, low R², or high volatility.'
        return None
    else:
        signal_data['risk_flag'] = '✅ Signal passed risk filter.'
        return signal_data
