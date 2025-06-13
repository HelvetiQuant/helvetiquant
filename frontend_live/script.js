async function fetchMarketData() {
    try {
        const res = await fetch("https://helvetiquanta.up.railway.app/price");
        const data = await res.json();
        displayData(data);
    } catch (error) {
        console.error("Errore nel recupero dati:", error);
        document.getElementById("output").innerText = "Errore nel caricamento.";
    }
}

function displayData(ticker) {
    const container = document.getElementById("output");
    container.innerHTML = `
        <strong>Token:</strong> ${ticker.token}<br>
        <strong>Prezzo:</strong> ${ticker.price}<br>
        <strong>Timestamp:</strong> ${ticker.timestamp}
    `;
}

setInterval(fetchMarketData, 3000);