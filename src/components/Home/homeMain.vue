<script>
import { store } from "../../store.js";
import playerSearchBar from "./playerSearchBar.vue";
import playerStatsAndImg from "./playerStatsAndImg.vue";
import playerDataAndSimilar from "./playerDataAndSimilar.vue";
import playerFantaValueOverall from "./playerFantaValueOverall.vue";
import bestMatches from "./bestMatches.vue";
import playerSeasonsStats from "./playerSeasonsStats.vue";

export default {
  components: {
    playerSearchBar,
    playerStatsAndImg,
    playerDataAndSimilar,
    playerFantaValueOverall,
    bestMatches,
    playerSeasonsStats,
  },
  data() {
    return {
      name: "PlayerComponent",
      store,
    };
  },
  mounted() {
    if (store.players.length > 0) {
      store.selectedPlayer = store.players[396];
    } else {
      this.$watch(
        () => store.players,
        (newPlayers) => {
          if (newPlayers.length > 0) {
            store.selectedPlayer = newPlayers[396];
          }
        },
        { immediate: true, deep: true }
      );
    }
  },
};
</script>

<template>
  <main>
    <div class="container">
      <playerSearchBar />
      <playerStatsAndImg
        v-if="store.selectedPlayer"
        :player="store.selectedPlayer"
      />
    </div>
    <playerDataAndSimilar
      :player="store.selectedPlayer"
      :similarPlayers="store.similarPlayers"
    />
    <bestMatches
      :selectedPlayer="store.selectedPlayer"
      :hasBorderTop="true"
      :players="store.players"
    />
    <!-- <playerFantaValueOverall :selectedPlayer="store.selectedPlayer" :isResponsiveFont="true" /> -->
    <playerSeasonsStats :selectedPlayer="store.selectedPlayer" />
  </main>
</template>

<style>
main {
  padding-top: 100px;
}

@media (min-width: 768px) {
  main {
    padding-top: 60px;
  }
}
</style>
