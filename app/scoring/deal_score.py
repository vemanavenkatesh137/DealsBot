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
    # 1. MRP discount — 25 points
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
        history_score = 10

    # ---------------------------------------------------------
    # 3. Rating — 20 points
    # ---------------------------------------------------------

    rating = max(0, min(rating, 5))

    rating_score = (rating / 5) * 20

    # ---------------------------------------------------------
    # 4. Reviews — 10 points
    # ---------------------------------------------------------

    if review_count >= 10000:
        review_score = 10

    elif review_count >= 5000:
        review_score = 9

    elif review_count >= 1000:
        review_score = 7

    elif review_count >= 500:
        review_score = 5

    elif review_count >= 100:
        review_score = 3

    else:
        review_score = 1

    # ---------------------------------------------------------
    # 5. Coupon + bank offer — 15 points
    # ---------------------------------------------------------

    extra_discount = max(0, coupon) + max(0, bank_discount)

    if extra_discount >= 2000:
        offer_score = 15

    elif extra_discount >= 1500:
        offer_score = 13

    elif extra_discount >= 1000:
        offer_score = 11

    elif extra_discount >= 500:
        offer_score = 8

    elif extra_discount >= 200:
        offer_score = 5

    elif extra_discount > 0:
        offer_score = 2

    else:
        offer_score = 0

    # ---------------------------------------------------------
    # Final score — 100 points
    # ---------------------------------------------------------

    score = (
        discount_score
        + history_score
        + rating_score
        + review_score
        + offer_score
    )

    return min(round(score), 100)
