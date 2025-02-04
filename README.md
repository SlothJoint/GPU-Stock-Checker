NVIDIA RTX 5090 Stock Checker 🚀

This script checks the NVIDIA store for RTX 5090 availability and sends a notification via Telegram when the GPU is in stock.

📥 Installation & Usage

1️⃣ Clone the Repository

To get started, open a terminal and run:

git clone https://github.com/SlothJoint/GPU-Stock-Checker.git
cd GPU-Stock-Checker

2️⃣ Install Dependencies

Make sure you have Python 3 installed, then run:

pip3 install -r requirements.txt

3️⃣ Configure Environment Variables

Before running the script, update the following values inside the script:

TELEGRAM_BOT_TOKEN: Your Telegram bot API token.

TELEGRAM_CHAT_ID: Your Telegram chat ID.

CHROMEDRIVER_PATH: Path to your ChromeDriver executable.

4️⃣ Run the Script

Start checking for stock by running:

python3 nvidia_stock_checker.py
