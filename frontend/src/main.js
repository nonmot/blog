import Vue from 'vue'
import App from './App.vue'

import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

import gv from './mixins/globalVariables'

Vue.config.productionTip = process.env.NODE_ENV === 'production'

Vue.mixin(gv)

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
