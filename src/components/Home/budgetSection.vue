<template lang="">
    <div class="col-100 my-10">
        <h1 class="text-center my-10 fs-l fw-800">Scegli il tuo budget per l'asta</h1>
        <div class="btn-group d-flex justify-content-center">
            <button
                v-for="budget in budgets"
                :key="budget.value"
                :class="['btn-budget', budget.selected ? 'bg-orange text-white' : 'text-orange']"
                @click="selectBudget(budget)"
            >
                {{ budget.value }}
            </button>
        </div>
    </div>
</template>

<script>
import { store } from '../../store.js'
 
export default {
    data() {
        return {
            budgets: [
                { value: 300, selected: false },
                { value: 500, selected: true },
                { value: 1000, selected: false }
            ]
        }
    },
    methods: {
        selectBudget(selectedBudget) {
            // Imposta tutti i budget come non selezionati
            this.budgets.forEach(budget => {
                budget.selected = false;
            });

            // Imposta il budget cliccato come selezionato
            selectedBudget.selected = true;

            store.budgetValue = selectedBudget.value
        }
    }
}
</script>

<style scoped>
    .btn-group {
        width: 70%;
        margin: 0 auto;
    }

    .btn-budget {
        display: inline-block;
        padding: 10px 16px;
        font-size: 16px;
        text-align: center;
        cursor: pointer;
        border: 2px solid #FE4C10;
        border-radius: 10px;
        background-color: rgb(255, 255, 255);
        margin: 0px 10px;
    }
</style>