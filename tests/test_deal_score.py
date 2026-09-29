```python
from app.scoring.deal_score import calculate_deal_score


def test_genuine_good_deal():
    score = calculate_deal_score(
        current_price=20000,
        mrp=30000,
        historical_low=20500,
        rating=4.5,
        review_count=10000,
        coupon=1000,
        bank_discount=500,
    )

    assert score >= 70


def test_poor_historical_price():
    score = calculate_deal_score(
        current_price=25000,
        mrp=30000,
        historical_low=15000,
        rating=4.5,
        review_count=10000,
        coupon=0,
        bank_discount=0,
    )

    assert score < 70


def test_low_rating_product():
    score = calculate_deal_score(
        current_price=18000,
        mrp=30000,
        historical_low=19000,
        rating=2.8,
        review_count=10000,
        coupon=1000,
        bank_discount=500,
    )

    assert score < 70


def test_no_discount():
    score = calculate_deal_score(
        current_price=30000,
        mrp=30000,
        historical_low=30000,
        rating=4.5,
        review_count=10000,
        coupon=0,
        bank_discount=0,
    )

    assert score < 70


def test_historical_low():
    score = calculate_deal_score(
        current_price=15000,
        mrp=25000,
        historical_low=15000,
        rating=4.5,
        review_count=10000,
        coupon=1000,
        bank_discount=500,
    )

    assert score >= 80


def test_invalid_price():
    score = calculate_deal_score(
        current_price=0,
        mrp=30000,
        historical_low=20000,
        rating=4.5,
        review_count=10000,
    )

    assert score == 0
```
