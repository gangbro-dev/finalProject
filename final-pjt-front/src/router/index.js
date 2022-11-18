import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import DetailView from '@/views/DetailView.vue'
import CommunityView from '@/views/CommunityView.vue'
import CreateView from '@/views/CreateView.vue'
import UpdateView from '@/views/UpdateView'
import CommunityDetailView from '@/views/CommunityDetailView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movie',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
  {
    path: '/community/:article_id/update',
    name: 'UpdateView',
    component: UpdateView
  },
  {
    path: '/community/:id',
    name: 'CommunityDetailView',
    component: CommunityDetailView
  },
  {
    path: '/movie/:id',
    name: 'DetailView',
    component: DetailView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
