document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.falling-hearts-container');
  if (!container) return;

  const numberOfHearts = 25; // Ajuste a quantidade de corações

  for (let i = 0; i < numberOfHearts; i++) {
    const heart = document.createElement('div');
    heart.classList.add('heart');
    heart.innerHTML = '♥'; // Caractere de coração

    // Posições e animações aleatórias
    heart.style.left = `${Math.random() * 100}vw`;
    heart.style.animationDuration = `${Math.random() * 5 + 8}s`; // Duração entre 8s e 13s
    heart.style.animationDelay = `${Math.random() * 10}s`; // Começa em tempos diferentes
    heart.style.fontSize = `${Math.random() * 16 + 10}px`; // Tamanhos entre 10px e 26px
    heart.style.opacity = Math.random() * 0.5 + 0.3; // Opacidade entre 0.3 e 0.8

    container.appendChild(heart);
  }
});