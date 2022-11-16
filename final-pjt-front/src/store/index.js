import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const API_URL = 'http://192.168.202.105:8000'

export default new Vuex.Store({
  state: {
    movies: [],
  },
  getters: {
  },
  mutations: {
  },
  actions: {
    getMovies(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          console.log(res, context)
          // context.commit('GET_MOVIES', res)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
