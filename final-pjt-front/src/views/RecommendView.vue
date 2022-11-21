<template>
  <div>
    <h1>Recommend</h1>
    <hr>
    <div v-if="recommendMovies.length > idx">
      <RecommendDetail
        :recommendMovie="recommendMovie"
      />
      <button @click="nextMovie">다음</button>
    </div>
    <div v-else>
      <p>대기열이 끝나버렷네요 ㅜ.ㅜ</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RecommendDetail from "@/components/RecommendDetail"

export default {
  name: "RecommendView",
  data() {
    return {
      recommendMovies: [],
      idx: 0,
      // recommendMovie: null,
    }
  },
  components: {
    RecommendDetail,
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
  }
}
</script>

<style>

</style>