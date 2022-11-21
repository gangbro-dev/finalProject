<template>
  <div>
    <h1>{{ user }}님의 프로필</h1>
    <p>좋아하는 영화</p>
    <button v-if="!is_follow">팔로우</button>
    <button v-else>팔로우 취소</button>
  </div>
</template>

<script>
// import axios from 'axios'


export default {
  name: 'ProfileView',
  data() {
    return {
      is_follow: false,
    }
  },
  computed: {
    user() {
      return this.$route.params.user_name
    },
  },
  beforeMount() {
    this.$store.dispatch('getUser')
  },

}
</script>

<style>

</style>