import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  state: {
    movies: [],
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {
      console.log(movies)
      state.movies = movies

    }
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          console.log(res.data)
          context.commit('GET_MOVIES', res.data)

        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
