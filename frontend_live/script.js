
document.addEventListener("DOMContentLoaded", () => {
    const statusDisplay = document.getElementById("status");
    const startBtn = document.getElementById("startBtn");
    const stopBtn = document.getElementById("stopBtn");

    async function updateStatus() {
        const res = await fetch("http://localhost:8000/status");
        const data = await res.json();
        statusDisplay.textContent = data.status === "running" ? "🟢 Attivo" : "🔴 Inattivo";
    }

    startBtn.addEventListener("click", async () => {
        await fetch("http://localhost:8000/start", { method: "POST" });
        updateStatus();
    });

    stopBtn.addEventListener("click", async () => {
        await fetch("http://localhost:8000/stop", { method: "POST" });
        updateStatus();
    });

    updateStatus();
});


    async function updateWhaleData() {
        const list = document.getElementById("whale-list");
        try {
            const res = await fetch("http://localhost:8000/whale-alert");
            const data = await res.json();
            if (!data.transactions || data.transactions.length === 0) {
                list.innerHTML = "<p>Nessuna transazione rilevante.</p>";
                return;
            }
            list.innerHTML = data.transactions.map(tx => `
                <div style="padding:10px; border-bottom:1px solid #444;">
                    <strong>${tx.symbol}</strong> → <span style="color:#0f0;">$${tx.amount_usd.toLocaleString()}</span><br/>
                    <small>${tx.timestamp} — da ${tx.from} a ${tx.to}</small>
                </div>
            `).join("");
        } catch (e) {
            list.innerHTML = "<p style='color:red;'>Errore nel caricamento dati whale.</p>";
        }
    }

    setInterval(updateWhaleData, 30000);  // ogni 30 sec
    updateWhaleData();
