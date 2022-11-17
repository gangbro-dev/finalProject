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

const API_URL = 'http://192.168.202.105:8000'

export default {
  name: "DetailCommentsListItem",
  props: {
    comment : Object,
  },
  methods: {
    deleteComment() {
      const commentId = this.comment.id
      console.log(this.comment.movie.id)
      axios ({
        method: 'delete',
        url: `${API_URL}/api/v1/movies/${this.comment.movie.id}/comment/`,
        data: {commentId: commentId}
      })
      .catch((err) => {
        console.log(err)
      })
      this.$router.go(this.$router.currentRoute) 
    }
  }
}
</script>

<style>

</style>