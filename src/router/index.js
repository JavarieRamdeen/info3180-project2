import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/logout',
      name: 'logout',
      component: HomeView
    },
    {
      path: '/explore',
      name: 'explore',
      component: () => import('../views/ExploreView.vue')
    },
    {
      path: '/users/user_id',
      name: 'user',
      component: () => import('../views/UserView.vue')
    },
    {
      path: '/cars/new',
      name: 'new_car',
      component: () => import('../views/NewCarView.vue')
    },
    {
      path: '/cars/car_id',
      name: 'car',
      component: () => import('../views/CarView.vue')
    }
  ]
})

export default router
