<template>
  <div style="width: 45rem; height: 20rem;">
    <div id="video-container">
      <iframe :src="videoURL" frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DetailVideo',
  props: {
    movie: Object,
  },
  computed: {
    videoURL:  function () {
      const videoId = this.movie.trailer
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>
#video-container {
  position: relative;   /* iframe을 container를 기준으로 위치를 지정 */
  padding-top: 56.25%;  /* 유튜브 비디오 비율을 맞추기 위한 높이 설정 */
}

#video-container > iframe {
  position: absolute;   /* container를 기준으로 위치를 지정*/
  top: 0;               /* container의 가장 위쪽으로 위치를 지정 */
  left: 0;
  width: 45rem;
  height: 25rem;
}

</style>