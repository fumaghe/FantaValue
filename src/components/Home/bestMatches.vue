<template>
    <div class="container">
        <div class="row my-10">
            <div class="col-100 p-10">
                <div class="fw-800 fs-xxl my-10">Abbinamenti Migliori</div>
            </div>

            <!-- Terzetto 1 -->
            <div class="col-33 d-flex justify-content-center flex-direction-column p-10">
                <div class="d-flex align-items-center justify-content-between my-10">
                    <span class="fw-600 fs-s">COSTO</span>
                    <div class="d-flex align-items-center">
                        <img src="../../assets/grafiche/costo.png" alt="" class="icon-table mx-2" />
                        <span class="text-orange fw-600 fs-m">{{ animatedPriceTerzetto1 }}</span>
                    </div>
                </div>
                <div class="d-flex align-items-center justify-content-between my-10">
                    <span class="fw-600 fs-s">AFFINITÀ</span>
                    <div class="d-flex align-items-center">
                        <img
                            src="../../assets/grafiche/affinita.png"
                            alt=""
                            class="icon-table mx-2" />
                        <span class="text-orange fw-600 fs-m">{{ animatedAffinitaTerzetto1 }}</span>
                    </div>
                </div>
            </div>
            <div v-for="(player, index) in validPlayersT1" :key="index" class="col-33 d-flex my-10">
                <img :src="`/img_giocatori/${player.img}`" alt="" class="matching-img mx-2" />
                <div class="fw-600 fs-m vertical-text">{{ player.nome }}</div>
            </div>

            <!-- Terzetto 2 -->
            <div class="col-33 d-flex justify-content-center flex-direction-column p-10">
                <div class="d-flex align-items-center justify-content-between my-10">
                    <span class="fw-600 fs-s">COSTO</span>
                    <div class="d-flex align-items-center">
                        <img src="../../assets/grafiche/costo.png" alt="" class="icon-table mx-2" />
                        <span class="text-orange fw-600 fs-m">{{ animatedPriceTerzetto2 }}</span>
                    </div>
                </div>
                <div class="d-flex align-items-center justify-content-between my-10">
                    <span class="fw-600 fs-s">AFFINITÀ</span>
                    <div class="d-flex align-items-center">
                        <img
                            src="../../assets/grafiche/affinita.png"
                            alt=""
                            class="icon-table mx-2" />
                        <span class="text-orange fw-600 fs-m">{{ animatedAffinitaTerzetto2 }}</span>
                    </div>
                </div>
            </div>
            <div v-for="(player, index) in validPlayersT2" :key="index" class="col-33 d-flex my-10">
                <img :src="`/img_giocatori/${player.img}`" alt="" class="matching-img mx-2" />
                <div class="fw-600 fs-m vertical-text">{{ player.nome }}</div>
            </div>
        </div>
    </div>
</template>

<script>
import { animationMixin } from "../../animationMixin" // Import del mixin
import { store } from "../../store.js"

export default {
    props: {
        selectedPlayer: {
            type: Object,
            required: true,
            default: () => ({}),
        },
        players: {
            type: Array,
            required: true,
            default: () => [],
        },
        hasBorderTop: {
            type: Boolean,
            default: true, // Default true, quindi la classe border-top sarà applicata di default
        },
    },
    data() {
        return {
            animatedPriceTerzetto1: 0,
            animatedPriceTerzetto2: 0,
            animatedAffinitaTerzetto1: 0,
            animatedAffinitaTerzetto2: 0,
        }
    },
    mixins: [animationMixin], // Inclusione del mixin
    computed: {
        validPlayersT1() {
            return this.getPlayers(["player1t1", "player2t1"])
        },
        validPlayersT2() {
            return this.getPlayers(["player1t2", "player2t2"])
        },
        priceTerzetto1() {
            return store.getDynamicValue(this.selectedPlayer, "prezzo_terzetto1_")
        },
        priceTerzetto2() {
            return store.getDynamicValue(this.selectedPlayer, "prezzo_terzetto2_")
        },
    },
    watch: {
        selectedPlayer: {
            immediate: true,
            handler(newPlayer) {
                if (newPlayer) {
                    // Anima i valori del terzetto 1
                    this.animateIntegerValue("animatedPriceTerzetto1", this.priceTerzetto1, 2000)
                    this.animateIntegerValue(
                        "animatedAffinitaTerzetto1",
                        newPlayer.affinita_terzetto1,
                        2000,
                        2
                    )

                    // Anima i valori del terzetto 2
                    this.animateIntegerValue("animatedPriceTerzetto2", this.priceTerzetto2, 2000)
                    this.animateIntegerValue(
                        "animatedAffinitaTerzetto2",
                        newPlayer.affinita_terzetto2,
                        2000,
                        2
                    )
                }
            },
        },
    },
    methods: {
        getPlayers(keys) {
            return keys
                .map((key) => {
                    const playerName = this.selectedPlayer[key]
                    const player = this.players.find((p) => p.nome === playerName)
                    if (player) {
                        return {
                            nome: player.nome,
                            img: player.img,
                        }
                    }
                    return null
                })
                .filter(Boolean)
        },
    },
}
</script>

<style scoped>
.icon-table {
    width: 30px;
    height: auto;
}

.border-top {
    border-top: 2px solid black;
    width: 100%;
}

.matching-img {
    max-height: 200px;
    width: 70%;
    object-fit: contain;
}

.vertical-text {
    margin-left: 10px;
    writing-mode: vertical-rl;
    transform: rotate(180deg);
}
</style>
