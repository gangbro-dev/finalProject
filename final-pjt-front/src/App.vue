<template>
  <div id="app" >
    <nav class="navbar navbar-expand-lg bg-light d-flex justify-content-between">
      <span id='nav-menu'>
        <router-link :to="{ name : 'MovieView'}" >Movie</router-link> |
        <router-link :to="{ name : 'CommunityView' }">Community</router-link> |
        <router-link :to="{ name : 'RecommendView' }">Recommend</router-link> 
      </span>
      <span id="nav-account" v-if='!isLogin'>
        <router-link  :to="{ name : 'SignUpView' }">SignUp</router-link> |
        <router-link  :to="{ name : 'LoginView' }">Login</router-link>
      </span>
      <span id="nav-account" v-else>
        <router-link :to="{ name : 'ProfileView', params: {user_name : user} }">Profile</router-link> |
        <a type='button' class='logoutButton' @click='logout' >Logout</a> 
      </span>
    </nav>
    <router-view class='container'/>
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

#nav-menu {
  margin: 0px 2rem 0px;
}

#nav-account {
  margin: 0px 2rem 0px;
}
</style>
