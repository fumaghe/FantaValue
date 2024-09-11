<template>
  <div class="container">
    <div class="row">
      <div class="col-100 my-10 p-10">
        <h3 class="fw-800 fs-xxl">Fanta<span class="text-orange">Value</span> Overall</h3>
      </div>
      <div class="col-33 d-flex align-items-center justify-content-center position-relative p-10">
        <img src="../../assets/grafiche/fish_overall.png" alt="">
        <div 
          class="fw-600 fantavalue-overall text-white" 
          :style="computedFontStyle"
        >
          {{ selectedPlayer?.fantavalue }}
        </div>
      </div>
      <div class="col-66 p-10">
        <ul class="list-unstyled">
          <li v-for="stat in stats" :key="stat.name">
            <div class="progress-bar-container">
              <span class="stat-name fw-600 fs-s">{{ stat.name }}</span>
              <div class="progress-bar">
                <div class="progress-fill" :style="{ width: stat.value + '%' }"></div>
              </div>
              <span class="fw-600 fs-s text-orange">{{ stat.value }}</span>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    selectedPlayer: {
      type: Object,
      required: true,
      default: () => ({
        fantavalue: 0,
        tiri_fv: 0,
        passaggi_fv: 0,
        difesa_fv: 0,
        possesso_fv: 0,
        azioni_fv: 0
      }),
    },
    fontSize: {
      type: Number,
      default: 27 // Valore di base del font-size
    },
    isResponsiveFont: {
      type: Boolean,
      default: true // Di default il font sarà responsivo
    }
  },
  computed: {
    stats() {
      return [
        { name: 'Tiri', value: Number(this.selectedPlayer?.tiri_fv) || 0 },
        { name: 'Passaggi', value: Number(this.selectedPlayer?.passaggi_fv) || 0 },
        { name: 'Difesa', value: Number(this.selectedPlayer?.difesa_fv) || 0 },
        { name: 'Possesso', value: Number(this.selectedPlayer?.possesso_fv) || 0 },
        { name: 'Azioni', value: Number(this.selectedPlayer?.azioni_fv) || 0 },
      ];
    },
    computedFontStyle() {
      if (this.isResponsiveFont) {
        // Usa variabili CSS per il font-size responsivo
        return { '--base-font-size': this.fontSize + 'px' };
      } else {
        // Usa il font-size fisso
        return { fontSize: this.fontSize + 'px' };
      }
    }
  }
};
</script>

<style scoped>
    .fantavalue-overall {
      position: absolute;
      font-size: var(--calculated-font-size);
    }

    .list-unstyled {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
    }

    .progress-bar-container {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
        width: 100%;
    }

    .stat-name {
        width: 25%;
        text-align: center;
    }

    .progress-bar {
        width: 55%;
        height: 20px;
        background-color: #15212A;
        border-radius: 10px;
        overflow: hidden;
        margin: 0px 10px;
    }

    .progress-fill {
        height: 100%;
        background-color: #FE4C10;
        border-radius: 10px;
    }

    img {
      width: 100%;
      height: auto;
    }

    

    @media (max-width: 767px) {
      .fantavalue-overall {
        --calculated-font-size: calc(var(--base-font-size) * 1);
      }
    }

    @media (min-width: 768px) {
      .fantavalue-overall {
        --calculated-font-size: calc(var(--base-font-size) * 1.5);
      }
    }

    @media (min-width: 991px) {
      .fantavalue-overall {
        --calculated-font-size: calc(var(--base-font-size) * 2);
      }

      img {
        width: 80%;
        height: auto;
      }
    }

    @media (min-width: 1200px) {
      .fantavalue-overall {
      --calculated-font-size: calc(var(--base-font-size) * 2.5);
    }
    }
</style>
