window.onload = () => {
  // Simula fetch API (puoi sostituire con reale /api/status)
  fetch('/api/status')
    .then(res => res.json())
    .then(data => {
      document.getElementById('status').innerText = 'Online';
      document.getElementById('ai-decision').innerText = data.gpt;
      document.getElementById('claude-decision').innerText = data.claude;

      // PUMP BUTTON logic
      const btn = document.getElementById('pump-button');
      if (data.signal === 'PUMP') {
        btn.className = 'pump';
        btn.innerText = 'PUMP DETECTED – ENTER';
      } else if (data.signal === 'DUMP') {
        btn.className = 'dump';
        btn.innerText = 'DUMP DETECTED – ENTER';
      } else {
        btn.className = 'neutral';
        btn.innerText = 'No signal';
      }

      // Watchlist
      const list = document.getElementById('token-list');
      list.innerHTML = '';
      data.watchlist.forEach(token => {
        const li = document.createElement('li');
        li.innerText = token;
        list.appendChild(li);
      });
    });
};