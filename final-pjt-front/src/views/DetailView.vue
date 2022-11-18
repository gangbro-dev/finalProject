<template>
  <div v-if="movie">
    <h1>Detail</h1>
    <DetailMovie
    :movie="movie"
    />
    <DetailCommentsForm
    :movie="movie"/>
    <DetailCommentsList
    :movie="movie"/>
    <DetailVideo
    :movie="movie"/>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = 'http://192.168.0.2:8000'
// const key = "550af897681babc49f34957fa75cbee8"
// const url = `https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=${key}&language=ko-KR`


import DetailMovie from '@/components/DetailMovie'
import DetailCommentsForm from '@/components/DetailCommentsForm'
import DetailCommentsList from '@/components/DetailCommentsList'
import DetailVideo from '@/components/DetailVideo'

export default {
  name: "DetailView",
  components: {
    DetailMovie,
    DetailCommentsForm,
    DetailCommentsList,
    DetailVideo,
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