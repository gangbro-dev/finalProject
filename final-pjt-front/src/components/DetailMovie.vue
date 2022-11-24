<template>
  <div class="d-flex flex-column align-items-start mt-5">
    <h1>{{ movie.title }}</h1>
    <div class="d-flex">
      <span
      v-for='(genre, index) in movie.genre'
      :key='index'
      class="badge rounded-pill bg-secondary ms-1 me-2"
      > {{ genre.name }} </span>
    </div>
    <div class="d-flex mt-3" style="width: 100%">
      <div class="poster-container me-1">
        <img :src="movie_poster" alt="" class="poster">
      </div>
      <div class="d-flex justify-content-center" style="width: 100%">
        <DetailVideo
        :movie="movie"/>
      </div>
    </div>
    <div class="d-flex my-3">
      <b-form-rating v-model="rate" variant="warning" size="md"  show-value readonly></b-form-rating>
      <img class="like-heart" v-if="!is_like" @click="getLike" src="https://img.icons8.com/material-two-tone/48/FF0000/filled-like.png" v-b-toggle.sidebar-right/>
      <img class="like-heart" v-else  @click="getLike" src="https://img.icons8.com/material-sharp/48/FF0000/filled-like.png" v-b-toggle.sidebar-right/>
    </div>
    <hr>
    <p class="overview">{{ movie.overview }}</p> 
    <p>개봉일 : {{ movie.release_date }} </p>
  </div>
</template>

<script>
import axios from 'axios'
import DetailVideo from '@/components/DetailVideo'
// const API_URL = 'http://192.168.202.105:8000'

export default {
  name: 'DetailMovie',
  components: {
    DetailVideo,
  },
  props: {
    movie: Object,
  },
  data() {
    return {
      is_like: null,
    }
  },
  computed: {
    movie_poster () {
      return `https://image.tmdb.org/t/p/original${this.movie.poster_path}`
    },
    rate() {
      return this.movie.rate / 20
    }
  }, 
  methods: {
    getLike() {
      axios({
        method: "post",
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.movie.id}/is_liked/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.is_like = res.data.like

        })
        .catch((err) => {
          console.log(err)
        })
    },
    checkLike() {
      axios({
        method: "get",
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.movie.id}/is_liked/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.is_like = res.data.like
          return res.data.like
        })
        .catch((err) => {
          console.log(err)
        })

    }
  },
  beforeMount() {
    this.checkLike()
  },
  updated() {
    this.checkLike()
  }

}
</script>

<style>
@font-face {
    font-family: 'IBMPlexSansKR-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/IBMPlexSansKR-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.overview {
  font-family: IBMPlexSansKR-Regular;
}
.like-heart {
  width: 3rem;
  height: 3rem;
  margin-left: 2rem;
  cursor: pointer;  
}
.poster {
  width: auto;
  height: 25rem;
}
</style>