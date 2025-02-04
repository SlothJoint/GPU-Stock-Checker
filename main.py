import time
import requests
import sys
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Telegram Bot Credentials
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# API & Buy Link
NVIDIA_URL = ""
BUY_LINK_TEMPLATE = ""

# Explicit ChromeDriver Path
CHROMEDRIVER_PATH = "YOUR_CHROMEDRIVER_PATH"

# Configure Selenium to Mimic a Browser
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start WebDriver Service
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=chrome_options)

def send_telegram_message(message):
    """Sends a notification via Telegram."""
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(telegram_url, json=payload)
    except requests.exceptions.RequestException as e:
        sys.stdout.write(f"\r[{datetime.now()}] Telegram Error: {e}    ")
        sys.stdout.flush()

def check_nvidia_stock():
    """Checks Nvidia's website for RTX 5090 stock using Selenium."""
    while True:
        try:
            driver.get(NVIDIA_URL)  # Use Chrome to access the API
            response = driver.page_source

            if "products" not in response:
                sys.stdout.write(f"\r[{datetime.now()}] No products found. Checking again in 60s...    ")
                sys.stdout.flush()
                time.sleep(60)
                continue

            products = response.json().get("products", [])
            if not products:
                sys.stdout.write(f"\r[{datetime.now()}] RTX 5090 still out of stock. Checking again in 60s...    ")
                sys.stdout.flush()
            else:
                for product in products:
                    digital_river_id = product.get("digitalRiverID", "")
                    if digital_river_id:
                        buy_link = BUY_LINK_TEMPLATE.format(digital_river_id)
                        message = f"🚀 RTX 5090 IN STOCK! Buy here: {buy_link}"
                        sys.stdout.write(f"\r[{datetime.now()}] {message}    \n")  # Print message and move to new line
                        sys.stdout.flush()
                        send_telegram_message(message)

        except Exception as e:
            sys.stdout.write(f"\r[{datetime.now()}] Error fetching stock: {e}    ")
            sys.stdout.flush()

        time.sleep(60)  # Wait 60 seconds before checking again

if __name__ == "__main__":
    check_nvidia_stock()
