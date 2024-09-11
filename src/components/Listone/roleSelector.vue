<template>
  <div class="col-100 d-flex justify-content-center my-20">
    <button
      v-for="(role, index) in roles"
      :key="index"
      :class="['text-white', getBackgroundClass(role), role.selected ? 'selected' : 'dimmed', 'hover-effect']"
      class="role-button"
      @click="selectRole(role, index)"
    >
      {{ role.ruolo }}
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedRole: 'A', // Ruolo selezionato di default
      roles: [
        { ruolo: 'P', selected: false },
        { ruolo: 'D', selected: false },
        { ruolo: 'C', selected: false },
        { ruolo: 'A', selected: true }
      ]
    };
  },
  methods: {
    selectRole(role) {
      // Resetta lo stato di selezione
      this.roles.forEach(r => (r.selected = false));
      role.selected = true;
      this.selectedRole = role.ruolo;

      // Invia l'informazione al genitore
      this.$emit('role-selected', this.selectedRole);
    },
    getBackgroundClass(role) {
      switch (role.ruolo) {
        case 'P':
          return 'bg-portieri';
        case 'D':
          return 'bg-difensori';
        case 'C':
          return 'bg-centrocampisti';
        case 'A':
          return 'bg-attaccanti';
        default:
          return 'bg-black'; // Valore predefinito
      }
    }
  }
};
</script>

<style scoped>
button {
  padding: 10px 25px;
  border-radius: 10px;
  border: none;
  margin-right: 10px;
  font-size: var(--font-size-m);
  cursor: pointer;
  transition: all 0.3s ease; /* Aggiunge una transizione fluida */
}

.role-button {
  margin: 0 10px;
}

.selected {
  filter: brightness(1); /* Mantiene il colore originale per il pulsante selezionato */
}

.dimmed {
  filter: brightness(0.7); /* Riduce la luminosità dei pulsanti non selezionati */
}

.bg-portieri {
  background-color: #EE9E1D;
}

.bg-difensori {
  background-color: #489B13;
}

.bg-centrocampisti {
  background-color: #276CE1;
}

.bg-attaccanti {
  background-color: #BB1523;
}

.bg-black {
  background-color: black;
}

/* Effetti di hover */
.hover-effect:hover {
  transform: scale(1.1); /* Ingrandisce il pulsante */
  filter: brightness(1); /* Riporta la luminosità a livello normale al passaggio del mouse */
}

/* Effetti di attivazione (clic) con transizione */
button:active {
  transition: transform 0.5s ease, background-color 0.2s ease;
}

/* Modifica il colore di sfondo al clic */
.bg-portieri:active {
  background-color: #d88a18;
}

.bg-difensori:active {
  background-color: #3f8511;
}

.bg-centrocampisti:active {
  background-color: #215bba;
}

.bg-attaccanti:active {
  background-color: #97131e;
}

.bg-black:active {
  background-color: #333;
}
</style>
