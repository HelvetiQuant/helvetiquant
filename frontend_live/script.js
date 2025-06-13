async function fetchData() {
    const priceRes = await fetch("/price");
    const signalRes = await fetch("/signal");
    const tradesRes = await fetch("/trades");

    const priceData = await priceRes.json();
    const signalData = await signalRes.json();
    const tradesData = await tradesRes.json();

    document.getElementById("token").innerText = priceData.token;
    document.getElementById("price").innerText = priceData.price;
    document.getElementById("signal").innerText = signalData.action;
    document.getElementById("confidence").innerText = signalData.confidence;

    const tradeList = document.getElementById("trade-list");
    tradeList.innerHTML = "";
    tradesData.forEach(trade => {
        const item = document.createElement("li");
        item.innerText = `Entry: ${trade.entry}, Exit: ${trade.exit}, Profit: ${trade.profit}`;
        tradeList.appendChild(item);
    });
}

setInterval(fetchData, 3000);
fetchData();