<template>
  <div>
    <h1>{{ recommendMovie.title }}</h1>
    <img :src="recommendMovie_poster" alt="">
    <p>평점 : {{ recommendMovie.rate / 10 }}  </p>
    <p>장르 : 
    <span
      v-for='(genre, index) in recommendMovie.genre'
      :key='index'
    > {{ genre.name }} </span>
    </p>
    <p>개봉일 : {{ recommendMovie.release_date }} </p>
    <p>줄거리 : {{ recommendMovie.overview }}</p> 
  </div>
</template>

<script>
export default {
  name: "RecommendDetail",
  props: {
    recommendMovie : Object,
  },
  computed: {
    recommendmovie_poster () {
      return `https://image.tmdb.org/t/p/original${this.recommendmovie.poster_path}`
    }
  }
}
</script>

<style>

</style>