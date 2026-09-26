import os
import requests


def send_telegram(message: str):
    token = os.environ["TELEGRAM_BOT_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    response = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": message,
        },
        timeout=30,
    )

    response.raise_for_status()


def main():
    message = """
🔥 Deal Hunter is working!

This is our first automated test.

🛒 Amazon: Connected soon
🛒 Flipkart: Connected soon

🤖 GitHub Actions → Python → Telegram
"""

    send_telegram(message)

    print("Telegram message sent successfully!")


if __name__ == "__main__":
    main()
