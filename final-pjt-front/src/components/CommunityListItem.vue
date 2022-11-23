<template>
  <div>
    <router-link :to="{ name: 'CommunityDetailView', params: {id : article.id} }" style="text-decoration: none;">
      <div class="d-flex justify-content-between p-2" >
        <div class="d-flex">
          <div class="mx-3">{{ article.id }}</div>
          <div class="communutySpan title ms-5" style="text-decoration: none;">{{ article.title }}</div> 
        </div>
        <div class="communutySpan information d-flex">
          <div class="me-5">
            {{ article.user.username }}
          </div> 
          <div class="ms-3" style="width: 90px;">
            {{article.updated_at | date }}
          </div>
        </div>
      </div>
    </router-link>
    <hr>
  </div>
</template>

<script>
export default {
  name: "CommunityListItem",
  props: {
    article: Object,
  },
  filters: {
    date(data) {
      return data.substr(0, 10)
    }
  }
}
</script>

<style>
.communutySpan {
  text-decoration: none ;
  text-decoration-style: bold;
  color: black;
}
.information {
  color: gray !important;
}
.title {
  font-weight: bold;
}
#간단정보 {
  text-decoration-line: none;
  text-decoration-color: none;
}
</style>