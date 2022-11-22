<template>
  <div>
    <img :src="likemovie_poster" alt="">
  </div>
</template>

<script>
export default {
  name: 'ProfileLikeMovie',
  props:{
    likeMovie: Object,
  },
  computed: {
    likemovie_poster () {
      return `https://image.tmdb.org/t/p/original${this.likeMovie.poster_path}`
    }
  }
}
</script>

<style>

</style>