<template>
  <div class="col-100">
    <div class="form-check">
      <label class="form-check-label" for="flexSwitchCheckDefault">Compatta:</label>
      <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="isCompact" @change="updateSwitchState">
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isCompact: false
    };
  },
  methods: {
    updateSwitchState() {
      this.$emit('compact-mode-changed', this.isCompact);
    }
  }
};
</script>

<style scoped>
.form-check {
  display: flex;
  align-items: center;
}

.form-check-label {
  margin-right: 10px;
}

.form-check-input {
  position: relative;
  width: 40px;
  height: 20px;
  appearance: none;
  background-color: #ccc;
  border-radius: 20px;
  outline: none;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.form-check-input:before {
  content: "";
  position: absolute;
  width: 16px;
  height: 16px;
  background-color: white;
  border-radius: 50%;
  top: 2px;
  left: 2px;
  transition: transform 0.3s ease;
}

.form-check-input:checked {
  background-color: #FE4C10;
}

.form-check-input:checked:before {
  transform: translateX(20px);
}
</style>
