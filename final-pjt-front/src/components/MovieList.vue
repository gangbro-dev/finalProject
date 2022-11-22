<template>
<div>
  <div class='d-flex flex-wrap justify-content-center'>
    <div v-for="(movie, rowIndex) in movies" :key="rowIndex">
      <MovieListItem 
      :movie='movie' 
      class="m-2"/>
    </div>
  </div>
    <br>
    <div class="col text-center">
      <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
        <!-- <div slot="no-more" style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px;">목록의 끝입니다 :)</div> -->
      </infinite-loading>
    </div>
</div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
import InfiniteLoading from 'vue-infinite-loading';

const EACH_LEN = 30

export default {
  name : 'MovieList',
  components : {
    MovieListItem,
    InfiniteLoading,
  },
  data() {
    return {
      movies: [],
      num: 0,
    }
  },
  // computed: {
  //   movies() {
  //     return this.$store.state.movies
  //   } 
  // },
  created() {
    this.$store.dispatch('getMovies')
    const num = this.num
    this.movies = this.movies.concat(this.$store.state.movies.slice(num, num+EACH_LEN))
    this.num += EACH_LEN
  },
  methods : {
    infiniteHandler($state) {
      const num = this.num
      setTimeout(() => {
        if(this.$store.state.movies.slice(num, num+EACH_LEN).length) {
          this.movies = this.movies.concat(this.$store.state.movies.slice(num, num+EACH_LEN))
          this.num += EACH_LEN
          // 끝 지정(No more this.$store.data.movies) - 데이터가 EACH_LEN개 미만이면 
          if(this.$store.state.movies.length / EACH_LEN < 1) {
            $state.complete()
            return
          }
          $state.loaded()
        } else {
          // 끝 지정(No more this.$store.data.movies)
          $state.complete()
        }
      }, 1000)
    },
  }
}
</script>

<style>
</style>