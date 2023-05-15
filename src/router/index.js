// Import Vue and VueRouter
import { createRouter, createWebHistory } from 'vue-router'

// Import routes
import Home from '../components/Home.vue'
import Dashboard from '../components/dashboard/Dashboard.vue'
import DashboardView from '../views/DashboardView.vue'
import RecommendCourses from '../components/recommendation/RecommendCourses.vue'
import RecommendCareers from '../components/recommendation/RecommendCareers.vue'
import CareerDesc from '../components/recommendation/CareerDesc.vue'



// Define routes
const routes = [
  { path: '/home', component: Home },
  { 
    path: '/', 
    component: DashboardView,
    children: [
      { path: 'dashboard', component: Dashboard },
    ]
  },
  { path: '/recommendcourses', component: RecommendCourses },
  { path: '/recommendcareers', component: RecommendCareers },
  { path: '/careerdesc', component: CareerDesc },

]

// Create the router
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
