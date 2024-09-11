<template>
  <div class="col-100 d-flex justify-content-center my-20 fascia-selector">
    <button
      v-for="(slot, index) in slots"
      :key="index"
      class="fascia-button text-white bg-black"
      @click="selectFascia(slot)"
    >
      Vai alla {{ slot }} Fascia
    </button>
  </div>
</template>

<script>
export default {
  props: {
    slots: Array // Array di slot delle fasce che viene passato dal componente genitore
  },
  methods: {
    selectFascia(slot) {
      this.$emit('fascia-selected', slot); // Emette l'evento per scrollare alla fascia selezionata
    }
  }
};
</script>

<style scoped>
.fascia-selector {
  margin-bottom: 20px;
}

.fascia-button {
  padding: 10px 20px;
  margin: 5px;
  border: none;
  cursor: pointer;
  background-color: #15212A;
  color: white;
  border-radius: 5px;
  font-size: var(--font-size-m);
}
</style>
