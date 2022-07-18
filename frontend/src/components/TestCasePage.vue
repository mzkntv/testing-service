<template>
  <div>
    <h1>Сервис проведения тестирования</h1>
    <input type="text" v-model="username" />
    <input type="password" v-model="password" />
    <button @click="signIn">Войти</button>
    <button @click="signUp">Регистрация</button>
    <router-view />
  </div>
</template>

<script>
import {HTTP} from "../plugins/axios.js";

export default {
  name: "TestCasePage",
  data() {
    return {
      username: null,
      password: null,
    }
  },
  mounted() {
    const token = localStorage.getItem('auth_token')
  },
  methods: {
    signIn() {
      HTTP.post('/api/auth/token/login', {
          username: this.username,
          password: this.password,
        }).then(({data}) => {
          localStorage.setItem('auth_token', data.auth_token)
        })
    },
    signUp() {
      HTTP.post('/api/auth/users/', {
        username: this.username,
        password: this.password,
      }).then(() => {
        HTTP.post('/api/auth/token/login', {
          username: this.username,
          password: this.password,
        }).then(({auth_token}) => {
          localStorage.setItem('auth_token', auth_token)
        })
      })
    }
  }
}
</script>
