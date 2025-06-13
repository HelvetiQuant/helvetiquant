async function fetchMarketData() {
    try {
        const response = await fetch("https://api.bybit.com/v2/public/tickers");
        const data = await response.json();
        const tickers = data.result;

        const symbols = ["BTCUSDT", "ETHUSDT", "XRPUSDT"];
        const filtered = tickers.filter(t => symbols.includes(t.symbol));
        displayData(filtered);
    } catch (error) {
        console.error("Errore nel recupero dati:", error);
        document.getElementById("output").innerText = "Errore nel recupero dei dati";
    }
}

function displayData(tickers) {
    const container = document.getElementById("output");
    container.innerHTML = "";

    tickers.forEach(ticker => {
        const price = parseFloat(ticker.last_price);
        const change = parseFloat(ticker.percent_change_24h);
        const direction = change >= 0 ? "🟢" : "🔴";

        const line = document.createElement("div");
        line.innerText = `${direction} ${ticker.symbol}: $${price.toFixed(4)} (${change.toFixed(2)}%)`;
        line.style.color = change >= 0 ? "lime" : "red";
        container.appendChild(line);
    });
}

setInterval(fetchMarketData, 30000);
fetchMarketData();