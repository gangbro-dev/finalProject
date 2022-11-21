<template>
<div>
  <div class="d-flex justify-content-between">
    <div>제목</div>
    <div>
      <span class="mx-3">
        작성자
      </span> 
      <span class="mx-3">
        작성 시간
      </span> 
    </div>
  </div>
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