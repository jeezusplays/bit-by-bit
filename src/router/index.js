// Import Vue and VueRouter
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Dashboard from '../components/dashboard/Dashboard.vue'


// Define routes
const routes = [
  { path: '/home', component: Home },
  { path: '/dashboard', component: Dashboard },
]

// Create the router
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
