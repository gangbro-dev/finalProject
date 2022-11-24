<template>
  <div>
    <div class="d-flex flex-column align-items-center" style="width: 100%; height: 600px; margin-top: 22vh;">
      <h1 class="mb-5">회원 정보 수정</h1>
      <p> * 변경을 원하시지 않으면 입력칸을 비워주세요</p>
      <form @submit.prevent='profileChange' style="width: 330px;">
        <div class="d-flex justify-content-between align-items-center my-2" style="width: 100%;">
          <label for="password1">변경 비밀번호</label>
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
          <router-link 
            :to="{name: 'ProfileView', params: { user_name: $route.params.user_name }}" 
            class="btn btn-secondary btn-sm mx-2"> 뒤로 </router-link>
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
  name: "ProfileUpdateView",
  data() {
    return {
      password1: null,
      password2: null,
      profileImage: null,
    };
  },
  computed: {
    messages() {
      return this.$store.getters.getErrorMessage;
    }
  },
  methods: {
    profileChange() {
      let is_edit = false
      const password1 = this.password1;
      const password2 = this.password2;
      this.getImage();
      const profile_image = this.profileImage;
      const payload = {
        password1: password1,
        password2: password2,
      };
      if (password1 && password2) {
        this.$store.dispatch("profileUpdate", payload)
        is_edit = true
      } else this.$store.commit('GET_AUTH_ERROR', [])
      if (profile_image) {
        console.log("프로필 이미지 저장 직전");
        console.log(profile_image);
        this.$store.dispatch("editProfileImage", profile_image);
        is_edit = true
      }
      if ((!this.$store.state.err_message.length) && is_edit) {
        this.$router.push({name: 'ProfileView', params: { user_name: this.$route.params.user_name }})
      }
    },
      getImage() {
        if (this.$refs.profileImage.files[0])
          this.profileImage = this.$refs.profileImage.files[0];
        else
          this.profileImage = null;
      }
  },
}
</script>

<style>

</style>