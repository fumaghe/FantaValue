<template>
    <!-- Layout usato in playerCard.vue -->
    <div v-if="isInPlayerCard">
        <div class="row">
            <div class="p-10 border-right table-container-card">
                <table>
                    <thead>
                        <tr>
                            <th></th>
                            <th class="text-orange">MV</th>
                            <th class="text-orange">FM</th>
                            <th class="text-orange">
                                <i class="fa-solid fa-futbol text-orange"></i>
                            </th>
                            <th class="text-orange">
                                <i class="fa-solid fa-font text-orange"></i>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="season in seasons" :key="season.year">
                            <td class="text-orange fw-600">{{ season.year }}</td>
                            <td class="fw-600">{{ season.media_voto }}</td>
                            <td class="fw-600">{{ season.fanta_media }}</td>
                            <td class="fw-600">{{ season.gol }}</td>
                            <td class="fw-600">{{ season.assist }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div
                class="col-33 col-md-50 percentage-container p-10 d-flex justify-content-center align-items-center flex-direction-column">
                <div class="fw-800 percentage">{{ animatedPercentageTitolare }}%</div>
                <div class="fw-600 fs-s">Partite Titolari 23/24</div>
            </div>
        </div>
    </div>

    <!-- Layout usato nella Home -->
    <div v-else>
        <div class="container bg-black rounded-10">
            <div class="row">
                <div class="col-100 p-10">
                    <div class="fw-600 fs-xxl my-10 text-white">Ultime Stagioni</div>
                </div>
                <div class="p-10 border-right table-container">
                    <table>
                        <thead>
                            <tr>
                                <th></th>
                                <th class="text-orange">MV</th>
                                <th class="text-orange">FM</th>
                                <th class="text-orange">
                                    <i class="fa-solid fa-futbol text-orange"></i>
                                </th>
                                <th class="text-orange">
                                    <i class="fa-solid fa-font text-orange"></i>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="season in seasons" :key="season.year">
                                <td class="text-orange">{{ season.year }}</td>
                                <td class="text-white">{{ season.media_voto }}</td>
                                <td class="text-white">{{ season.fanta_media }}</td>
                                <td class="text-white">{{ season.gol }}</td>
                                <td class="text-white">{{ season.assist }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div
                    class="col-33 col-md-50 p-10 d-flex justify-content-center align-items-center flex-direction-column">
                    <div class="text-white fw-800 percentage">
                        {{ animatedPercentageTitolare }}%
                    </div>
                    <div class="text-white fw-600 fs-s">Partite Titolari</div>
                </div>
                <priceChart
                    :labels="['11/08', '18/08', '22/08']"
                    :data="priceData"
                    :pmaData="pmaData" />
            </div>
        </div>
    </div>
</template>

<script>
import priceChart from "./priceChart.vue"
import { animationMixin } from "../../animationMixin" // Import del mixin per l'animazione della percentuale titolari
import { store } from "../../store.js" // Import dello store

export default {
    data() {
        return {
            store,
            animatedPercentageTitolare: 0, // Variabile animata
        }
    },
    components: {
        priceChart,
    },
    mixins: [animationMixin], // Inclusione del mixin
    props: {
        selectedPlayer: {
            type: Object,
            required: true,
        },
        isInPlayerCard: {
            type: Boolean,
            default: false,
        },
    },
    computed: {
        seasons() {
            return [
                {
                    year: "22/23",
                    media_voto: this.selectedPlayer?.media_voto_22_23,
                    fanta_media: this.selectedPlayer?.fanta_media_22_23,
                    gol: this.selectedPlayer?.gol_22_23,
                    assist: this.selectedPlayer?.assist_22_23,
                },
                {
                    year: "23/24",
                    media_voto: this.selectedPlayer?.media_voto_23_24,
                    fanta_media: this.selectedPlayer?.fanta_media_23_24,
                    gol: this.selectedPlayer?.gol_23_24,
                    assist: this.selectedPlayer?.assist_23_24,
                },
                {
                    year: "24/25",
                    media_voto: this.selectedPlayer?.media_voto_24_25,
                    fanta_media: this.selectedPlayer?.fanta_media_24_25,
                    gol: this.selectedPlayer?.gol_24_25,
                    assist: this.selectedPlayer?.assist_24_25,
                },
            ]
        },
        priceData() {
            return [
                this.selectedPlayer?.[`PREZZO_11_08_${store.budgetValue}`],
                this.selectedPlayer?.[`PREZZO_18_08_${store.budgetValue}`],
                this.selectedPlayer?.[`PREZZO_22_08_${store.budgetValue}`],
            ]
        },
        pmaData() {
            return [
                this.selectedPlayer?.[`PMA_11_08_${store.budgetValue}`],
                this.selectedPlayer?.[`PMA_18_08_${store.budgetValue}`],
                this.selectedPlayer?.[`PMA_22_08_${store.budgetValue}`],
            ]
        },
    },
    watch: {
        selectedPlayer: {
            immediate: true,
            handler(newPlayer) {
                if (newPlayer) {
                    // Anima la percentuale titolari
                    this.animateFloatValue(
                        "animatedPercentageTitolare",
                        newPlayer.percentuale_titolare,
                        2000,
                        2
                    )
                }
            },
        },
    },
}
</script>

<style scoped>
.table-container {
    overflow-x: hidden; /* Nascondi la barra di scorrimento per impostazione predefinita */
    width: calc(100% / 3 * 2);
    transition: overflow 0.5s ease; /* Transizione per rendere fluida l'animazione */
}

.table-container-card {
    overflow-x: hidden; /* Nascondi la barra di scorrimento per impostazione predefinita */
    width: calc(100% / 3 * 2);
    transition: overflow 0.5s ease; /* Transizione per rendere fluida l'animazione */
}

.table-container:hover {
    overflow-x: auto; /* Mostra la barra di scorrimento al passaggio del mouse */
}
table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    padding: 10px;
    text-align: center;
}

.percentage {
    font-size: 40px;
}

@media (min-width: 768px) {
    .table-container {
        width: 50%;
    }

    .table-container-card {
        width: 100%;
        border: 0;
    }

    .col-md-50 {
        width: 50%;
    }

    .percentage {
        font-size: 90px;
    }

    .percentage-container {
        width: 100%;
        margin-top: 50px;
    }
}
</style>
