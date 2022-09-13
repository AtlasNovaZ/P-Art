import { createApp } from 'vue'
import App from './App.vue'
import Router from './router'
import './index.css'
import axios from 'axios'



createApp(App).use(Router).mount('#app')
