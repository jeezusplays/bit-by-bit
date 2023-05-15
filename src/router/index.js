// Import Vue and VueRouter
import { createRouter, createWebHistory } from 'vue-router'

// Import routes
import Home from '../components/Home.vue'
import Dashboard from '../components/dashboard/Dashboard.vue'
import DashboardView from '../views/DashboardView.vue'
import Recommend from '../components/recommendation/Home.vue'
import OnboardInterest from '../components/onboard/OnboardInterest.vue'


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
  { path: '/recommend', component: Recommend },
  { path:'/onboard/interest', component: OnboardInterest}
]

// Create the router
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
