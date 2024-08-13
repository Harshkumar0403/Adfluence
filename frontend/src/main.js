import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

if (module.hot) {
    console.log('HMR is enabled.');
    module.hot.accept();
  }

createApp(App).use(router).mount('#app')
