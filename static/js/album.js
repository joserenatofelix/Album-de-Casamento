document.addEventListener('DOMContentLoaded', () => {
  const imgs = Array.from(document.querySelectorAll('#thumbs .thumb')).map(t => t.dataset.file);
  const main = document.getElementById('main-photo');
  const prevBtn = document.getElementById('prev');
  const nextBtn = document.getElementById('next');
  const playBtn = document.getElementById('play');

  let idx = 0;
  let interval = null;
  let isSlideshowActive = false;

  // Adicionar ano atual no footer
  const now = new Date();
  const footerText = document.querySelector('footer .small');
  if (footerText) {
    footerText.textContent = `© ${now.getFullYear()} Renato & Cleonice - Todos os momentos especiais`;
  }

  // --- NEW SHOW FUNCTION ---
  function show(newIndex) {
    if (imgs.length === 0) return;
    const oldIndex = idx;
    newIndex = (newIndex + imgs.length) % imgs.length;

    if (newIndex === oldIndex && main.classList.contains('photo-in')) {
        if (!isSlideshowActive || (interval && newIndex !== (oldIndex + 1) % imgs.length)) {
            return;
        }
    }

    main.classList.add('photo-out');
    main.classList.remove('photo-in');

    setTimeout(() => {
        idx = newIndex;
        main.src = `/static/photos/${imgs[idx]}`;
        main.classList.remove('photo-out');
        main.classList.add('photo-in');

        document.querySelectorAll('#thumbs .thumb').forEach((thumb, index) => {
            thumb.classList.toggle('active-thumb', index === idx);
        });
    }, 400);
  }
  // --- END NEW SHOW FUNCTION ---

  // Navegação
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      show(idx - 1);
      if (isSlideshowActive) restartSlideshow();
    });
  }

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      show(idx + 1);
      if (isSlideshowActive) restartSlideshow();
    });
  }

  // Miniaturas
  document.querySelectorAll('#thumbs .thumb').forEach((t, i) => {
    t.addEventListener('click', () => {
      show(i);
      if (isSlideshowActive) restartSlideshow();
    });
  });

  // Slideshow
  function startSlideshow() {
    stopSlideshow();
    interval = setInterval(() => show(idx + 1), 4000);
    if (playBtn) {
      playBtn.innerHTML = '<i class="fas fa-pause"></i> Pausar';
      playBtn.classList.replace('btn-primary', 'btn-danger');
    }
    isSlideshowActive = true;
    if (progressBar) startProgressBar();
  }

  function stopSlideshow() {
    if (interval) {
      clearInterval(interval);
      interval = null;
    }
    if (playBtn) {
      playBtn.innerHTML = '<i class="fas fa-play"></i> Slideshow';
      playBtn.classList.replace('btn-danger', 'btn-primary');
    }
    isSlideshowActive = false;
  }

  function restartSlideshow() {
    stopSlideshow();
    startSlideshow();
  }

  if (playBtn) {
    playBtn.addEventListener('click', () => {
      if (isSlideshowActive) {
        stopSlideshow();
      } else {
        startSlideshow();
      }
    });
  }

  // Navegação por teclado
  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
      show(idx - 1);
      if (isSlideshowActive) restartSlideshow();
    }
    if (e.key === 'ArrowRight') {
      show(idx + 1);
      if (isSlideshowActive) restartSlideshow();
    }
    if (e.key === ' ' || e.key === 'Spacebar') {
      e.preventDefault();
      if (playBtn) playBtn.click();
    }
    if (e.key === 'Escape' && isSlideshowActive) {
      stopSlideshow();
    }
  });

  // Carregar a primeira imagem
  if (imgs.length > 0) {
    main.src = `/static/photos/${imgs[0]}`;
    main.classList.add('photo-in');
    if (document.querySelectorAll('#thumbs .thumb').length > 0) {
      document.querySelectorAll('#thumbs .thumb')[0].classList.add('active-thumb');
    }
  }

  // Swipe para dispositivos móveis
  let touchStartX = 0;
  let touchEndX = 0;

  main.parentElement.addEventListener('touchstart', e => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  main.parentElement.addEventListener('touchend', e => {
    touchEndX = e.changedTouches[0].screenX;
    handleSwipe();
  }, { passive: true });

  function handleSwipe() {
    const minSwipeDistance = 50;
    if (touchStartX - touchEndX > minSwipeDistance) {
      show(idx + 1);
      if (isSlideshowActive) restartSlideshow();
    }
    if (touchEndX - touchStartX > minSwipeDistance) {
      show(idx - 1);
      if (isSlideshowActive) restartSlideshow();
    }
  }

  // Preload de imagens
  function preloadImages() {
    imgs.forEach(img => {
      const preloadImg = new Image();
      preloadImg.src = `/static/photos/${img}`;
    });
  }
  window.addEventListener('load', preloadImages);

  // Barra de progresso
  let progressBar;
  if (imgs.length > 0) {
      const pBar = document.createElement('div');
      pBar.className = 'slideshow-progress';
      main.parentElement.style.position = 'relative';
      main.parentElement.appendChild(pBar);
      progressBar = pBar;
  }

  function startProgressBar() {
      if (!progressBar) return;
      progressBar.style.transition = 'none';
      progressBar.style.width = '0%';
      void progressBar.offsetWidth; // Reflow
      progressBar.style.transition = 'width 4s linear';
      progressBar.style.width = '100%';
  }
});
