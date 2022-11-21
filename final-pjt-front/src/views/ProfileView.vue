<template>
  <div>
    <h1>{{ user }}님의 프로필</h1>
    <p>좋아하는 영화</p>
    <ProfileLikeMovie
    v-for="likeMovie in likeMovies"
    :key="likeMovie.id"
    :likeMovie="likeMovie"
    />
    <button v-if="!is_follow">팔로우</button>
    <button v-else>팔로우 취소</button>
  </div>
</template>

<script>
import ProfileLikeMovie from "@/components/ProfileLikeMovie"

export default {
  name: 'ProfileView',
  data() {
    return {
      is_follow: false,
      username: null,
    }
  },
  components: {
    ProfileLikeMovie,
  },
  computed: {
    user() {
      return this.$route.params.user_name
    },
    likeMovies() {
      console.log('좋아하는 영화 가져옴')
      return this.$store.state.likeMovies
    },
  },
  methods: {
    getLikeMovies() {
      console.log('좋아하는 영화 갱신됨')
      const user= this.user
      this.$store.dispatch('getLikeMovie', user)
      return user
    },
  },
  beforeMount() {
    this.getLikeMovies()
  },
  watch: {
    user: {
      deep: true,
      handler: function (newUser) {
        this.username = newUser
        this.getLikeMovies()
      }
    }
  }

}
</script>

<style>

</style>