import { createRouter, createWebHistory } from 'vue-router'
import DinoListView from '../views/DinoListView.vue'
import SingleDinoView from '@/views/SingleDinoView.vue'
import HomeView from '@/views/HomeView.vue'
import CategoryListView from '@/views/CategoryListView.vue'
import SingleCategoryView from '@/views/SingleCategoryView.vue'
import AlimentationListView from '@/views/AlimentationListView.vue'
import SingleAlimentationView from '@/views/SingleAlimentationView.vue'
// import SingleCategoryView from '@/views/SingleCategoryView.vue'
// import AlimentationListView from '@/views/AlimentationListView.vue'
// import SingleAlimentationView from '@/views/SingleAlimentationView.vue'

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
    },
    {
      path: '/categories/',
      name: 'category',
      component: CategoryListView
    },
    {
      path: '/categorie/:id',
      name: 'dinosByCategory',
      component: SingleCategoryView
    },
    {
      path: '/alimentations/',
      name: 'alimentation',
      component: AlimentationListView
    },
    {
      path: '/alimentation/:type',
      name: 'dinosByAlimentation',
      component: SingleAlimentationView
    }



  ],
})

export default router
