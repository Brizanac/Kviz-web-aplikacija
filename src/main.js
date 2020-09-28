//import Vue from 'vue'
//import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import { createApp } from 'vue'
//import Vuetify from 'vuetify'
import App from './App.vue'
import router from './router'
import store from './store'

// Install BootstrapVue
//Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
//Vue.use(IconsPlugin)

import axios from 'axios'

createApp(App).config.productionTip = false;

window.axios = axios.create({
  baseURL: 'http://localhost:5000'
})

/*
new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
*/

createApp(App).use(store).use(router).mount('#app')
