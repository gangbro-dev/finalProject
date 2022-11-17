<template>
  <div>
    <hr>
    <DetailCommentsListItem
    v-for="(comment, index) in comments"
    :key="index"
    :comment="comment"/>
  </div>
</template>

<script>
import axios from 'axios'
import DetailCommentsListItem from "@/components/DetailCommentsListItem"

const API_URL = 'http://192.168.202.105:8000'

export default {
  name: "DetailCommentsList",
  data() {
    return {
      comments: []
    }
  },
  components: {
    DetailCommentsListItem,
  },
  props:{
    movie: Object,
  },
  methods: {
    getComment() {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/${this.movie.id}/comment/`,
      })
      .then((res) => {
        console.log(res.data)
        this.comments = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  mounted() {
    this.getComment()
  }

}

</script>

<style>

</style>