<script>
import homeHeader from "./components/homeHeader.vue"
import homeMain from "./components/Home/homeMain.vue"
import Papa from "papaparse"
import { store } from "./store"

export default {
    components: {
        homeHeader,
        homeMain,
    },
    name: "App",
    mounted() {
        this.loadCSV() // Chiama la funzione per caricare il CSV quando il componente viene montato
    },
    methods: {
        loadCSV() {
            fetch("/dataset.csv")
                .then((response) => response.text())
                .then((data) => {
                    // Usa PapaParse per convertire il CSV in array di oggetti
                    Papa.parse(data, {
                        header: true, // Se il CSV ha intestazioni
                        skipEmptyLines: true, // Salta le righe vuote nel CSV
                        complete: (results) => {
                            store.players = results.data.map((player) => {
                                return {
                                    nome: player["Nome"],
                                    ruolo: player["Ruolo"],
                                    team: player["Team"],
                                    pma: player["02_09_PMA_500"],
                                    quot: player["Quot."],
                                    mv: player["MV"],
                                    fmv: player["FMV"],
                                    presenze: player["Presenze"],
                                    fmv_exp: player["FMV Exp."],
                                    pt_tit: player["Pt. Tit."],
                                    minuti: player["Minuti"],
                                    gol: player["Gol"],
                                    assist: player["Assist"],
                                    ammonizioni: player["Ammonizioni"],
                                    espulsioni: player["Espulsioni"],
                                    rig_segnati: player["Rig. Segnati"],
                                    rig_sbagliati: player["Rig. Sbagliati"],
                                    gol_subiti: player["Gol Subiti"],
                                    rig_parati: player["Rig. Parati"],
                                    prezzo: player["02_09_PREZZO_500"],
                                    titolarita: player["Titolarità"],
                                    affidabilita: player["Affidabilità"],
                                    integrita: player["Integrità"],
                                    prezzo_percentuale: player["Prezzo%"],
                                    img: player["img"],
                                    fascia: player["Fascia"],
                                    fanta_media_22_23: player["Fanta Media 22-23"],
                                    media_voto_22_23: player["Media Voto 22-23"],
                                    gol_22_23: player["Gol 22-23"],
                                    assist_22_23: player["Assist 22-23"],
                                    fanta_media_23_24: player["Fanta Media 23-24"],
                                    media_voto_23_24: player["Media Voto 23-24"],
                                    gol_23_24: player["Gol 23-24"],
                                    assist_23_24: player["Assist 23-24"],
                                    percentuale_titolare: player["Percentuale Titolare"],
                                    fantavalue: player["FantaValue"],
                                    tiri_fv: player["Tiri_FV"],
                                    passaggi_fv: player["Passaggi_FV"],
                                    difesa_fv: player["Difesa_FV"],
                                    possesso_fv: player["Possesso_FV"],
                                    azioni_fv: player["Azioni_FV"],
                                    player1t1: player["Player1T1"],
                                    player2t1: player["Player2T1"],
                                    player1t2: player["Player1T2"],
                                    player2t2: player["Player2T2"],
                                    prezzo_terzetto1: player["PrezzoTerzetto1"],
                                    affinita_terzetto1: player["AffinitaTerzetto1"],
                                    prezzo_terzetto2: player["PrezzoTerzetto2"],
                                    affinita_terzetto2: player["AffinitaTerzetto2"],
                                    sp1: player["SP1"],
                                    sp2: player["SP2"],
                                    sp3: player["SP3"],
                                    sp4: player["SP4"],
                                    sp5: player["SP5"],
                                    avatars: player["avatars"],
                                    pma300: player["02_09_PMA_300"],
                                    pma500: player["02_09_PMA_500"],
                                    pma1000: player["02_09_PMA_1000"],
                                    prezzo300: player["02_09_PREZZO_300"],
                                    prezzo500: player["02_09_PREZZO_500"],
                                    prezzo1000: player["02_09_PREZZO_1000"],
                                    prezzo_terzetto1_300: player["PrezzoTerzetto1300"],
                                    prezzo_terzetto1_500: player["PrezzoTerzetto1500"],
                                    prezzo_terzetto1_1000: player["PrezzoTerzetto11000"],
                                    prezzo_terzetto2_300: player["PrezzoTerzetto2300"],
                                    prezzo_terzetto2_500: player["PrezzoTerzetto2500"],
                                    prezzo_terzetto2_1000: player["PrezzoTerzetto21000"],
                                    PMA_11_08_300: player["11_08_PMA_300"],
                                    PMA_11_08_500: player["11_08_PMA_500"],
                                    PMA_11_08_1000: player["11_08_PMA_1000"],
                                    PMA_18_08_300: player["18_08_PMA_300"],
                                    PMA_18_08_500: player["18_08_PMA_500"],
                                    PMA_18_08_1000: player["18_08_PMA_1000"],
                                    PMA_22_08_300: player["22_08_PMA_300"],
                                    PMA_22_08_500: player["22_08_PMA_500"],
                                    PMA_22_08_1000: player["22_08_PMA_1000"],
                                    PREZZO_11_08_300: player["11_08_PREZZO_300"],
                                    PREZZO_11_08_500: player["11_08_PREZZO_500"],
                                    PREZZO_11_08_1000: player["11_08_PREZZO_1000"],
                                    PREZZO_18_08_300: player["18_08_PREZZO_300"],
                                    PREZZO_18_08_500: player["18_08_PREZZO_500"],
                                    PREZZO_18_08_1000: player["18_08_PREZZO_1000"],
                                    PREZZO_22_08_300: player["22_08_PREZZO_300"],
                                    PREZZO_22_08_500: player["22_08_PREZZO_500"],
                                    PREZZO_22_08_1000: player["22_08_PREZZO_1000"],
                                    diagnosi: player["Diagnosi"],
                                    fanta_media_24_25: player["Fanta Media 24-25"],
                                    media_voto_24_25: player["Media Voto 24-25"],
                                    gol_24_25: player["Gol 24-25"],
                                    assist_24_25: player["Assist 24-25"],
                                    PMA_24_08_300: player["24_08_PMA_300"],
                                    PMA_24_08_500: player["24_08_PMA_500"],
                                    PMA_24_08_1000: player["24_08_PMA_1000"],
                                    PREZZO_24_08_300: player["24_08_PREZZO_300"],
                                    PREZZO_24_08_500: player["24_08_PREZZO_500"],
                                    PREZZO_24_08_1000: player["24_08_PREZZO_1000"],
                                    PMA_26_08_300: player["26_08_PMA_300"],
                                    PMA_26_08_500: player["26_08_PMA_500"],
                                    PMA_26_08_1000: player["26_08_PMA_1000"],
                                    PREZZO_26_08_300: player["26_08_PREZZO_300"],
                                    PREZZO_26_08_500: player["26_08_PREZZO_500"],
                                    PREZZO_26_08_1000: player["26_08_PREZZO_1000"],
                                    PMA_28_08_300: player["28_08_PMA_300"],
                                    PMA_28_08_500: player["28_08_PMA_500"],
                                    PMA_28_08_1000: player["28_08_PMA_1000"],
                                    PREZZO_28_08_300: player["28_08_PREZZO_300"],
                                    PREZZO_28_08_500: player["28_08_PREZZO_500"],
                                    PREZZO_28_08_1000: player["28_08_PREZZO_1000"],
                                    PMA_02_09_300: player["02_09_PMA_300"],
                                    PMA_02_09_500: player["02_09_PMA_500"],
                                    PMA_02_09_1000: player["02_09_PMA_1000"],
                                    PREZZO_02_09_300: player["02_09_PREZZO_300"],
                                    PREZZO_02_09_500: player["02_09_PREZZO_500"],
                                    PREZZO_02_09_1000: player["02_09_PREZZO_1000"],
                                    titolarita_24_25: player["Titolarita 24/25"],
                                    rigorista: player["Rigorista"],
                                    calciPiazzati: player["CalciPiazzati"],
                                }
                            })
                        },
                        error: (error) => {
                            console.error("Errore nel parsing del CSV:", error)
                        },
                    })
                })
        },
    },
}
</script>

<template>
    <homeHeader />
    <router-view />
</template>

<style scoped></style>
