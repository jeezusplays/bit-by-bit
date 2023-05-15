// import './assets/main.css' // Doesn't work for dashboard

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

/* import specific icons */
import {
    faUserSecret,
    faUser,
    faBuilding,
    faHouse,
    faChartPie,
    faMap,
    faChartColumn,
    faComment,
    faStar,
    faMagnifyingGlass,
    faSearch,
    faTag,
    faSquarePhoneFlip,
    faPen,
    fa1,
    fa2,
    fa3,
    faCalendar,
    faCreditCard,
    faLock,
    faPlus,
    faComputer,
    faCircle
  } from "@fortawesome/free-solid-svg-icons";
  import {
    faTwitter,
    faInstagram,
    faLinkedin,
  } from "@fortawesome/free-brands-svg-icons";
  
  /* add icons to the library */
  library.add(
    faUserSecret,
    faTwitter,
    faInstagram,
    faLinkedin,
    faUser,
    faBuilding,
    faHouse,
    faChartPie,
    faMap,
    faChartColumn,
    faComment,
    faStar,
    faMagnifyingGlass,
    faSearch,
    faTag,
    faSquarePhoneFlip,
    faPen,
    fa1,
    fa2,
    fa3,
    faCalendar,
    faCreditCard,
    faLock,
    faPlus,
    faComputer,
    faCircle
  );

const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(router)
app.mount('#app')

