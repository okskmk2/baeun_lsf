import Vue from 'vue'
import App from './views/App.vue'
import router from './router'
import store from './store'
import i18n from './i18n'
import './assets/base.less';

Vue.config.productionTip = false;

new Vue({
  i18n,
  router,
  store,
  render: h => h(App)
}).$mount('#app');
