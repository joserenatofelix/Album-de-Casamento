
document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.falling-roses-container');
  if (!container) return;

  const numberOfRoses = 20; // Ajuste a quantidade de rosas

  for (let i = 0; i < numberOfRoses; i++) {
    const rose = document.createElement('div');
    rose.classList.add('rose');
    rose.innerHTML = '❀'; // Você pode usar '❀', '✿', '🌹'

    // Posições e animações aleatórias
    rose.style.left = `${Math.random() * 100}vw`;
    rose.style.animationDuration = `${Math.random() * 5 + 8}s`; // Duração entre 8s e 13s
    rose.style.animationDelay = `${Math.random() * 10}s`; // Começa em tempos diferentes
    rose.style.fontSize = `${Math.random() * 16 + 12}px`; // Tamanhos entre 12px e 28px
    rose.style.opacity = Math.random() * 0.5 + 0.4; // Opacidade entre 0.4 e 0.9

    container.appendChild(rose);
  }
});
