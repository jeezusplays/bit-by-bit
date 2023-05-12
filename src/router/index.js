// Import Vue and VueRouter
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'


// Define routes
const routes = [
  { path: '/home', component: Home }
]

// Create the router
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
