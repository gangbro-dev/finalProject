<template>
  <div id="app container" >
    <nav class="nav navbar navbar-expand-lg bg-light d-flex justify-content-between">
      <span id='nav-menu'>
        <router-link :to="{ name : 'MovieView'}" >Movie</router-link> |
        <router-link :to="{ name : 'CommunityView' }">Community </router-link>
        <router-link v-if='isLogin' :to="{ name : 'RecommendView' }">| Recommend</router-link> 
      </span>
      <span id="nav-account" v-if='!isLogin'>
        <router-link  :to="{ name : 'SignUpView' }">SignUp</router-link> |
        <!-- <router-link  :to="{ name : 'LoginView' }">Login</router-link> -->
        <b-div v-b-toggle.sidebar-right>Log In</b-div>
        <b-sidebar id="sidebar-right" title="" right shadow>
          <div class="px-3 py-2">
            <LoginView/>
          </div>
        </b-sidebar>
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
import LoginView from '@/views/LoginView'

export default {
  components: {
    LoginView
  },
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
  },
  mounted () {
    this.$router.push({ name: 'MovieView' })
  }
  
}
</script>

<style>
@font-face {
    font-family: 'IBMPlexSansKR-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/IBMPlexSansKR-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
#app {
  font-family: IBMPlexSansKR-Regular, Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
;
}

div a {
  color: #2c3e50;
  text-decoration: none;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
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
div {
  font-family: IBMPlexSansKR-Regular;
}
b-div {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}
</style>
