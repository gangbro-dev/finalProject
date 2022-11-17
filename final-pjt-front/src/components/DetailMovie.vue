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
    <button>좋아요</button>
  </div>
</template>

<script>

export default {
  name: 'DetailMovie',
  props: {
    movie: Object,
  },
  computed: {
    movie_poster () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    }
  }, 
}
</script>

<style>

</style>