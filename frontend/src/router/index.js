import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import LoginView from '../views/LoginView.vue'
import QuestionsView from '../views/QuestionsView.vue'
import RegisterView from '../views/RegisterView.vue'
import SolutionsView from '../views/SolutionsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/questions',
      name: 'questions',
      component: QuestionsView
    },
    {
      path: '/solutions',
      name: 'solutions',
      component: SolutionsView
    }
  ]
})

export default router
