<template>
    <div class="container">
        <div class="row bg-black rounded-10">
            <div
                class="col-100 d-flex justify-content-center align-items-center my-10 playerName-mobile">
                <div v-if="player.diagnosi" class="container-relative" @click="showDiagnosiTooltip">
                    <i class="fa-solid fa-truck-medical fs-m text-orange"></i>
                    <div
                        v-if="showTooltip"
                        :class="[
                            'message-bubble text-white',
                            { 'message-bubble-active': showTooltip },
                        ]">
                        {{ player.diagnosi }}
                    </div>
                </div>
                <h1 class="text-white fs-xxl">{{ player?.nome }}</h1>
            </div>
            <div class="col-50 col-md-25 my-10 text-center order-1">
                <div class="text-white fs-l fw-600 my-10">Media Voto</div>
                <span class="text-orange fs-xl fw-600">{{ animatedMv }}</span>
            </div>
            <div class="col-50 col-md-25 my-10 text-center order-3">
                <div class="text-white fs-l fw-600 my-10">FantaMedia</div>
                <span class="text-orange fs-xl fw-600">{{ animatedFmv }}</span>
            </div>
            <div class="col-100 col-md-50 text-center my-10 border-top order-2">
                <div class="text-white fs-l fw-600 my-10">Similar Players</div>
                <ul class="list-unstyled d-flex flex-wrap justify-content-center my-10">
                    <li
                        v-for="similarPlayer in similarPlayers"
                        :key="similarPlayer.nome"
                        @click="selectPlayer(similarPlayer)"
                        class="mx-2">
                        <img
                            v-if="similarPlayer.squadra"
                            :src="`/teams_similar_players/${similarPlayer.squadra}.png`"
                            alt=""
                            class="similar-player-img" />
                        <div v-if="similarPlayer.nome" class="text-white fs-xs">
                            {{ similarPlayer.nome }}
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { store } from "../../store.js"
import { animationMixin } from "../../animationMixin.js"

export default {
    props: {
        player: {
            type: Object,
            required: true,
        },
    },
    mixins: [animationMixin],
    data() {
        return {
            animatedMv: 0,
            animatedFmv: 0,
            similarPlayers: [],
            showTooltip: false,
        }
    },
    watch: {
        player: {
            immediate: true,
            handler(newPlayer) {
                if (newPlayer) {
                    this.setSimilarPlayers(newPlayer)
                    this.animateFloatValue("animatedMv", newPlayer.mv) // Animazione per Media Voto
                    this.animateFloatValue("animatedFmv", newPlayer.fmv) // Animazione per FantaMedia
                }
            },
        },
    },
    methods: {
        selectPlayer(similarPlayer) {
            store.selectedPlayer = store.players.find((p) => p.nome === similarPlayer.nome)
            this.setSimilarPlayers(store.selectedPlayer)
        },
        setSimilarPlayers(player) {
            this.similarPlayers = ["sp1", "sp2", "sp3", "sp4", "sp5"]
                .map((key) => {
                    const similarPlayerName = player[key]
                    const similarPlayer = store.players.find((p) => p.nome === similarPlayerName)
                    return similarPlayer
                        ? { nome: similarPlayer.nome, squadra: similarPlayer.team }
                        : null
                })
                .filter(Boolean)
        },
        showDiagnosiTooltip() {
            this.showTooltip = !this.showTooltip
        },
    },
}
</script>

<style scoped>
.similar-player-img {
    width: 100px;
    height: auto;
}

li div {
    margin-bottom: 10px;
}

li {
    transition: transform 0.3s ease, background-color 0.3s ease;
}

li:hover {
    background-color: #202f3b;
    border-radius: 10px;
    cursor: pointer;
    transform: scale(1.1);
}

.fa-truck-medical {
    margin-right: 10px;
}

.container-relative {
    position: relative;
    cursor: pointer;
}

.message-bubble {
    position: absolute;
    left: 40%;
    bottom: calc(100% + 13px);
    transform: translateX(-50%);
    background-color: #15212a;
    padding: 8px;
    border-radius: 10px;
    font-size: 14px;
    margin-top: 6.5px;
    z-index: 9999;
    max-width: 500px;
    text-align: center;
    border: 0;
    opacity: 0;
    transition: opacity 0.6s ease;
}

/* Punta del fumetto */
.message-bubble::before {
    content: "";
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    border-left: 10px solid transparent;
    border-right: 10px solid transparent;
    border-top: 10px solid #15212a;
}

.message-bubble-active {
    opacity: 1;
}

@media (min-width: 768px) {
    .similar-player-img {
        width: 100px;
        height: auto;
    }

    .playerName-mobile {
        display: none;
    }

    .border-top {
        border-top: 0;
    }

    .col-md-50 {
        width: 60%;
    }

    .col-md-25 {
        width: 20%;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .order-1 {
        order: 1;
    }

    .order-2 {
        order: 2;
    }

    .order-3 {
        order: 3;
    }
}

@media (min-width: 991px) {
    .similar-player-img {
        width: 115px;
        height: auto;
    }
}
</style>
