<template>
  <div v-if='article'>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }} </p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성시간 : {{ article?.created_at }}</p>
    <p>수정시간 : {{ article?.updated_at }}</p>
    <button @click="deleteArticle">XXX</button>
    <router-link :to="{ name: 'UpdateView', params: {article: article, article_id: article.id} }">[edit]</router-link>
    <CommunityDetailCommentsList
      :article="article"
    />
  </div>
</template>

<script>
import CommunityDetailCommentsList from "@/components/CommunityDetailCommentsList"
import axios from 'axios'

export default {
  name: 'CommunityDetailView',
  data() {
    return {
      article: null,
    }
  },
  components: {
    CommunityDetailCommentsList,
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
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${this.$store.state.API_URL}/articles/${this.$route.params.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then(() => {
          this.$router.push({name : 'CommunityView'})
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