<template>
  <div>
    <div class="d-flex justify-content-between">
      <h1>Recommend</h1>
      <button @click="nextMovie" class="btn btn-dark btn-sm">다음</button>
    </div>
    <hr>
    <div v-if="recommendMovies.length > idx">
      <DetailMovie
        :movie="recommendMovie"
      />
    </div>
    <div v-else class="d-flex justify-content-center align-items-center">
      <button class="btn btn-dark btn-sm">
        <h1>대기열을 불러오는 중입니다.</h1>
      </button>
      <p>{{ recommendMovie }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import DetailMovie from "@/components/DetailMovie"

export default {
  name: "RecommendView",
  data() {
    return {
      recommendMovies: [],
      idx: 0,
    }
  },
  components: {
    DetailMovie,
  },
  computed: {
    recommendMovie() {
      const movieNow = this.recommendMovies[this.idx]
      if (movieNow) return this.recommendMovies[this.idx]
      else this.getRecommend()
      return null
    }
  },
  methods: {
    getRecommend() {
      console.log('대기열 불러오기 시작')
      const recommended = {
        movies: this.recommendMovies,
      }
      console.log(recommended)
      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v1/movies/recommend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        },
        data: {
          recommended
        }
      })
        .then((res) => {
          console.log('대기열 불러오기 완료')
          this.recommendMovies = [...this.recommendMovies,  ...res.data]
          
        })
        .catch((err) => {
          console.log(err)
        })
    },
    nextMovie() {
      if (this.recommendMovie) this.idx += 1
    }
  },
}
</script>

<style>

</style>