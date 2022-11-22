<template>
  <div>
    <form @submit.prevent='createComment'>
      <input
        type="text"
        v-model='comment'
      >
      <button type="submit" class="btn btn-dark btn-sm">확인</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

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
          comment,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$emit('refresh_comments')
        this.comment = null
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