<template>
  <div v-if="!is_editing" class="d-flex justify-content-between community">
    <div>
      <router-link :to="{name: 'ProfileView', params:{ user_name: comment.user.username }}">
        {{ comment.user.username }}
      </router-link>
       :
      {{ comment.content}}
    </div>
    <div v-if="isWriter">
      <button @click="changeToForm" class="btn btn-dark btn-sm" >Edit</button>
      <button @click="deleteComment" class="btn btn-danger btn-sm">X</button>
    </div>
  </div>
  <div v-else class="community">
    <form @submit.prevent='updateComment'>
      <input type="text" v-model='input'>
      <button type="submit" class="btn btn-dark btn-sm">확인</button>
      <button @click='canclingEdit' class="btn btn-dark btn-sm">취소</button>
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
.community button {
  margin-left: 1rem; 
}
</style>