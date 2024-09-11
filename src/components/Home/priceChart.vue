<template>
  <div class="col-100 p-10">
    <div class="fw-600 fs-xxl my-10 text-white">Andamento Prezzo</div>
    <canvas id="priceAndPMAChart" width="400" height="150"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import { store } from '../../store.js';

// Funzione debounce
function debounce(func, wait) {
  let timeout;
  return function (...args) {
    const context = this;
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(context, args), wait);
  };
}

Chart.register(...registerables, ChartDataLabels);  // Registra il plugin

export default {
  data() {
    return {
      store,
      chartInstance: null,
    };
  },
  mounted() {
    this.loadChartDataDebounced();
  },
  watch: {
    'store.selectedPlayer': debounce(function (newPlayer) {
      if (this.hasPlayerData(newPlayer)) {
        this.renderChart();
      }
    }, 1000),  // Debounce di 1000ms (1 secondo)
    'store.budgetValue': function (newBudget) {
      if (this.hasPlayerData(this.store.selectedPlayer)) {
        this.renderChart();
      }
    },
  },
  methods: {
    loadChartDataDebounced() {
      if (this.store.selectedPlayer && this.hasPlayerData(this.store.selectedPlayer)) {
        this.renderChart();
      } else {
        console.error('Dati del giocatore mancanti o incompleti');
      }
    },
    hasPlayerData(player) {
      const dateKeys = Object.keys(player).filter(key => key.includes(`PREZZO_`) && key.includes(`_${this.store.budgetValue}`));
      return dateKeys.length > 0;
    },
    getAvailableDates(player) {
      const dateRegex = new RegExp(`PREZZO_(\\d{2}_\\d{2})_${this.store.budgetValue}`);
      const dates = Object.keys(player)
        .map(key => {
          const match = key.match(dateRegex);
          return match ? match[1] : null;
        })
        .filter(date => date !== null);
      return dates;
    },
    renderChart() {
      if (this.chartInstance) {
        this.chartInstance.destroy();
      }

      const ctx = document.getElementById('priceAndPMAChart').getContext('2d');
      const player = this.store.selectedPlayer;
      const dates = this.getAvailableDates(player);

      if (dates.length === 0) {
        console.error('Non ci sono date disponibili per il giocatore selezionato.');
        return;
      }

      this.store.pmaData = dates.map(date => player[`PMA_${date}_${this.store.budgetValue}`]);
      this.store.priceData = dates.map(date => player[`PREZZO_${date}_${this.store.budgetValue}`]);

      const allValues = [...this.store.pmaData, ...this.store.priceData];
      const minValue = Math.min(...allValues);
      const maxValue = Math.max(...allValues);

      const yMin = Math.max(0, minValue - minValue * 0.2);
      const yMax = maxValue + maxValue * 0.2;

      this.chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
          labels: dates.map(date => date.replace('_', '/')),
          datasets: [
            {
              label: 'PMA',
              data: this.store.pmaData,
              borderColor: '#FE4C10',
              backgroundColor: 'rgba(254, 76, 16, 0.4)',
              borderWidth: 4,
              pointRadius: 6,
              pointBackgroundColor: '#FE4C10',
              fill: false
            },
            {
              label: 'Prezzo',
              data: this.store.priceData,
              borderColor: '#4C88FE',
              backgroundColor: 'rgba(76, 136, 254, 0.4)',
              borderWidth: 4,
              pointRadius: 6,
              pointBackgroundColor: '#4C88FE',
              fill: false
            }
          ]
        },
        options: {
          layout: {
            padding: {
              left: 10,
              right: 10
            }
          },
          scales: {
            x: {
              type: 'category',
              offset: true,
              title: {
                display: true,
                text: 'Data',
                color: '#fff'
              },
              ticks: {
                color: '#fff',
                align: 'center'
              }
            },
            y: {
              beginAtZero: false,
              min: yMin,
              max: yMax,
              ticks: {
                color: '#fff'
              }
            }
          },
          elements: {
            line: {
              tension: 0.4
            }
          },
          plugins: {
            datalabels: {
              display: true,
              color: '#fff',
              font: {
                weight: 'bold',
                size: 14
              },
              formatter: function (value) {
                return value;
              },
              align: function (context) {
                const datasetLabel = context.dataset.label;
                const pmaValue = context.chart.data.datasets[0].data[context.dataIndex];
                const prezzoValue = context.chart.data.datasets[1].data[context.dataIndex];

                if (pmaValue === prezzoValue) {
                  return 'top';
                }

                const diffPercentage = Math.abs(pmaValue - prezzoValue) / Math.max(pmaValue, prezzoValue);
                if (diffPercentage <= 0.15) {
                  if (datasetLabel === 'PMA' && pmaValue > prezzoValue) {
                    return 'top';
                  } else if (datasetLabel === 'Prezzo' && prezzoValue > pmaValue) {
                    return 'top';
                  } else if (datasetLabel === 'PMA' && pmaValue < prezzoValue) {
                    return 'bottom';
                  } else if (datasetLabel === 'Prezzo' && prezzoValue < pmaValue) {
                    return 'bottom';
                  }
                }

                return 'top';
              },
              offset: 5
            }
          }
        }
      });
    }
  },
  beforeDestroy() {
    if (this.chartInstance) {
      this.chartInstance.destroy();
    }
  }
};
</script>
