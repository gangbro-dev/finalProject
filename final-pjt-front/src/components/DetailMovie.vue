<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <img :src="movie_poster" alt="">
    <p>평점 : {{ movie.rate / 10 }}  </p>
    <p>장르 : 
    <span
      v-for='(genre, index) in movie.genre'
      :key='index'
    > {{ genre.name }} </span>
    </p>
    <p>개봉일 : {{ movie.release_date }} </p>
    <p>줄거리 : {{ movie.overview }}</p> 
    <button v-if="!is_like" @click="getLike">좋아요</button>
    <button v-else @click="getLike">좋아요 취소</button>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = 'http://192.168.202.105:8000'

export default {
  name: 'DetailMovie',
  props: {
    movie: Object,
  },
  data() {
    return {
      is_like: null,
    }
  },
  computed: {
    movie_poster () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    }
  }, 
  methods: {
    getLike() {
      axios({
        method: "post",
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.movie.id}/is_liked/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.is_like = res.data.like

        })
        .catch((err) => {
          console.log(err)
        })
    },
    checkLike() {
      
      axios({
        method: "get",
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.movie.id}/is_liked/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          return res.data.like
        })
        .catch((err) => {
          console.log(err)
        })

    }
  },
  beforeMount() {
    console.log(this.$store.state.API_URL)
    this.is_like = this.checkLike()
  }
}
</script>

<style>

</style>