<template>
  <div>
    <h1>Movie</h1>
    <hr>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  },
  Beforecreate () {
    this.$store.dispatch('getMovies')
  }

}
</script>

<style>

</style>