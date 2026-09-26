def calculate_deal_score(
    current_price: float,
    mrp: float,
    historical_low: float,
    rating: float,
    review_count: int,
    coupon: float = 0,
    bank_discount: float = 0,
) -> int:

    if mrp <= 0 or current_price <= 0:
        return 0

    # 1. MRP discount
    discount_percent = ((mrp - current_price) / mrp) * 100
    discount_score = min(discount_percent / 50 * 25, 25)

    # 2. Historical price
    if historical_low > 0:
        if current_price <= historical_low:
            history_score = 25
        else:
            difference = (
                (historical_low - current_price)
                / historical_low
            ) * 100

            history_score = max(
                0,
                min(25, 15 + difference)
            )
    else:
        history_score = 10

    # 3. Rating
    rating_score = min((rating / 5) * 15, 15)

    # 4. Reviews
    if review_count >= 10000:
        review_score = 10
    elif review_count >= 5000:
        review_score = 8
    elif review_count >= 1000:
        review_score = 6
    elif review_count >= 100:
        review_score = 4
    else:
        review_score = 1

    # 5. Coupon + bank offer
    extra_discount = coupon + bank_discount

    if extra_discount >= 1000:
        offer_score = 10
    elif extra_discount >= 500:
        offer_score = 7
    elif extra_discount >= 200:
        offer_score = 5
    elif extra_discount > 0:
        offer_score = 3
    else:
        offer_score = 0

    score = (
        discount_score
        + history_score
        + rating_score
        + review_score
        + offer_score
    )

    return min(round(score), 100)
