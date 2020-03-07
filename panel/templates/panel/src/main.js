import Vue from 'vue'
import App from './App.vue'
import router from './router';
import store from './store';
import {ValidationProvider,ValidationObserver, localize} from 'vee-validate';
import fa from 'vee-validate/dist/locale/fa.json';

Vue.config.productionTip = false;
Vue.component('ValidationProvider', ValidationProvider);
Vue.component('ValidationObserver', ValidationObserver);
localize('fa', fa);

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app');
