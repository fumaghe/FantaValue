<template>
    <div class="row">
        <div class="col-50 col-md-33">
            <img
                v-if="player && player.img"
                :src="`/img_giocatori/${player.img}`"
                alt="immagine giocatore"
                class="img-player" />
        </div>
        <div class="col-50 col-md-66 d-flex flex-wrap align-items-center">
            <div class="col-100 d-flex align-items-center justify-content-center h-70">
                <ul class="list-unstyled">
                    <li
                        v-for="(item, index) in playerInfo"
                        :key="index"
                        class="text-center my-10"
                        :class="item.class">
                        <div class="fs-l fw-600">{{ item.label }}</div>
                        <span class="text-orange fw-600 contrail-one-font">{{ item.value }}</span>
                    </li>
                </ul>
            </div>
            <div
                class="d-flex justify-content-end align-items-end playerName-desktop h-30 position-relative">
                <div v-if="player.diagnosi" class="container-relative" @click="showDiagnosiTooltip">
                    <i class="fa-solid fa-truck-medical fs-xl text-orange"></i>
                    <div
                        v-if="showTooltip"
                        :class="[
                            'message-bubble text-white',
                            { 'message-bubble-active': showTooltip },
                        ]">
                        {{ player.diagnosi }}
                    </div>
                </div>
                <h1 :class="player?.nome && player.nome.length > 5 ? 'fs-small' : 'fs-large'">
                    {{ player?.nome }}
                </h1>
            </div>
        </div>
    </div>
</template>

<script>
import { store } from "../../store"
import { animationMixin } from "../../animationMixin"

export default {
    props: {
        player: {
            type: Object,
            default: () => ({}),
        },
    },
    mixins: [animationMixin],
    data() {
        return {
            animatedPma: 0,
            animatedPrice: 0,
            animatedTitolarita: 0,
            showTooltip: false,
        }
    },
    computed: {
        pmaValue() {
            return this.player ? this.player[`pma${store.budgetValue}`] : 0
        },
        priceValue() {
            return this.player ? this.player[`prezzo${store.budgetValue}`] : 0
        },
        titolaritaValue() {
            return this.player ? this.player["titolarita_24_25"] : 0
        },
        playerInfo() {
            return [
                {
                    label: "PMA",
                    value: this.animatedPma,
                    class: "pma",
                },
                {
                    label: "PREZZO",
                    value: this.animatedPrice,
                    class: "price",
                },
                {
                    label: "TIT.",
                    value: this.animatedTitolarita + "%",
                    class: "titolarita",
                },
                {
                    label: "RUOLO",
                    value: this.player?.ruolo || "N/A",
                    class: "role",
                },
                {
                    label: "SQUADRA",
                    value: this.player?.team || "N/A",
                    class: "squad",
                },
            ]
        },
    },
    watch: {
        pmaValue(newValue) {
            this.animateIntegerValue("animatedPma", newValue, 1500) // Animazione adattiva per PMA
        },
        priceValue(newValue) {
            this.animateIntegerValue("animatedPrice", newValue, 1500) // Animazione adattiva per prezzo
        },
        titolaritaValue(newValue) {
            this.animateIntegerValue("animatedTitolarita", newValue, 1500) // Animazione adattiva per titolarità
        },
    },
    methods: {
        showDiagnosiTooltip() {
            this.showTooltip = !this.showTooltip
        },
    },
    mounted() {
        this.animateIntegerValue("animatedPma", this.pmaValue, 1500) // Inizializza l'animazione per PMA
        this.animateIntegerValue("animatedPrice", this.priceValue, 1500) // Inizializza l'animazione per prezzo
        this.animateIntegerValue("animatedTitolarita", this.titolaritaValue, 1500)
    },
}
</script>

<style scoped>
.contrail-one-font {
    font-size: var(--font-size-xl);
}

.h-30 {
    height: 30%;
}

.h-70 {
    height: 70%;
}

.img-player {
    width: 100%;
    height: auto;
}

.price,
.role,
.squad,
.pma,
.titolarita {
    background-position: center;
    background-size: 80% auto;
    background-repeat: no-repeat;
}

.titolarita {
    background-image: url(../../assets/grafiche/magliatitolarita.png);
}

.price {
    background-image: url(../../assets/grafiche/price.png);
}

.role {
    background-image: url(../../assets/grafiche/role.png);
}

.squad {
    background-image: url(../../assets/grafiche/team.png);
}

.pma {
    background-image: url(../../assets/grafiche/pma.png);
}

.fs-small {
    font-size: 60px;
}

.fs-large {
    font-size: 150px;
}

.playerName-desktop h1 {
    color: #d9d9d9;
    display: none;
}

.playerName-desktop {
    width: 0%;
}

.fa-truck-medical {
    margin-right: 10px;
    padding-bottom: 20px;
}

.container-relative {
    position: relative;
    cursor: pointer;
    display: none;
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
    .col-md-66 {
        width: calc(100% / 3 * 2);
    }

    .col-md-33 {
        width: calc(100% / 3);
    }

    .list-unstyled {
        width: 100%;
        height: 100%;
        display: flex;
    }

    li {
        width: 20%;
        height: 100%;
        display: flex;
        justify-content: center;
        flex-direction: column;
    }

    .playerName-desktop {
        width: 100%;
    }

    .playerName-desktop h1 {
        display: block;
    }

    .fantavalue {
        display: block;
    }

    .container-relative {
        display: block;
    }

    .contrail-one-font {
        font-size: 60px;
    }
}

@media (min-width: 991px) {
    .fs-small {
        font-size: 80px;
    }
}
</style>
