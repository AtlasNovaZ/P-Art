import { createWebHistory, createRouter, RouteRecordRaw } from "vue-router";

import * as Pages from '../pages'

const routes: Array<RouteRecordRaw> = [
  {
    name: 'Home',
    path: '/',
    component: Pages.Home
  },
  {
    name: 'About',
    path: '/about',
    component: Pages.About
  },
  {
    name: 'Show Generated Image',
    path: '/generate/:generatedImageId',
    component: Pages.Generated
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
