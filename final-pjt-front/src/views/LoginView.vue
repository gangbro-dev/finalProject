<template>
  <div>
    <h1>Login page</h1>
    <form @submit.prevent='login' class="d-flex flex-column align-items-end">
      <div class="d-flex justify-content-between align-items-center m-1">
        <label for="username" class="me-3">ID : </label>
        <input type="text" id="username" v-model='username'><br>
      </div>
      <div class="d-flex justify-content-between m-1" >
        <label for="password" class="me-3">PW : </label>
        <input type="password" id="password" v-model='password'><br>
      </div>
      <input type="submit" value="login" class="btn btn-dark">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    login() {
      const username = this.username
      const password = this.password

      const payload = {
        username,
        password,
      }
      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style>

</style>