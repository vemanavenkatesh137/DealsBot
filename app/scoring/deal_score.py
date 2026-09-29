```python
def calculate_deal_score(
    current_price: float,
    mrp: float,
    historical_low: float,
    rating: float,
    review_count: int,
    coupon: float = 0,
    bank_discount: float = 0,
) -> int:

    if current_price <= 0 or mrp <= 0:
        return 0

    # ---------------------------------------------------------
    # 1. Price discount vs MRP — 25 points
    # ---------------------------------------------------------

    discount_percent = ((mrp - current_price) / mrp) * 100

    discount_percent = max(0, discount_percent)

    discount_score = min(
        (discount_percent / 50) * 25,
        25,
    )

    # ---------------------------------------------------------
    # 2. Historical price — 30 points
    # ---------------------------------------------------------

    if historical_low > 0:

        price_difference_percent = (
            (current_price - historical_low)
            / historical_low
        ) * 100

        if current_price <= historical_low:
            history_score = 30

        elif price_difference_percent <= 5:
            history_score = 25

        elif price_difference_percent <= 10:
            history_score = 20

        elif price_difference_percent <= 20:
            history_score = 12

        elif price_difference_percent <= 30:
            history_score = 6

        else:
            history_score = 0

    else:
        # No historical data available
        history_score = 10

    # ---------------------------------------------------------
    # 3. Rating — 15 points
    # ---------------------------------------------------------

    rating = max(0, min(rating, 5))

    rating_score = (rating / 5) * 15

    # -------------------
```
