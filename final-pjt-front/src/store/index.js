import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://192.168.0.2:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    articles: [],
    token: null,
    API_URL : API_URL
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'MovieView' })
    },
    LOGOUT(state) {
      state.token = null
      localStorage.removeItem('user')
      location.reload();
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',  
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)

        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    login(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
    },
    logout(context) {
      context.commit('LOGOUT')
    },
    getArticles(context) {
      axios ({
        method: 'get',
        url: `${API_URL}/articles/`
      })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})
