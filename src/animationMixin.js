// animationMixin.js
export const animationMixin = {
  methods: {
    animateIntegerValue(key, finalValue, duration = 2000) {
      const startValue = this[key] || 0;
      const startTime = performance.now();

      const animate = (currentTime) => {
        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        const currentValue = startValue + (finalValue - startValue) * progress;

        // Arrotonda il valore all'intero inferiore
        this[key] = Math.floor(currentValue);

        if (progress < 1) {
          requestAnimationFrame(animate);
        }
      };

      requestAnimationFrame(animate);
    },
    animateFloatValue(key, finalValue, duration = 2000, decimals = 2) {
      const startValue = this[key] || 0;
      const startTime = performance.now();

      const animate = (currentTime) => {
        const elapsedTime = currentTime - startTime;
        const progress = Math.min(elapsedTime / duration, 1);
        const currentValue = startValue + (finalValue - startValue) * progress;

        // Mantieni il valore con i decimali specificati
        this[key] = parseFloat(currentValue.toFixed(decimals));

        if (progress < 1) {
          requestAnimationFrame(animate);
        }
      };

      requestAnimationFrame(animate);
    }
  }
};
