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
        <ul class="footer-button-plus">
          <input ref="profileImage" type="file" label="이미지 제출" style="width: 400px; margin-left: 100px;"
              @change="onImageChange"/>
        </ul>
        <div class="d-flex justify-content-end align-items-center my-2" style="width: 100%;">
          <input type="submit" value='확인' class="btn btn-dark btn-sm" >
        </div>
      </form>
      <ul>
        <li v-for="message, index in messages"
        :key="index">{{ message }}</li>
      </ul>
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
      uploadimage: '',
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
      const profile_image = this.uploadimageurl

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
        profile_image: profile_image,
      }
      this.$store.dispatch('signUp',payload)
    },
    onImageChange() {
      this.uploadimage = this.$refs.profileImage.files
      console.log(this.uploadimage)
    }
  }
}
</script>

<style>

</style>