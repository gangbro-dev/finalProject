<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id='title' v-model.trim='title'><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model.trim='content'></textarea>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UpdateView',
  computed: {
    article() {
      return this.$route.params.article
    }
  },
  data() {
    return {
      title: this.$route.params.article.title,
      content: this.$route.params.article.content,
      id: this.$route.params.article_id,
    }
  },
  methods: {
    updateArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요')
        return
      } else if (!content) {
        alert('내용을 입력해주세요')
        return
      }
      console.log(this.id)
      axios({
        method: "put",
        url: `${this.$store.state.API_URL}/articles/${this.id}/`,
        data: {
          title: title,
          content: content,
        },
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        },
      })
        .then(() => {
          this.$router.push({ name: 'CommunityDetailView', params: { id: this.id } })
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  beforMount() {
    this.title = this.$route.params.article.title
    this.content = this.$route.params.article.content
    this.id = this.$route.params.article.id
  }

}
</script>

<style>

</style>