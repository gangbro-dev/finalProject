<template>
  <div id="app" class='container'>
    <nav>
      <router-link :to="{ name : 'MovieView'}" >Movie</router-link> |
      <span v-if='!isLogin'>
        <router-link  :to="{ name : 'SignUpView' }">SignUp</router-link> |
        <router-link  :to="{ name : 'LoginView' }">Login</router-link>
      </span>
      <a v-else type='button' class='logoutButton' @click='logout' >Logout</a> |
      <router-link :to="{ name : 'CommunityView' }">Community</router-link> |
      <router-link :to="{ name : 'RecommendView' }">Recommend</router-link> 
      <span v-if="isLogin">
      |
      <router-link :to="{ name : 'ProfileView', params: {user_name : user} }">Profile</router-link> 
      </span>
    </nav>
    <router-view/>
  </div>
</template>

<script>

export default {
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
    user() {
      return this.$store.state.user.username
    }

  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
      this.$router.push({name : 'LoginView'})
    },
  },
  beforeCreate() {
    this.$store.dispatch('getUser')
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
