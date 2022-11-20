<template>
  <div>
    <h1>{{ user }}님의 프로필</h1>
    <p>좋아하는 영화</p>
    <button v-if="!is_follow">팔로우</button>
    <button v-else>팔로우 취소</button>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://192.168.0.2:8000'

export default {
  name: 'ProfileView',
  data() {
    return {
      user : null,
    }
  },
  methods: {
    getUser() {
      axios ({
        method: 'get',
        url: `${API_URL}/accounts/user`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
          this.user = res.data.username
        })
        . catch((err) => {
          console.log(err)
        })
    }
  },
  created () {
    this.getUser()
  }

}
</script>

<style>

</style>