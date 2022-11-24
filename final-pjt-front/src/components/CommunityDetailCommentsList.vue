<template>
  <div v-if='article'>
    <CommunityDetailCommentsListItem
    v-for="(comment,index) in comments"
    :key="index"
    :comment="comment"
    @refresh_comments="getComment"
    class="m-2"
    />
    <CommunityDetailCommentsForm
    :article="article"
    @refresh_comments="getComment"
    />
  </div>
</template>

<script>
import CommunityDetailCommentsListItem from "@/components/CommunityDetailCommentsListItem"
import CommunityDetailCommentsForm from "@/components/CommunityDetailCommentsForm"
import axios from 'axios'

export default {
  name: "CommunityDetailCommentsList",
  data() {
    return {
      comments: []
    }
  },
  props: {
      article: Object,
  },
  components: {
    CommunityDetailCommentsListItem,
    CommunityDetailCommentsForm,
  },
  methods : {
    getComment() {
      axios({
        method: 'get',
        url: `${this.$store.state.API_URL}/articles/${this.article.id}/comment/`
      })
        .then((res) => {
          this.comments = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  mounted() {
    this.getComment()
  }
}
</script>

<style>

</style>