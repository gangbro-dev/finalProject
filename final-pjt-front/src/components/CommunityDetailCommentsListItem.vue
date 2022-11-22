<template>
  <div v-if="!is_editing" class="d-flex justify-content-between">
    <div>
      {{ comment.user.username }} :
      {{ comment.content}}
    </div>
    <div>
      <button @click="changeToForm">Edit</button>
      <button @click="deleteComment">X</button>
    </div>
  </div>
  <div v-else>
    <form @submit.prevent='updateComment'>
      <input type="text" v-model='input'>
      <button type="submit">확인</button>
      <button @click='canclingEdit'>취소</button>
    </form>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: 'CommunityDetailCommentsListItem',
  props: {
    comment : Object,
  },
  data() {
    return {
      is_editing: false,
      input: null
    }
  },
  methods: {
    deleteComment() {
      axios ({
        method: 'delete',
        url: `${this.$store.state.API_URL}/articles/${this.comment.article.id}/comment/${this.comment.id}`,
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
    },
    changeToForm() {
      this.is_editing = true
      return
    },
    canclingEdit() {
      this.is_editing = false
      return
    },

    updateComment() {
      axios ({
        method: 'put',
        url: `${this.$store.state.API_URL}/articles/${this.comment.article.id}/comment/${this.comment.id}/`,
        data: {
          content: this.input
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then(() => {
        this.$emit('refresh_comments')
        this.is_editing = false
      })
      .catch((err) => {
        console.log(err)
      })
    }
  },
}
</script>

<style>

</style>