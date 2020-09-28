import { createRouter, createWebHistory } from 'vue-router'
import Registracija from '../views/Registracija.vue'

const routes = [
  {
    path: '/',
    name: 'Registracija',
    component: Registracija
  },
  {
    path: '/home',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/igra',
    name: 'Igra',
    component: () => import('../views/Igra.vue')
  }
]



const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
