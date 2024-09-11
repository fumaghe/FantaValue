<template>
    <div class="register-container">
      <form class="register-form" @submit.prevent="register">
        <h2>Registrati</h2>
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Password" required />
        <button type="submit">Registrati</button>
        <p class="login-link">
          Hai già un account? <a href="/login">Accedi qui</a>
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
      async register() {
        try {
          const response = await axios.post('http://localhost:5000/register', { // Cambia l'URL con quello del tuo server backend
            email: this.email,
            password: this.password,
          });
  
          if (response.status === 201) {
            alert('Registrazione avvenuta con successo! Ora puoi effettuare il login.');
            this.$router.push('/login');
          }
        } catch (error) {
          console.error('Errore durante la registrazione:', error);
          alert('Registrazione fallita. Riprova.');
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .register-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f2f2f2;
  }
  
  .register-form {
    background-color: white;
    padding: 40px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 300px;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .register-form h2 {
    margin-bottom: 20px;
    color: #fe4c10;
  }
  
  .register-form input {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .register-form button {
    width: 100%;
    padding: 10px;
    background-color: #fe4c10;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .register-form button:hover {
    background-color: #e74300;
  }
  
  .login-link {
    margin-top: 10px;
  }
  </style>
  