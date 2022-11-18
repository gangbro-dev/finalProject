<template>
  <div>
    <form @submit='createComment'>
      <input
        type="text"
        v-model='comment'
      >
      <button type="submit">확인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

// const API_URL = 'http://192.168.202.105:8000'
export default {
  name: 'DetailCommentsForm',
  props: {
    movie: Object,
  },
  data() {
    return {
      comment : null
    }
  },
  methods: {
    createComment() {
      const comment = this.comment
      
      axios({
        method: 'post',
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.movie.id}/comment/`,
        data: {
          // userToken: this.$store.state.token,
          comment,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .catch((err) => {
        console.log(err)
      })
        
    }
  }

}
</script>

<style>

</style>