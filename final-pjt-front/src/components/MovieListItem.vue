<template>
  <div
  @mouseenter="mouseOver"
  @mouseleave="mouseOut">
    <router-link :to="{ name :'DetailView', params:{id: movie.id}  }">
      <img :src="movie_poster" alt="" 
      >
    </router-link>
    <router-link :to="{ name :'DetailView', params:{id: movie.id}  }">
      <div style="position:relative; top: -200px; height: 0px;">
        <div v-if="isMouseOver" class="d-flex flex-column justify-content-center movieListOverlay">
          <h3 class="text-center" style="width: 12rem; height:6rem">{{ movie.title }}</h3>
          <b-form-rating v-model="rate" variant="warning" size="md"  show-value readonly></b-form-rating>
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  data() {
    return {
      isMouseOver: false,
    }
  },
  props: {
    movie: Object,
  },
  computed: {
    movie_poster () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    },
    rate() {
      return this.movie.rate / 20
    }    
  },
  methods :{
    mouseOver() {
      this.isMouseOver = true
      event.target.firstChild.classList.toggle("listItem")
    },
    mouseOut() {
      this.isMouseOver = false
      event.target.firstChild.classList.toggle("listItem")
    }
  }

}
</script>

<style>
img {
  width : 12rem;
  height: 17rem;
}
.listItem img{
  opacity: 0.2;
  transform: scale(1.1);
  z-index: 1;
  transition: all ease 300ms;
  border: solid 5px #42b983;
  border-radius: 10%;
}
</style>