<template>
    <main>

        <div class="container">
            <div class="row">
                <!-- Intestazione -->
                <div class="col-100 text-center border-bottom">
                <h1 class="text-orange my-20">LISTONE & FASCE</h1>
                </div>
                <!-- Selettori Fasce (Scroll Navigator) -->
                <!-- <FasciaSelector :slots="fasciaSlots" @fascia-selected="scrollToSlot" /> -->
                
                <!-- Selettori Ruolo -->
                <roleSelector @role-selected="handleRoleSelection" />
                <chooseCompactExtended @compact-mode-changed="handleCompactModeChange" />
            </div>
        </div>
        
        <!-- Visualizzazione Fasce -->
        <FasciaView
            v-for="(players, slot) in filteredPlayersBySlot"
            :key="slot"
            :fascia="slot"
            :players="players"
            :isCompactMode="isCompactMode"
        />
    </main>
</template>
  
<script>
import { store } from '../../store';
import roleSelector from './roleSelector.vue';
import fasciaSelector from './fasciaSelector.vue';  
import FasciaView from './fasciaView.vue';
import chooseCompactExtended from './chooseCompactExtended.vue';

export default {
    components: {
        roleSelector,
        fasciaSelector,
        FasciaView,
        chooseCompactExtended
    },
    data() {
      return {
        selectedRole: 'A',
        hiddenSlots: [],
        fasciaOrder: ['Prima', 'Seconda', 'Terza', 'Quarta', 'Scommesse', 'Outsider', 'Titolare "Scarso"', 'Non Impostata'],
        isCompactMode: false
      };
    },
    computed: {
        filteredPlayersBySlot() {
            // Filtra i giocatori per ruolo
            const filteredPlayers = store.players.filter(player => player.ruolo === this.selectedRole);
           
            // Raggruppa i giocatori per fascia
            const playersByFascia = filteredPlayers.reduce((acc, player) => {
                if (!acc[player.fascia]) acc[player.fascia] = [];
                acc[player.fascia].push(player);
                return acc;
            }, {});

            // Ordina le fasce secondo l'ordine specificato
            const orderedFasce = {};
            this.fasciaOrder.forEach(fascia => {
                if (playersByFascia[fascia]) {
                    orderedFasce[fascia] = playersByFascia[fascia];
                }
            });

            return orderedFasce;
        }
    },
    methods: {
        handleRoleSelection(selectedRole) {
            this.selectedRole = selectedRole;
        },
        handleCompactModeChange(isCompact) {
            this.isCompactMode = isCompact;
        }
    }
}

</script>
  
<style scoped>
    /* Stili generali */
    .border-bottom {
        border-bottom: 1px solid rgb(223, 223, 223);
    }

    main {
        padding-top: 100px;
    }

    @media (min-width: 768px) {
        main {
            padding-top: 60px;
        }
    }
</style>
  