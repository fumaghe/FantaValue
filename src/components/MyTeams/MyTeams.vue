<template>
  <div class="image-container">
    <img src="/public/comingSoon.png" alt="Coming Soon">
  </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 94vh; /* Questo assicura che l'immagine sia centrata in verticale su tutta l'altezza della finestra */
}

img {
  width: 80%;
}
</style>
