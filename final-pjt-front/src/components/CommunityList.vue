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
  v-for="article in pageArticles"
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
  props: {
    pageArticles: Array,
  }
}
</script>

<style>


</style>