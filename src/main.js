import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'; // Importa il router

createApp(App).use(router).mount('#app'); // Usa il router nell'app
