
document.addEventListener("DOMContentLoaded", async () => {
    try {
        const watchlist = await fetch('/api/watchlist').then(res => res.json());
        const sentiment = await fetch('/api/sentiment').then(res => res.json());
        const macro = await fetch('/api/macro-news').then(res => res.json());

        console.log("Top 10 Token AI:", watchlist);
        console.log("Sentiment:", sentiment);
        console.log("News & Macro:", macro);

        // Qui puoi aggiungere logica per aggiornare il DOM
    } catch (err) {
        console.error("Errore durante fetch dati:", err);
    }
});
