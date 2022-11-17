<template>
  <div>
    {{ comment.user.username }} :
    {{ comment.content }}
    <hr>
  </div>
</template>

<script>
export default {
  name: "DetailCommentsListItem",
  props: {
    comment : Object,
  }
}
</script>

<style>

</style>