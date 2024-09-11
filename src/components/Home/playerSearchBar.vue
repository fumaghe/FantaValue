<template>
    <div class="row">
        <budgetSection />
        <div class="col-100 my-20">
            <div class="player-search-container position-relative">
                <div class="input-group my-10">
                    <input 
                        type="text" 
                        class="form-control" 
                        placeholder="Nome Giocatore" 
                        aria-label="Player's name" 
                        aria-describedby="search-button" 
                        v-model="searchQuery" 
                        @input="filterPlayers"
                        @keydown.down.prevent="navigateSuggestions(1)"
                        @keydown.up.prevent="navigateSuggestions(-1)"
                        @keydown.enter.prevent="selectHighlightedPlayer"
                    />
                    <button class="btn bg-orange border-0" type="button">
                        <i class="fa-solid fa-magnifying-glass text-white"></i>
                    </button>
                    <ul v-if="filteredPlayers.length" class="suggested-players" ref="suggestionsList">
                        <li 
                            v-for="(player, index) in filteredPlayers" 
                            :key="player.nome" 
                            @click="selectPlayer(player)" 
                            class="player-item" 
                            :class="{ 'highlighted': index === highlightedIndex }"
                            ref="playerItems"
                        >
                            <img 
                                :src="getAvatarPath(player.avatars)" 
                                alt="player-avatar" 
                                class="player-avatar"
                                @error="useDefaultAvatar"
                            />
                            <div :class="['player-role', getRoleClass(player.ruolo)]">{{ player.ruolo }}</div>
                            <div class="player-info">
                                <p class="player-name">{{ player.nome }}</p>
                                <p class="player-team">{{ player.team }}</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { store } from '../../store.js'
import BudgetSection from './budgetSection.vue';

export default {
    components: {
        budgetSection: BudgetSection
    },
    data() {
        return {
            searchQuery: '', 
            filteredPlayers: [],
            highlightedIndex: -1, // Indice del giocatore attualmente evidenziato
            budgets: [
                { value: 300, selected: true }, // Selezionato di default
                { value: 500, selected: false },
                { value: 1000, selected: false }
            ]
        };
    },
    methods: {
        filterPlayers() {
            if (store.players.length === 0) {
                console.warn("Nessun giocatore disponibile per la ricerca.");
                return;
            }
            // Filtra i giocatori in base al testo inserito
            clearTimeout(this.debounceTimeout);
            this.debounceTimeout = setTimeout(() => {
                this.filteredPlayers = store.players.filter(player =>
                    player.nome.toLowerCase().includes(this.searchQuery.toLowerCase())
                );
                this.highlightedIndex = -1; // Reset the highlighted index when results change
            }, 300); // Debounce di 300ms
        },
        navigateSuggestions(direction) {
            if (this.filteredPlayers.length === 0) return;
            const newIndex = this.highlightedIndex + direction;

            // Impedisce di superare i limiti dell'array
            if (newIndex >= this.filteredPlayers.length) {
                this.highlightedIndex = 0; // Ricomincia dall'inizio
            } else if (newIndex < 0) {
                this.highlightedIndex = this.filteredPlayers.length - 1; // Vai alla fine
            } else {
                this.highlightedIndex = newIndex;
            }

            // Assicura che l'elemento evidenziato sia visibile
            this.scrollToHighlighted();
        },
        scrollToHighlighted() {
            this.$nextTick(() => {
                const list = this.$refs.suggestionsList;
                const items = this.$refs.playerItems;

                if (items && items[this.highlightedIndex]) {
                    const highlightedItem = items[this.highlightedIndex];
                    const listHeight = list.clientHeight;
                    const itemTop = highlightedItem.offsetTop;
                    const itemBottom = itemTop + highlightedItem.clientHeight;

                    // Verifica se l'elemento evidenziato è visibile
                    if (itemBottom > list.scrollTop + listHeight) {
                        // Scorri in basso
                        list.scrollTop = itemBottom - listHeight;
                    } else if (itemTop < list.scrollTop) {
                        // Scorri in alto
                        list.scrollTop = itemTop;
                    }
                }
            });
        },
        selectHighlightedPlayer() {
            if (this.highlightedIndex >= 0 && this.highlightedIndex < this.filteredPlayers.length) {
                this.selectPlayer(this.filteredPlayers[this.highlightedIndex]);
            }
        },
        selectPlayer(player) {
            // Salva il giocatore selezionato nello store
            store.selectedPlayer = player;

            // Cerca giocatori simili
            store.similarPlayers = ['sp1', 'sp2', 'sp3', 'sp4', 'sp5'].map(key => {
                const similarPlayerName = player[key];
                const similarPlayer = store.players.find(p => p.nome === similarPlayerName);
                return similarPlayer ? { nome: similarPlayer.nome, squadra: similarPlayer.team } : null;
            }).filter(Boolean); // Filtra eventuali null
            
            this.filteredPlayers = [];
            this.searchQuery = '';
            this.highlightedIndex = -1; // Reset the highlighted index
        },
        getAvatarPath(avatar) {
            return `/avatar/${avatar}`;
        },
        useDefaultAvatar(event) {
            event.target.src = '/avatar/avatar.png'; // Default avatar
        },
        getRoleClass(role) {
            switch (role) {
                case 'P':
                    return 'role-goalkeeper';
                case 'D':
                    return 'role-defender';
                case 'C':
                    return 'role-midfielder';
                case 'A':
                    return 'role-forward';
                default:
                    return '';
            }
        }
    }
}
</script>

<style scoped>
.suggested-players {
    list-style-type: none;
    position: absolute;
    width: calc(100% - 46px);
    background-color: #e9ecef;
    border: 1px solid #ced4da;
    border-top: none;
    border-radius: 10px;
    z-index: 10;
    max-height: 200px; /* Altezza massima della lista */
    overflow-y: auto; /* Abilita lo scroll verticale */
    top: 110%;
    left: 0;
}

.suggested-players li {
    display: flex;
    align-items: center;
    padding: 10px;
    cursor: pointer;
    border-bottom: 1px solid #ced4da;
}

.suggested-players li:hover,
.suggested-players li.highlighted {
    background-color: #f0f0f0;
}

.player-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 15px;
}

.player-role {
    width: 30px;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    color: white;
    font-weight: bold;
    margin-right: 15px;
    font-size: 16px;
}

.role-goalkeeper {
    background-color: orange;
}

.role-defender {
    background-color: green;
}

.role-midfielder {
    background-color: blue;
}

.role-forward {
    background-color: red;
}

.player-info {
    display: flex;
    flex-direction: column;
}

.player-name {
    font-size: 16px;
    font-weight: bold;
}

.player-team {
    font-size: 14px;
    color: #555;
}

.input-group {
    display: flex;
    width: 70%;
    margin: 0 auto;
    position: relative;
}

.form-control {
    flex: 1 1 auto;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ced4da;
    border-radius: 10px 0 0 10px;
    background-color: #e9ecef;
    position: relative;
}

.btn {
    display: inline-block;
    padding: 10px 16px;
    font-size: 16px;
    text-align: center;
    cursor: pointer;
    border-radius: 0 10px 10px 0;
}
</style>
