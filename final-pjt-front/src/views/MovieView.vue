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
  
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  },
  created () {
    this.getMovies()
  }

}
</script>

<style>

</style>