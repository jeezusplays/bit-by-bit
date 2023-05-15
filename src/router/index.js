// Import Vue and VueRouter
import { createRouter, createWebHistory } from 'vue-router'

// Import routes
// import Home from '../components/Home.vue'
import NavBar from '../views/NavBar.vue'
import Dashboard from '../components/dashboard/Dashboard.vue'
import Plan from '../components/plan/Plan.vue'
import OnboardInterest from '../components/onboard/OnboardInterest.vue'

// import DashboardView from '../views/DashboardView.vue'
// import Recommend from '../components/recommendation/Home.vue'
import RecommendCourses from '../components/recommendation/RecommendCourses.vue'
import RecommendCareers from '../components/recommendation/RecommendCareers.vue'
import CareerDesc from '../components/recommendation/CareerDesc.vue'



// Define routes
const routes = [
  {
    path: '/',
    component: NavBar,
    children: [
      { path: 'dashboard', component: Dashboard },
      { path: 'plan', component: Plan }
    ]
  },
  
  { path: '/onboard/interest', component: OnboardInterest },

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
