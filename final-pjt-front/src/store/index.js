import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)


const API_URL = process.env.VUE_APP_LOCAL_BACK_SERVER_ADRESSE


export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies: [],
    articles: [],
    token: null,
    API_URL : API_URL,
    user: {username: null},
    likeMovies: [],
    err_message: [],
    imgData: null,
    // 팔로우 관련 데이터
    isFollowed: null,
    followerCount: null,
    followingCount: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    getErrorMessage(state) {
      return state.err_message
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    SAVE_TOKEN(state, token) {
      console.log('로그인 성공')
      state.token = token
      console.log('메인페이지로 이동합니다.')
      router.push({name : 'MovieView'})
    },
    LOGOUT(state) {
      state.token = null
      localStorage.removeItem('user')
      router.push({name : 'MovieView'})
    },
    GET_ARTICLES(state, articles) {
      state.articles = articles.slice().reverse()
    },
    GET_USER(state, user) {
      state.user = user
      console.log('유저 정보 가져오기 완료')
    },
    GET_LIKE_MOVIE(state, likeMovies) {
      state.likeMovies = likeMovies
    },
    GET_AUTH_ERROR(state, err_data) {
      let error_message = []
      for (const err_key in err_data) {
        error_message = [...error_message, ...err_data[err_key]]
      }
      state.err_message = error_message
    },
    GET_IMG(state, imgData) {
      state.imgData = encodeURI(imgData)
    },
    // 팔로우 데이터 저장
    GET_FOLLOW_DATA(state, followData) {
      state.isFollowed = followData.isFollowed
      state.followerCount = followData.followerCount
      state.followingCount = followData.followingCount
    }
  },
  actions: {
    // 영화 정보 가져오기
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
        console.log('프로필 이미지 저장 직전')
        console.log(payload.profile_image)
        context.dispatch('editProfileImage', payload.profile_image)
        context.dispatch('getUser')
        context.commit('GET_AUTH_ERROR', [])
      })
      .catch((err) => {
        console.log(err.response.data)
        context.commit('GET_AUTH_ERROR', err.response.data)
      })
    },
    // 프로필 이미지 저장
    editProfileImage(context, Image) {
      console.log('프로필 이미지 저장 시작')
      console.log(Image)
      const profile_image = new FormData();
      profile_image.append('image', Image)
      console.log(profile_image)
      const headers = {
        'Content-Type': 'multipart/form-data', // Content-Type을 변경해야 파일이 전송됨
        'Authorization': `Token ${context.state.token}`,
      }
      axios({
        method: "put",
        url: `${API_URL}/api/v1/accounts/image/`,
        data: profile_image,
        headers: headers
      })
      .then(() => {
        console.log('프로필 이미지 전송 성공')
        context.dispatch('getImg', context.user.username)
      })
      .catch((err) => {
        console.log(err.response.data)
      })
    },
    // 로그인
    login(context, payload) {
      console.log('로그인 시작')
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        }
      })
        .then((res) => {
          console.log('로그인 요청 성공')
          context.commit('SAVE_TOKEN', res.data.key)
          context.dispatch('getUser')
        }).catch((err) => {
          console.log('로그인 실패')
          console.log(payload)
          console.log(err)
        })
    },
    // 로그아웃
    logout(context) {
      context.commit('LOGOUT')
      context.dispatch('getUser')
    },
    //회원 정보 수정
    profileUpdate(context, payload) {
      const headers = {
        'Authorization': `Token ${context.state.token}`,
      }
      axios({
        method: "post",
        url: `${API_URL}/accounts/password/change/`,
        data: {
          new_password1: payload.password1,
          new_password2: payload.password2
        },
        headers: headers,
      })
      .then(() => {
        context.commit('GET_AUTH_ERROR', [])
      })
      .catch((err) => {
        console.log(err.response.data)
        context.commit('GET_AUTH_ERROR', err.response.data)
      })
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
          context.dispatch('getImg', res.data.user.username)
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        context.commit('GET_USER', {username: null})
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
    // 프로필 이미지 가져오기
    getImg(context, user) {
      const headers = {
        'Authorization': `Token ${context.state.token}`,
      }
      axios({
        method: "get",
        url: `${API_URL}/api/v1/accounts/image/${user}`,
        headers: headers
      })
        .then((res) => {
          console.log(res.data)
          context.commit("GET_IMG", res.data)
        })
    },
    // 팔로우 여부, 총 팔로우 수 가져오기
    getFollowCount(context, user) {
      const headers = {
        'Authorization': `Token ${context.state.token}`,
      }
      axios({
        method: "GET",
        url: `${API_URL}/api/v1/accounts/follow/${user}`,
        headers: headers,
      })
        .then((res) => {
          context.commit('GET_FOLLOW_DATA', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // 팔로우하기 
    follow(context, user) {
      const headers = {
        'Authorization': `Token ${context.state.token}`,
      }
      axios({
        method: "POST",
        url: `${API_URL}/api/v1/accounts/follow/`,
        headers: headers,
        data: {
          user: user
        }
      })
        .then((res) => {
          console.log(res.data)
          context.dispatch('getFollowCount', user)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
