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
    movies: null,
    articles: [],
    token: null,
    API_URL : API_URL,
    user: null,
    likeMovies: [],
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
      router.push({name : 'LoginView'})
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    GET_USER(state, user) {
      state.user = user
    },
    GET_LIKE_MOVIE(state, likeMovies) {
      state.likeMovies = likeMovies
    },
  },
  actions: {
    // 영화 정보 가져오기
    getMovies(context) {
      if (context.state.movies.length >= 2000) {
        return
      }
      else {
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
      }
    },
    // 회원가입
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
    // 로그인
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
          context.dispatch('getUser')
        })
    },
    // 로그아웃
    logout(context) {
      context.commit('LOGOUT')
    },
    // 게시판 전제 가져오기
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
    // 현재 로그인된 유저 이름 가져오기
    getUser(context) {
      if (context.state.token) {
        axios ({
          method: 'get',
          url: `${API_URL}/accounts/user`,
          headers: {
            Authorization: `Token ${context.state.token}`
          }
        })
        .then((res) => {
          context.commit('GET_USER', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    // 입력한 유저의 좋아요 표시한 영화 가져오기
    getLikeMovie(context, user) {
      axios({
        method: 'get',
        url: `${context.state.API_URL}/api/v1/movies/like_movies/${user}`,
        headers: {
          Authorization: `Token ${context.state.token}`
        }
      })
        .then((res) => {
          context.commit('GET_LIKE_MOVIE', res.data)
        }) 
        .catch((err) => {
          console.log(err)
        })
    },
  },
  modules: {
  }
})
