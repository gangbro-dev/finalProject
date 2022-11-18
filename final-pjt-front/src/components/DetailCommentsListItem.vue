<template>
  <div>
    {{ comment.user.username }} :
    {{ comment.content }}
    <button @click="deleteComment" >X</button>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: "DetailCommentsListItem",
  props: {
    comment : Object,
  },
  methods: {
    deleteComment() {
      const commentId = this.comment.id
      axios ({
        method: 'delete',
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.comment.movie.id}/comment/`,
        data: {commentId: commentId},
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$emit('refresh_comments')
      })
      .catch((err) => {
        console.log(err)
      })
      // this.$router.go(this.$router.currentRoute) 
    }
  }
}
</script>

<style>

</style>