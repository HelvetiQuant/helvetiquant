
import time

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
        print(f"Trade aperto: {symbol} {direction} @ {entry_price} (leva {leverage}x)")

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
                print(f"Trade chiuso: {symbol} PnL: {pnl:.2f} USDT")
                return pnl
        print(f"Nessun trade aperto trovato per {symbol}")
        return 0

    def _calculate_pnl(self, trade, exit_price):
        entry = trade["entry_price"]
        leverage = trade["leverage"]
        direction = trade["direction"]
        size = self.balance / 3  # massimo 1/3 del capitale
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

# Esempio
if __name__ == "__main__":
    sim = TradeSimulator()
    sim.open_trade("1000PEPEUSDT", entry_price=0.00000100)
    time.sleep(1)
    sim.close_trade("1000PEPEUSDT", exit_price=0.00000110)
    print(f"Balance finale: {sim.get_balance()} USDT")
