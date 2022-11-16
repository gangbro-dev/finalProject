<template>
  <div>
    <h2>Movie List</h2>
    <hr>
    <MovieListItem/>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'

export default {
  name : 'MovieList',
  components : {
    MovieListItem,
  }


}
</script>

<style>

</style>