<template>
  <div>
    <h1>Community</h1>
    <router-link :to="{ name: 'CreateView'}"><button class="btn btn-dark">CREATE</button></router-link>
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