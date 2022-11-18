<template>
  <div>
    <hr>
    <DetailCommentsListItem
    v-for="(comment, index) in comments"
    :key="index"
    :comment="comment"
    />
  </div>
</template>

<script>
import DetailCommentsListItem from "@/components/DetailCommentsListItem"
import axios from 'axios'

// const API_URL = 'http://192.168.202.105:8000'

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
        url: `${this.$store.state.API_URL}/api/v1/movies/${this.movie.id}/comment/`,
      })
      .then((res) => {
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