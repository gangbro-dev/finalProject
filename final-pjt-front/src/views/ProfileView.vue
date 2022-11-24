<template>
  <div>
    <h1>프로필</h1>

    <div class="d-flex justify-content-center m-5">
      <div class="box">
        <img class="profile" :src="`${apiUrl}/media/${profileImg}`" alt="">
      </div>
      <div class="username">
        <h1>{{ user }}</h1>
        <div v-if="isMyPage">
          <router-link :to="{name: 'ProfileUpdateView', params: {user_name: user}}">
            <button class="btn btn-dark">회원정보 수정</button>
          </router-link>
        </div>
        <div v-else>
          <button v-if="!is_follow" class="btn btn-dark" @click="follow" v-b-toggle.sidebar-right>팔로우</button>
          <button v-else class="btn btn-dark" @click="follow" v-b-toggle.sidebar-right>팔로우 취소</button>
          <p class="mt-3"> 팔로우 : {{ followers }} | 팔로잉 : {{ followings }}</p>
        </div>
      </div>
    </div>

  <hr>
    <div class="d-flex flex-column align-items-center" style="width: 100%; height: 600px; margin-top: 5rem;"> 
      <div>
        <p>좋아요 표시한 영화</p>
      </div>
      <div class="d-flex flex-wrap">
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
    apiUrl() {
      return this.$store.state.API_URL
    },
    profileImg() {
      return this.$store.state.imgData
    },
    is_follow() {
      return this.$store.state.isFollowed
    },
    followers() {
      return this.$store.state.followerCount
    },
    followings() {
      return this.$store.state.followingCount
    },
    isMyPage() {
      return this.user === this.$store.state.user.username
    }
  },
  methods: {
    getLikeMovies() {
      console.log('좋아하는 영화 갱신됨')
      const user= this.user
      console.log(user)
      this.$store.dispatch('getLikeMovie', user)
      console.log('프로필 이미지 갱신됨')
      this.$store.dispatch('getImg', user)
      return user
    },
    getFollowed() {
      console.log('팔로우 확인')
      const user= this.user
      this.$store.dispatch('getFollowCount', user)
    },
    follow() {
      console.log('팔로우 시도')
      const user= this.user
      this.$store.dispatch('follow', user)
    }
  },

  beforeMount() {
    this.getLikeMovies()
    this.getFollowed()
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
.box {
    width: 150px;
    height: 150px; 
    margin-right: 4rem;
    border-radius: 70%;
    overflow: hidden;
}
.profile {
    width: 100%;
    height: 100%;
    object-fit: cover;
}


</style>