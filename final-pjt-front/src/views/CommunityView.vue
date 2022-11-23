<template>
  <div>
    <div class="d-flex justify-content-between">
      <h1>Community</h1>
      <router-link :to="{ name: 'CreateView'}"><button class="btn btn-dark">글쓰기</button></router-link>
    </div>
    <CommunityList/>
  </div>
</template>

<script>
import CommunityList from "@/components/CommunityList"

export default {
  name: "CommunityView",
  components: {
    CommunityList,
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  },
  created() {
    this.getArticles()
  }

}
</script>

<style>

</style>