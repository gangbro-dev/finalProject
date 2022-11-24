<template>
  <div>
    <div class="d-flex justify-content-between">
      <h1>Community</h1>
      <router-link v-if="user" :to="{ name: 'CreateView'}"><button class="btn btn-dark">글쓰기</button></router-link>
    </div>
    <CommunityList :pageArticles="pageArticles"/>
    <div class="d-flex justify-content-center">
      <ul class="pagination">
        <li class="page-item"><a class="page-link" href="#" @click="changePage(0)">first</a></li>
        <li class="page-item"
          v-for="(pageNum, index) in pages"
          :key="index"><a class="page-link" href="#" @click="changePage(pageNum)">{{ pageNum + 1 }}</a></li>
        <li class="page-item"><a class="page-link" href="#" @click="changePage(pageLen - 1)">last</a></li>
      </ul>
    </div>
  </div>
</template>

<script>
import CommunityList from "@/components/CommunityList"
import _ from "lodash"

const PAGE_SIZE = 10

export default {
  name: "CommunityView",
  data() {
    return {
      page: 0,
    }
  },
  components: {
    CommunityList,
  },
  computed: {
    pages() {
      const pageLen = this.pageLen
      let pageArr = _.range(pageLen)
      return pageArr
    },
    pageArticles() {
      return this.$store.state.articles.slice(this.page * PAGE_SIZE, (this.page + 1) * PAGE_SIZE)
    },
    pageLen() {
      if ((this.$store.state.articles.length) % PAGE_SIZE) {
        return parseInt((this.$store.state.articles.length) / PAGE_SIZE) + 1
      } else return parseInt((this.$store.state.articles.length) / PAGE_SIZE)
    },
    user() {
      return this.$store.state.user.username
    }

  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    },
    changePage(pageNum) {
      document.querySelector(".pagination").children[this.page + 1].classList.toggle('active')
      this.page = pageNum
      document.querySelector(".pagination").children[pageNum + 1].classList.toggle('active')
    }
  },
  created() {
    this.getArticles()
  },
  mounted() {
    document.querySelector(".pagination").children[this.page + 1].classList.toggle('active')
  }

}
</script>

<style>

</style>