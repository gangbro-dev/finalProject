<template>
  <div>
    <router-link :to="{ name :'DetailView', params:{id: likeMovie.id}  }" id="userProfileLikeMovie">
      <img :src="likemovie_poster" alt="">
    </router-link>
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
  #userProfileLikeMovie img {
    width: 18rem;
    height: calc(18rem * 1.414);
    margin-bottom: 1rem;
  }
</style>