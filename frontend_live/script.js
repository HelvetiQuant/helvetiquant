async function fetchMarketData() {
  try {
    const priceRes = await fetch("/price");
    const signalRes = await fetch("/signal");
    const tradesRes = await fetch("/trades");

    const price = await priceRes.json();
    const signal = await signalRes.json();
    const trades = await tradesRes.json();

    console.log({ price, signal, trades });

    document.getElementById("output").innerHTML = `
      <strong>Token:</strong> ${price.token}<br>
      <strong>Price:</strong> ${price.price}<br>
      <strong>Signal:</strong> ${signal.action} (Confidenza: ${signal.confidence})<br>
      <strong>Ultimi trade:</strong><br>
      ${trades.map(t => `Entry: ${t.entry}, Exit: ${t.exit}, Profit: ${t.profit}`).join("<br>")}
    `;
  } catch (error) {
    document.getElementById("output").innerText = "Errore nel recupero dati.";
    console.error(error);
  }
}

setInterval(fetchMarketData, 3000);