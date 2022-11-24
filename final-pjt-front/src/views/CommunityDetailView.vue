<template>
  <div v-if='article'>
    <div class="d-flex justify-content-end " v-if="isWriter">
      <router-link :to="{ name: 'UpdateView', params: {article: article, article_id: article.id} }"><button class="btn btn-dark ms-2">EDIT</button></router-link>
      <button @click="deleteArticle" class="btn btn-danger ms-2">DELETE</button>
    </div>
    <div class="d-flex justify-content-between align-items-center p-3" style="background-color:cornsilk;">
      <div class="d-flex align-items-center">
        <div style="width:100px">{{ article?.id }}</div>
        <div>{{ article?.title }}</div>
      </div>
      <div>{{ article?.updated_at | date}}</div>
    </div>
    <div class="d-flex justify-content-end">
      <router-link :to="{ name :'ProfileView', params:{user_name : article.user.username} }">작성자 : {{ article?.user.username }}</router-link>
    </div>
    <p style="min-height: 30rem;" class="mx-4">{{ article?.content }}</p>
    <router-link :to="{ name: 'CommunityView' }" class="">
      <button class="btn btn-dark">뒤로</button>
    </router-link>
    <hr>
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
  computed: {
    isWriter() {
      if (this.$store.state.user.username === this.article.user.username) {
        return true
      } else {
        return false
      }
    },
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
  },
  filters: {
    date(data) {
      return data.substr(0, 10)
    }
  },
}
</script>

<style>

</style>