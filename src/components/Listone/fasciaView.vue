<template>
  <div class="container">
    <div class="row">
      <div
        class="col-100 text-center bg-black rounded-10 my-10 clickable"
        :class="{ 'active': isActive }"
        @click="toggleSlot"
      >
        <h2 class="text-orange my-20 fs-xl">{{ fascia }} Fascia</h2>
      </div>

      <transition-group
        name="list"
        tag="div"
        class="row fascia-container"
        :class="{ 'fascia-open': !isHidden, 'fascia-closed': isHidden }"
      >
        <div v-if="!isCompactMode">
          <PlayerCard
            v-for="(player, index) in sortedPlayers"
            :key="player.nome"
            :player="player"
            :index="index"
            :activeCardIndex="activeCardIndex"
            @updateActiveCard="updateActiveCard"
            @open-modal="openPlayerModal"
            class="list-item"
          />
        </div>
        <div v-else>
          <PlayerCardCompact
            v-for="(player, index) in sortedPlayers"
            :key="player.nome"
            :player="player"
          />
        </div>
      </transition-group>
    </div>
  </div>
</template>

<script>
import PlayerCard from './playerCard.vue';
import PlayerCardCompact from './playerCardCompact.vue';

export default {
  components: {
    PlayerCard,
    PlayerCardCompact
  },
  props: {
    fascia: String,
    players: Array,
    isCompactMode: Boolean
  },
  data() {
    return {
      isHidden: false,
      isActive: false,
      activeCardIndex: null // Stato per gestire la card attiva
    };
  },
  computed: {
    sortedPlayers() {
      // Ordina i giocatori in base al prezzo in ordine decrescente
      return [...this.players].sort((a, b) => b.prezzo - a.prezzo);
    }
  },
  methods: {
    toggleSlot() {
      // Aggiungi feedback visivo
      this.isActive = true;

      // Ripristina lo stato dopo un breve ritardo
      setTimeout(() => {
        this.isActive = false;
        this.isHidden = !this.isHidden;
      }, 200);
    },
    updateActiveCard(index) {
      // Se la stessa card è cliccata, chiudi la card aperta
      if (this.activeCardIndex === index) {
        this.activeCardIndex = null;
      } else {
        // Imposta la card attiva
        this.activeCardIndex = index;
      }
    },
    openPlayerModal(player) {
      this.$emit('open-modal', player);
    }
  }
};
</script>

<style scoped>
/* Stile per la transizione dell'altezza della fascia */
.fascia-container {
  overflow: hidden;
  transition: max-height 0.4s ease;
  max-height: 12000px;
}

.fascia-closed {
  max-height: 0;
}

/* Animazioni per il riordino delle card */
.list-item {
  display: inline-block;
  transition: transform 0.3s ease, opacity 0.3s ease;
}

/* Transizione per gli elementi che entrano e escono */
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}
.list-enter,
.list-leave-to {
  opacity: 0;
  transform: translateY(20px);
}

/* Stile base per il pulsante cliccabile */
.clickable {
  transition: transform 0.2s ease, background-color 0.2s ease;
  cursor: pointer;
}

/* Stile per l'effetto attivo */
.clickable.active {
  transform: scale(1.05);
  background-color: #333;
}
</style>
