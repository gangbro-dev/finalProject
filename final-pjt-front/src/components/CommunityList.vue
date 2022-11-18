<template>
<div>
  <hr>
  <CommunityListItem
  v-for="article in articles"
  :key="article.id"
  :article="article"/>
</div>
</template>

<script>
import CommunityListItem from '@/components/CommunityListItem'

export default {
  name: "CommunityList",
  components: {
    CommunityListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  }
}
</script>

<style>

</style>