document.addEventListener('DOMContentLoaded', () => {
  const slider = document.querySelector('.slider');
  const beforeImage = document.querySelector('.image-container.before img');
  const sliderWrapper = document.querySelector('.slider-wrapper');
  const infoTexts = document.querySelectorAll('.info-text');

  if (!slider || !beforeImage || !sliderWrapper) {
    return;
  }

  let isDragging = false;
  let currentPercentage = 0.5;

  const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

  const setSliderPosition = (percentage) => {
    currentPercentage = clamp(percentage, 0, 1);
    slider.style.left = `${currentPercentage * 100}%`;
    beforeImage.style.clipPath = `inset(0 ${(1 - currentPercentage) * 100}% 0 0)`;
  };

  const hideInfoTexts = () => {
    infoTexts.forEach((text) => text.classList.add('hidden'));
  };

  const getClientX = (event) => {
    if (event.touches && event.touches.length > 0) {
      return event.touches[0].clientX;
    }
    if (event.changedTouches && event.changedTouches.length > 0) {
      return event.changedTouches[0].clientX;
    }
    return event.clientX;
  };

  const updateFromEvent = (event) => {
    const rect = sliderWrapper.getBoundingClientRect();
    const offsetX = getClientX(event) - rect.left;
    setSliderPosition(offsetX / rect.width);
  };

  const startDrag = (event) => {
    isDragging = true;
    hideInfoTexts();
    updateFromEvent(event);
    event.preventDefault();
  };

  const stopDrag = () => {
    isDragging = false;
  };

  const onMove = (event) => {
    if (!isDragging) {
      return;
    }
    updateFromEvent(event);
    event.preventDefault();
  };

  slider.addEventListener('mousedown', startDrag);
  slider.addEventListener('touchstart', startDrag, { passive: false });
  sliderWrapper.addEventListener('click', updateFromEvent);

  window.addEventListener('mousemove', onMove);
  window.addEventListener('touchmove', onMove, { passive: false });
  window.addEventListener('mouseup', stopDrag);
  window.addEventListener('touchend', stopDrag);
  window.addEventListener('resize', () => setSliderPosition(currentPercentage));

  setSliderPosition(currentPercentage);
});