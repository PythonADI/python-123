def place_bet(price, prev_price):
    """
    - return sell order if price is +10% of prev_price, 1
    - return purchase order if -10% of prev_price, 2
    - return None otherwise
    """
    price_dt = ((price - prev_price) / prev_price) * 100
    if price_dt >= 10:
        return 1
    if price_dt <= -10:
        return 2

    return None
