from app.scoring.deal_score import calculate_deal_score
from app.notifications.telegram import send_telegram


def main():

    # Temporary test product
    product = {
        "name": "Sony WH-1000XM5",
        "platform": "Amazon",
        "mrp": 34990,
        "current_price": 21999,
        "historical_low": 22999,
        "rating": 4.5,
        "review_count": 12500,
        "coupon": 1000,
        "bank_discount": 500,
        "url": "https://www.amazon.in/",
    }

    score = calculate_deal_score(
        current_price=product["current_price"],
        mrp=product["mrp"],
        historical_low=product["historical_low"],
        rating=product["rating"],
        review_count=product["review_count"],
        coupon=product["coupon"],
        bank_discount=product["bank_discount"],
    )

    effective_price = (
        product["current_price"]
        - product["coupon"]
        - product["bank_discount"]
    )

    message = f"""
🔥 DEAL DETECTED — {score}/100

🎧 {product["name"]}

🛒 {product["platform"]}

💰 Price: ₹{product["current_price"]:,}
🏷 MRP: ₹{product["mrp"]:,}

🎟 Coupon: ₹{product["coupon"]:,}
🏦 Bank offer: ₹{product["bank_discount"]:,}

💵 Effective price: ₹{effective_price:,}

⭐ Rating: {product["rating"]}/5
👥 Reviews: {product["review_count"]:,}

📉 Historical low: ₹{product["historical_low"]:,}

🔗 {product["url"]}
"""

    print(message)

    # Only notify good deals
    if score >= 70:
        send_telegram(message)
        print("Deal sent to Telegram.")
    else:
        print("Deal score below threshold.")


if __name__ == "__main__":
    main()
