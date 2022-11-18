<template>
  <div>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }} </p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CommunityDetailView',
  data() {
    return {
      article: null,
    }
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/articles/${this.$route.params.id}`
      })
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created() {
    this.getArticleDetail()
  }
}
</script>

<style>

</style>