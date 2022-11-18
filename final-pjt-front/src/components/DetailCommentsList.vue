<template>
  <div>
    <hr>
    <DetailCommentsListItem
    v-for="(comment, index) in comments"
    :key="index"
    :comment="comment"
    @refresh_comments='getComment'
    />
    <DetailCommentsForm
      :movie="movie"
      @refresh_comments='getComment'/>
  </div>
</template>

<script>
import DetailCommentsListItem from "@/components/DetailCommentsListItem"
import DetailCommentsForm from '@/components/DetailCommentsForm'
import axios from 'axios'


export default {
  name: "DetailCommentsList",
  data() {
    return {
      comments: []
    }
  },
  components: {
    DetailCommentsListItem,
    DetailCommentsForm,
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
      .catch((err) => {
        console.log(err)
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