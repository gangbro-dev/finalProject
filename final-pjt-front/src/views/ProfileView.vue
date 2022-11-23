<template>
  <div>
    <h1>프로필</h1>
    <div id='userProfile' class="d-flex flex-column align-items-center" style="width: 100%; height: 600px; margin-top: 5rem;">
      <div id="userInformations" style="width: 100%;" class="d-flex">
        <span>
          <h1>{{ user }}</h1>
        </span>
        <button v-if="!is_follow">팔로우</button>
        <button v-else>팔로우 취소</button>
      </div>
      <hr>
      <p>좋아요 표시한 영화</p>
      <div class="d-flex">
        <ProfileLikeMovie
        v-for="likeMovie in likeMovies"
        :key="likeMovie.id"
        :likeMovie="likeMovie"
        class="me-3"/>
      </div>
    </div>
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
      return this.$store.state.likeMovies.slice(0,5)
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