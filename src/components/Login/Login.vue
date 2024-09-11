<template>
    <div class="login-container">
      <form class="login-form" @submit.prevent="login">
        <h2>Login</h2>
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Login</button>
        <p class="register-link">
          Non hai un account? <a href="/register">Registrati qui</a>
        </p>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        password: '',
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://localhost:5000/login', { // Cambia l'URL con quello del tuo server backend
            email: this.email,
            password: this.password,
          });
  
          // Controlla la risposta del server
          if (response.status === 200) {
            // Salva il token di autenticazione nel localStorage
            localStorage.setItem('token', response.data.token);
            // Reindirizza alla homepage
            this.$router.push('/');
          }
        } catch (error) {
          console.error('Errore durante il login:', error);
          alert('Credenziali non valide. Riprova.');
        }
      },
    },
  };
  </script>
  
  
  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* Rende la pagina a tutta altezza */
    background-color: #f2f2f2; /* Colore di sfondo leggero */
  }
  
  .login-form {
    background-color: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .login-form h2 {
    margin-bottom: 20px;
    color: #fe4c10; /* Colore del testo arancione per il titolo */
  }
  
  .login-form input {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .login-form button {
    width: 100%;
    padding: 10px;
    background-color: #fe4c10; /* Colore del bottone */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .login-form button:hover {
    background-color: #e74300; /* Colore del bottone al passaggio del mouse */
  }
  
  .register-link {
    margin-top: 10px;
  }
  </style>
  