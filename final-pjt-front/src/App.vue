<template>
  <div id="app" class="container">
    <nav>
      <router-link :to="{ name : 'MovieView'}" >Movie</router-link> |
      <router-link :to="{ name : 'SignUpView' }">SignUpPage</router-link> |
      <router-link v-if='!isLogin' :to="{ name : 'LoginView' }">LoginPage</router-link>
      <a v-else type='button' class='logoutButton' @click='logout' >Logout</a>

    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
