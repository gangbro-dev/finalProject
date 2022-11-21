<template>
  <div class='container'>
    <br>
    <router-link :to="{ name :'DetailView', params:{id: movie.id}  }  ">
      <!-- <p>{{ movie.title }}</p> -->
      <img :src="movie_poster" alt="">
    </router-link>
    
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
  width : 12rem;
  height: 18rem;
}
</style>