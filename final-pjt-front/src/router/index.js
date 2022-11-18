import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import DetailView from '@/views/DetailView.vue'
import CommunityView from '@/views/CommunityView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
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
    path: '/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/community',
    name: 'CommunityView',
    component: CommunityView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
