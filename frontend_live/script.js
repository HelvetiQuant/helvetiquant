async function fetchMarketData() {
    try {
        const res = await fetch('/price');
        const data = await res.json();
        displayData(data);
    } catch (error) {
        console.error("Errore nel recupero dati:", error);
        document.getElementById("output").innerText = "Errore nel caricamento.";
    }
}

function displayData(ticker) {
    const container = document.getElementById("output");
    container.innerHTML = `Token: ${ticker.token}<br>Prezzo: ${ticker.price}<br>Timestamp: ${ticker.timestamp}`;
}

setInterval(fetchMarketData, 3000);