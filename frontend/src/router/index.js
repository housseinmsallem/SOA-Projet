import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: DashboardView,
      meta: { title: 'Tableau de Bord' }
    },
    {
      path: '/statistics',
      name: 'statistics',
      component: () => import('../views/DashboardView.vue'), // Placeholder reuse
      meta: { title: 'Statistiques' }
    },
    // Add other routes as placeholders for now
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: DashboardView, // Fallback to dashboard for now or 404
      meta: { title: 'Page' }
    }
  ],
})

export default router
