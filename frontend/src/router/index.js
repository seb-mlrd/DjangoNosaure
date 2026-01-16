import { createRouter, createWebHistory } from 'vue-router'
import DinoListView from '../views/DinoListView.vue'
import SingleDinoView from '@/views/SingleDinoView.vue'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/dinos/',
      name: 'dinos',
      component: DinoListView
    },
    {
      path: '/dino/:id',
      name: 'showDino',
      component: SingleDinoView
    }
  ],
})

export default router
