import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import DetailView from '@/views/DetailView.vue'
import CommunityView from '@/views/CommunityView.vue'
import CreateView from '@/views/CreateView.vue'
import UpdateView from '@/views/UpdateView.vue'
import CommunityDetailView from '@/views/CommunityDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import RecommendView from '@/views/RecommendView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView'


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
    path: '/recommend',
    name: 'RecommendView',
    component: RecommendView
  },
  {
    path: '/profile/:user_name',
    name: 'ProfileView',
    component: ProfileView
  },
  {
    path: '/profile/:user_name/update',
    name: "ProfileUpdateView",
    component: ProfileUpdateView,
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

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => {
		if (err.name !== 'NavigationDuplicated') throw err;
	});
};


export default router
