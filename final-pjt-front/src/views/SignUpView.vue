<template>
  <div>
    <div class="d-flex flex-column align-items-center" style="width: 100%; height: 600px; margin-top: 22vh;">
      <h1 class="mb-5">회원 가입</h1>
      <form @submit.prevent='signUp' style="width: 330px;">
        <div class="d-flex justify-content-between align-items-center my-2" style="width: 100%;">
          <label for="username">ID</label>
          <input type="text" id='username' v-model="username">
        </div>
        <div class="d-flex justify-content-between align-items-center my-2" style="width: 100%;">
          <label for="password1">비밀번호</label>
          <input type="password" id='password1' v-model='password1'>
        </div>
        <div class="d-flex justify-content-between align-items-center my-2" style="width: 100%;">
          <label for="password2">비밀번호 확인</label>
          <input type="password" id='password2' v-model='password2'>
        </div> 
        <hr>
        <ul class="footer-button-plus d-flex justify-content-between my-2 p-0">
          <label>프로필 사진</label> 
          <input 
            ref="profileImage" 
            type="file" 
            :name="username"
            accept=".jpg, .jpeg, .png" 
            label="이미지 제출" 
            style="width: 200px;"/>
        </ul>
        <hr>
        <div class="d-flex justify-content-end align-items-center my-2" style="width: 100%;">
          <input type="submit" value='확인' class="btn btn-dark btn-sm" >
        </div>
      </form>
      <ul>
        <li v-for="(message, index) in messages"
        :key="index">{{ message }}</li>
      </ul>
      <!-- <button @click="onImageChange">테스트</button> -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'SignUpView.vue',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
      profileImage: null,
    }
  },
  computed: {
    messages() {
      return this.$store.getters.getErrorMessage
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      this.getImage()
      const profile_image = this.profileImage
      
      const payload = {
        username: username,
        password1: password1,
        password2: password2,
        profile_image: profile_image,
      }
      this.$store.dispatch('signUp',payload)
    },
    getImage() {
      this.profileImage = this.$refs.profileImage.files[0]
      console.log(this.profileImage)
    }
  }
}
</script>

<style>

</style>