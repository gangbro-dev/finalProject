<template>
  <div>
    <div class="d-flex justify-content-between">
      <h1>Recommend</h1>
      <button @click="nextMovie">다음</button>
    </div>
    <hr>
    <div v-if="recommendMovies.length > idx">
      <DetailMovie
        :movie="recommendMovie"
      />
      
    </div>
    <div v-else>
      <p>대기열이 끝나버렷네요 ㅜ.ㅜ</p>
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
      return this.recommendMovies[this.idx]
    }
  },
  methods: {
    getRecommend() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/api/v1/movies/recommend/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.recommendMovies = res.data
          console.log(res)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    nextMovie() {
      this.idx += 1
    }
  },
  created() {
    this.getRecommend()
  },
}
</script>

<style>

</style>