<template>
  <div class='container'>
    <p>{{ movie.title }}</p>
    <img :src="movie_poster" alt="">
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  computed: {
    movie_poster () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    }
  }

}
</script>

<style>
img {
  width : 30rem;
}
</style>