<template>
  <div>
    <div v-if="!is_editing" class="d-flex justify-content-between moviecomment">
      <div>
        <router-link :to="{name: 'ProfileView', params:{ user_name: comment.user.username }}">
          {{ comment.user.username }}
        </router-link>
        :
        {{ comment.content }}
      </div>
      <div v-if="isWriter">
        <button @click="changeToForm" class="btn btn-dark btn-sm" >Edit</button>
        <button @click="deleteComment" class="btn btn-danger btn-sm">X</button>
      </div>
    </div>
    <div v-else class="moviecomment">
      <form @submit.prevent='updateComment'>
      <input type="text" v-model='input'>
      <button type="submit" class="btn btn-dark btn-sm">확인</button>
      <button @click='canclingEdit' class="btn btn-dark btn-sm">취소</button>
      </form>
    </div>
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
  data() {
    return {
      is_editing: false,
      input: this.comment.content
    }
  },
  computed: {
    isWriter() {
      if (this.$store.state.user.username === this.comment.user.username) {
        return true
      } else {
        return false
      }
    },
    lastContent() {
      return this.comment.content
    }
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
      const commentId = this.comment.id
      axios ({
        method: 'put',
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.comment.movie.id}/comment/`,
        data: {
          commentId: commentId,
          comment: this.input
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
  }
}
</script>

<style>
.moviecomment button {
  margin-left: 1rem;
}
</style>