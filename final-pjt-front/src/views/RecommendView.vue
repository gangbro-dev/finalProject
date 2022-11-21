<template>
  <div>
    <h1>Recommend</h1>
    <RecommendDetail
      v-for="recommendMovie in recommendMovies"
      :key="recommendMovie.id"
      :recommendMovie="recommendMovie"
    />
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
    }
  },
  components: {
    RecommendDetail,
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

    }
  },
  created() {
    this.getRecommend()
  }
}
</script>

<style>

</style>