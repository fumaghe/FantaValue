<template>
    <h3 class="nome col-100">{{ player.nome }}</h3>
    <div class="row bg-light-gray rounded-10 card">
        <div class="main-info d-flex align-items-center justify-content-between">
            <img :src="`/stemmi/${player.team}.png`" alt="stemma squadra" class="stemma">
            <img 
                :src="`/avatar/${player.avatars}`" 
                alt="img avatar" 
                class="avatar" 
                @error="setDefaultAvatar"
            >
        </div>
        <div class="side-info d-flex align-items-center">
            <ul class="list-unstyled d-flex align-items-center">
                <li v-for="(key, index) in visibleStatsKeys" :key="index" class="fw-600">
                    <div class="stat-type">{{ statLabels[key] }}</div>
                    <span class="text-orange">{{ getTransformedStat(key) }}</span>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { store } from '../../store';

export default {
  props: {
    player: Object
  },
  methods: {
    setDefaultAvatar(event) {
      event.target.src = '/avatar/avatar.png';
    },
    // Metodo che trasforma le stats in interi se necessario
    getTransformedStat(key) {
      if (key === 'prezzo' || key === 'pma') {
        const dynamicKey = key;  // La chiave originale senza il suffisso numerico
        return Math.floor(store.getDynamicValue(this.player, dynamicKey));
      }
      return this.player[key]; // Ritorna il valore originale per le altre stats
    },
    selectPlayer(player) {
        store.selectedPlayer = player
    }
  },
  computed: {
    selectedStatsKeys() {
      return [
        'prezzo',
        'pma',
        'media_voto_23_24',
        'fanta_media_23_24',
        'fantavalue',
        'gol_23_24',
        'assist_23_24',
        'media_voto_22_23',
        'fanta_media_22_23',
        'gol_22_23',
        'assist_22_23',
        'percentuale_titolare'
      ];
    },
    statLabels() {
      return {
        prezzo: 'Prezzo',
        pma: 'PMA',
        media_voto_23_24: 'MV 23/24',
        fanta_media_23_24: 'FM 23/24',
        fantavalue: 'FantaValue',
        gol_23_24: 'Gol 23/24',
        assist_23_24: 'Assist 23/24',
        media_voto_22_23: 'MV 22/23',
        fanta_media_22_23: 'FM 22/23',
        gol_22_23: 'Gol 22/23',
        assist_22_23: 'Assist 22/23',
        percentuale_titolare: '% Titolare'
      };
    },
    // Mostra solo un numero limitato di elementi o tutti in base a showAll
    visibleStatsKeys() {
      return this.selectedStatsKeys; // Mostra tutte le stats di default
    }
  }
};
</script>

<style scoped>
.card {
    min-height: 40px;
}

span {
    font-size: 20px;
}

.stat-type {
  color: rgb(109, 109, 109);
  font-size: 12px;
  margin-bottom: 5px;
}

.avatar {
  width: auto;
  height: 30px;
}

.stemma {
  height: 30px;
  width: auto;
}

.nome {
  margin: 10px 0px 0px 5px;
  font-size: 15px;
}

li {
  text-align: center;
  width: 70px;
}

.main-info {
  width: 7%;
}

.side-info { 
  width: 93%;
  cursor: pointer; /* Icona di grab per il drag */
}

.card:hover {
    cursor: pointer;
    background-color: #d8d8d8;
}
</style>
