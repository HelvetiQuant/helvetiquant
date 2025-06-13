
from fpdf import FPDF
import os
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'HelvetiQuant – Report Giornaliero', ln=True, align='C')
        self.ln(10)

    def add_summary(self, balance, trade_count):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Data: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', ln=True)
        self.cell(0, 10, f'Saldo attuale: {balance:.2f} USDT', ln=True)
        self.cell(0, 10, f'Trade eseguiti: {trade_count}', ln=True)
        self.ln(5)

    def add_trade_table(self, trades):
        self.set_font('Arial', 'B', 11)
        self.cell(40, 10, 'Simbolo', 1)
        self.cell(30, 10, 'Entrata', 1)
        self.cell(30, 10, 'Uscita', 1)
        self.cell(30, 10, 'PnL', 1)
        self.cell(30, 10, 'Leva', 1)
        self.ln()
        self.set_font('Arial', '', 10)
        for t in trades:
            self.cell(40, 10, t['symbol'], 1)
            self.cell(30, 10, str(t['entry_price']), 1)
            self.cell(30, 10, str(t.get('exit_price', '-')), 1)
            self.cell(30, 10, f"{t.get('pnl', 0):.2f}", 1)
            self.cell(30, 10, f"{t['leverage']}x", 1)
            self.ln()

def generate_daily_report(balance, trades, out_dir="reports"):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    pdf = PDFReport()
    pdf.add_page()
    pdf.add_summary(balance, len(trades))
    pdf.add_trade_table(trades)

    filename = os.path.join(out_dir, f"report_{datetime.now().strftime('%Y-%m-%d')}.pdf")
    pdf.output(filename)
    print(f"📄 Report salvato: {filename}")
    return filename

# Esempio d'uso
if __name__ == "__main__":
    trades = [{
        "symbol": "1000PEPEUSDT",
        "entry_price": 0.00000100,
        "exit_price": 0.00000120,
        "pnl": 48.0,
        "leverage": 25
    }]
    generate_daily_report(balance=3648.0, trades=trades)
