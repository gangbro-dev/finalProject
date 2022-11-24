<template>
<div>
  <div class="d-flex justify-content-between">
    <div class= "mx-4">No</div>
    <div >제목</div>
    <div>
      <span class="me-5">
        작성자  
      </span> 
      <span class="mx-4">
        작성 시간
      </span> 
    </div>
  </div>
  <hr>
  <CommunityListItem
  v-for="article in articles.slice().reverse()"
  :key="article.id"
  :article="article"/>
  <div class="d-flex justify-content-center">
    <ul class="pagination">
      <li class="page-item"><a class="page-link" href="#">Previous</a></li>
      <li class="page-item"><a class="page-link" href="#">1</a></li>
      <li class="page-item"><a class="page-link" href="#">2</a></li>
      <li class="page-item"><a class="page-link" href="#">3</a></li>
      <li class="page-item"><a class="page-link" href="#">Next</a></li>
    </ul>
  </div>
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