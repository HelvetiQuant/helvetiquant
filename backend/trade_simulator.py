
import time
from telegram_notifier import send_telegram_message

class TradeSimulator:
    def __init__(self, starting_balance=3600):
        self.balance = starting_balance
        self.active_trades = []
        self.trade_history = []

    def open_trade(self, symbol, entry_price, leverage=25, direction="LONG"):
        trade = {
            "symbol": symbol,
            "entry_price": entry_price,
            "direction": direction,
            "leverage": leverage,
            "open_time": time.time(),
            "status": "OPEN"
        }
        self.active_trades.append(trade)
        msg = f"📥 *TRADE APERTO*
"               f"Symbol: `{symbol}`
"               f"Direzione: *{direction}*
"               f"Prezzo Entrata: `{entry_price}`
"               f"Leva: `{leverage}x`"
        send_telegram_message(msg)

    def close_trade(self, symbol, exit_price):
        for trade in self.active_trades:
            if trade["symbol"] == symbol and trade["status"] == "OPEN":
                pnl = self._calculate_pnl(trade, exit_price)
                trade["exit_price"] = exit_price
                trade["pnl"] = pnl
                trade["close_time"] = time.time()
                trade["status"] = "CLOSED"
                self.balance += pnl
                self.trade_history.append(trade)
                self.active_trades.remove(trade)

                msg = f"📤 *TRADE CHIUSO*
"                       f"Symbol: `{symbol}`
"                       f"Prezzo Uscita: `{exit_price}`
"                       f"PnL: `{pnl:.2f} USDT`
"                       f"💰 Balance attuale: `{self.get_balance()} USDT`"
                send_telegram_message(msg)
                return pnl
        return 0

    def _calculate_pnl(self, trade, exit_price):
        entry = trade["entry_price"]
        leverage = trade["leverage"]
        direction = trade["direction"]
        size = self.balance / 3
        delta = (exit_price - entry) / entry
        if direction == "SHORT":
            delta *= -1
        return size * delta * leverage

    def get_balance(self):
        return round(self.balance, 2)

    def get_open_trades(self):
        return self.active_trades

    def get_trade_history(self):
        return self.trade_history

if __name__ == "__main__":
    sim = TradeSimulator()
    sim.open_trade("1000PEPEUSDT", entry_price=0.00000100)
    time.sleep(1)
    sim.close_trade("1000PEPEUSDT", exit_price=0.00000110)
    print(f"Balance finale: {sim.get_balance()} USDT")
