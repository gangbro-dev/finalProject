<template>
  <div v-if="movie">
    <DetailMovie
      :movie="movie"/>
    <DetailCommentsList
      :movie="movie"/>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = 'http://192.168.0.2:8000'
// const key = "550af897681babc49f34957fa75cbee8"
// const url = `https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=${key}&language=ko-KR`


import DetailMovie from '@/components/DetailMovie'
import DetailCommentsList from '@/components/DetailCommentsList'

export default {
  name: "DetailView",
  components: {
    DetailMovie,
    DetailCommentsList,
  },
  data() {
    return {
      movie: null,
    }
  },
  
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.$route.params.id}`

      })
        .then((res) => {
          // console.log(res)
          this.movie = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
}
</script>

<style>

</style>