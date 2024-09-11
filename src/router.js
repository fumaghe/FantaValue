import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home/homeMain.vue';
import Listone from './components/Listone/Listone.vue';
import Asta from './components/Asta/Asta.vue';
import MyTeams from './components/MyTeams/MyTeams.vue';
import Login from './components/Login/Login.vue';
import Register from './components/Login/Register.vue'; // Importa il componente Register

const routes = [
  { path: '/login', component: Login },
  { path: '/register', component: Register }, // Aggiungi la rotta di registrazione
  { path: '/', component: Home, meta: { requiresAuth: true } },
  { path: '/listone', component: Listone, meta: { requiresAuth: true } },
  { path: '/asta', component: Asta, meta: { requiresAuth: true } },
  { path: '/myteams', component: MyTeams, meta: { requiresAuth: true } },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('token'); // Controlla se esiste un token di autenticazione

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login'); // Se la rotta richiede autenticazione e l'utente non è autenticato, reindirizza a login
  } else {
    next(); // Altrimenti, continua normalmente
  }
});

export default router;
