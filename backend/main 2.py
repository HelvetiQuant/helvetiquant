
import time
from datetime import datetime
from trade_simulator import TradeSimulator
from report_generator import generate_daily_report
from telegram_notifier import send_telegram_message

# Inizializza simulatore con capitale 3600 USDT
simulator = TradeSimulator(starting_balance=3600)

def simulate_trading_day():
    # Esempio: apriamo e chiudiamo un trade simulato
    simulator.open_trade("1000PEPEUSDT", entry_price=0.00000100)
    time.sleep(2)
    simulator.close_trade("1000PEPEUSDT", exit_price=0.00000120)

def daily_report_and_notify():
    trades = simulator.get_trade_history()
    balance = simulator.get_balance()
    pdf_path = generate_daily_report(balance=balance, trades=trades)
    send_telegram_message(f"📄 Report giornaliero generato. Bilancio: {balance:.2f} USDT")
    with open(pdf_path, "rb") as f:
        requests.post(
            url=f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendDocument",
            data={"chat_id": os.getenv("TELEGRAM_CHAT_ID")},
            files={"document": f}
        )

def run_loop():
    while True:
        now = datetime.now()
        if now.hour == 20 and now.minute == 0:
            print("🕗 Generazione report delle 20:00")
            daily_report_and_notify()
            time.sleep(60)
        else:
            time.sleep(30)

if __name__ == "__main__":
    simulate_trading_day()  # solo per test
    run_loop()
