import { reactive } from "vue";

export const store = reactive({
   players: [], // Qui memorizzeremo il nostro array di oggetti
   selectedPlayer: {},
   similarPlayers: [],
   playersT1: [],
   playersT2: [],
   budgetValue: 500,
   getDynamicValue(player, property) {
      return player ? player[`${property}${this.budgetValue}`] : null;
   },
   pmaData: [],
   priceData: []
})