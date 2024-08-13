import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EditCampaign from '@/components/EditCampaign.vue';
import EditAd from '@/components/EditAd.vue';
import AddAd from '@/components/AddAd.vue'
import AdComponent from '@/components/AdComponent.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/login.vue')
  },
  {
    path: '/register-brand',
    name: 'register-brand',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/register-brand.vue')
  },
  {
    path: '/register-influencer',
    name: 'register-influencer',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/register-influencer.vue')
  },
  {
    path: '/sponsor-dashboard',
    name: 'sponsor-dashboard',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/sponsor-dashboard.vue')
  },
  {
    path: '/Admin-dashboard',
    name: 'Admin-dashboard',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Admin-dashboard.vue')
  },
  {
    path: '/influencer-dashboard',
    name: 'influencer-dashboard',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/influencer-dashboard.vue')
  },
  {
    path: '/edit-campaign/:id',
    name: 'EditCampaign',
    component: EditCampaign,
  },
  {
    path: '/edit-ad/:id',
    name: 'EditAd',
    component: EditAd,
  },
  {
    path: '/add-ad/:id',
    name: 'AddAd',
    component: AddAd,
  },
  {
    path: '/ads',
    name: 'Ads',
    component: AdComponent
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
