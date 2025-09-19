document.addEventListener('DOMContentLoaded', () => {
  const audio = document.getElementById('bg-music');
  if (audio) {
    // tenta tocar automaticamente
    audio.play().catch(() => {
      // se bloqueado pelo navegador, mostra o botão
      const btn = document.getElementById('music-play-btn');
      if (btn) btn.style.display = 'inline-block';
    });
  }

  // botão manual
  const btn = document.getElementById('music-play-btn');
  if (btn) {
    btn.addEventListener('click', () => {
      audio.play();
      btn.style.display = 'none';
    });
  }
});
