import Vue from 'vue'
import Router from 'vue-router'
import Profile from './views/Profile.vue'
import Contact from './views/Contact.vue'
import Portfolio from './views/Portfolio.vue'
import Blog from './views/Blog.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/Profile'
    },
    {
      path: '/Profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/Contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/Portfolio',
      name: 'Portfolio',
      component: Portfolio
    },
    {
      path: '/Blog',
      name: 'Blog',
      component: Blog
    }
  ]
})
