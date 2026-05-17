def calculate_risk_score(amount, velocity):

    score = (amount * 0.6) + (velocity * 0.4)

    return round(score, 2)