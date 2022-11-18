<template>
  <div>
    <router-link :to="{ name: 'CommunityDetailView', params: {id : article.id} }">
      <p>{{ article.title }}</p>
      <p>작성자: {{ article.user.username }} </p>
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: "CommunityListItem",
  props: {
    article: Object,
  }
}
</script>

<style>

</style>