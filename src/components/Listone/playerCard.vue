<template>
  <div :class="['player-card-wrapper', { 'expanded-card': showStats }]" :style="{ order: showStats ? rowStartIndex : index }">
    <div class="player-card bg-light-gray rounded-10" @click="toggleStats">
      <div :class="{ 'content-card' : showStats }">
        <h3 class="player-name fw-800 fs-l p-10">{{ player.nome }}</h3>
        <div class="d-flex align-items-center">
          <img :src="`/img_giocatori/${player.img}`" :alt="player.nome" class="player-img">
          <ul class="list-unstyled">
            <li>
              <div class="stats fw-600 fs-s text-center">
                <img src="../../assets/grafiche/price_black.png" alt="">
              </div>
              <span class="fw-600 fs-s text-orange">{{ animatedPrezzo }}</span>
            </li>
            <li><div class="stats fw-600 fs-s text-center">PMA:</div> <span class="fw-600 fs-s text-orange">{{ animatedPma500 }}</span></li>
            <li><div class="stats fw-600 fs-s text-center">FM:</div> <span class="fw-600 fs-s text-orange">{{ animatedFmv }}</span></li>
            <li><div class="stats fw-600 fs-s text-center">MV:</div> <span class="fw-600 fs-s text-orange">{{ animatedMv }}</span></li>
          </ul>
        </div>
        <img :src="`/stemmi/${player.team}.png`" :alt="player.team" class="team-logo-img">
      </div>
        <playerFantaValueOverall :selectedPlayer="player" :fontSize="30" :isResponsiveFont="false" v-if="showStats" class="fantaValueOverall"/>
        <bestMatches :selectedPlayer="player" :players="store.players" :hasBorderTop="false" v-if="showStats" class="bestMatches"/>
        <playerSeasonsStats :selectedPlayer="player" :isInPlayerCard="true" v-if="showStats" class="seasonsStats"/>
    </div>
  </div>
</template>

<script>
import playerFantaValueOverall from '../Home/playerFantaValueOverall.vue';
import bestMatches from '../Home/bestMatches.vue';
import playerSeasonsStats from '../Home/playerSeasonsStats.vue';
import { store } from '../../store.js';
import { animationMixin } from '../../animationMixin.js';

export default {
  mixins: [animationMixin],
  components: {
    playerFantaValueOverall,
    bestMatches,
    playerSeasonsStats
  },
  props: {
    player: Object,
    index: Number, // Indice della card per la gestione
    activeCardIndex: Number // Prop per determinare la card attiva
  },
  data() {
    return {
      store,
      animatedPrezzo: 0,
      animatedPma500: 0,
      animatedFmv: 0,
      animatedMv: 0
    };
  },
  computed: {
    showStats() {
      return this.activeCardIndex === this.index;
    },
    // Determina l'offset dell'indice di inizio riga in base alla larghezza dello schermo
    rowStartIndex() {
      if (window.innerWidth >= 1200) {
        return Math.floor(this.index / 4) * 4; // 4 card per riga per schermi grandi
      } else if (window.innerWidth >= 768) {
        return Math.floor(this.index / 3) * 3; // 3 card per riga per schermi medi
      } else if (window.innerWidth >= 568) {
        return Math.floor(this.index / 2) * 2; // 2 card per riga per schermi piccoli
      } else {
        return this.index; // 1 card per riga per schermi extra piccoli
      }
    },
    isFirstInRow() {
      // Se la card è attiva, controlliamo se deve essere posizionata per prima nella riga
      return this.activeCardIndex >= this.rowStartIndex && this.activeCardIndex < this.rowStartIndex + this.getCardsPerRow();
    },
    getCardsPerRow() {
      if (window.innerWidth >= 1200) {
        return 4; // 4 card per riga per schermi grandi
      } else if (window.innerWidth >= 768) {
        return 3; // 3 card per riga per schermi medi
      } else if (window.innerWidth >= 568) {
        return 2; // 2 card per riga per schermi piccoli
      } else {
        return 1; // 1 card per riga per schermi extra piccoli
      }
    }
  },
  watch: {
    showStats: {
      immediate: true,
      handler(newValue) {
        if (newValue) {
          this.startAnimation();
        }
      }
    }
  },
  mounted() {
    this.startAnimation()
  },
  methods: {
    toggleStats() {
      this.$emit('updateActiveCard', this.index);
    },
    startAnimation() {
      this.animateIntegerValue('animatedPrezzo', this.player.prezzo, 2000);
      this.animateIntegerValue('animatedPma500', this.player.pma500, 2000, 2);
      this.animateFloatValue('animatedFmv', this.player.fmv, 2000, 2);
      this.animateFloatValue('animatedMv', this.player.mv, 2000, 2);
    }
  }
};
</script>

<style scoped>
/* Stile del PlayerCard come già descritto */
.player-card-wrapper {
  margin-bottom: 40px;
  padding: 0 20px;
  width: 100%;
  transition: width 0.5s ease, order 0.5s ease;
  cursor: pointer;
}

.player-card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  position: relative;
  padding-top: 10px;
  width: 100%;
}

.player-name {
  margin: 10px;
}

.player-img {
  width: 50%;
  height: auto;
  margin-top: 10px;
}

.team-logo-img {
  position: absolute;
  right: 0;
  bottom: 0;
  transform: translate(50%, 50%);
  width: 55px;
  height: auto;
}

.list-unstyled {
  width: 100%;
}

.list-unstyled li {
  margin: 10px 0px;
}

.stats {
  width: 50%;
  display: inline-block;
}

.stats img {
  width: auto;
  height: 20px;
}

.expanded-card {
  width: 100%;
}

@media (min-width: 568px) {
  .player-card-wrapper {
    width: 50%;
  }
  .expanded-card {
    width: 100%;
  }
}

@media (min-width: 768px) {
  .player-card-wrapper {
    width: calc(100% / 3);
  }
  
  .expanded-card {
    width: 100%;
  }

  .player-card {
    display: flex;
    flex-wrap: wrap;
  }

  .content-card {
    width: 40%;
  }

  .fantaValueOverall {
    width: 60%;
  }

  .bestMatches {
    width: 50%;
  }

  .seasonsStats {
    width: 50%;
  }
}

@media (min-width: 1200px) {
  .player-card-wrapper {
    width: 25%;
  }

  .expanded-card {
    width: 100%;
  }
}
</style>
