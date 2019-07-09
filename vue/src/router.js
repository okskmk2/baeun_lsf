import Vue from 'vue'
import Router from 'vue-router'
import Jobs from './views/Jobs.vue'
import Queues from './views/Queues.vue'
import Hosts from './views/Hosts.vue'
import Users from './views/Users.vue'
import Config from './views/Config.vue'
import Limits from './views/Limits.vue'
import Logs from './views/Logs.vue'
import JobDetail from "./views/JobDetail";

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/',
            redirect: '/Jobs'
        },
        {
            path: '/Jobs',
            name: 'Jobs',
            component: Jobs
        },
        {
            path: '/Job/:jobId',
            name: 'JobDetail',
            component: JobDetail
        },
        {
            path: '/Queues',
            name: 'Queues',
            component: Queues
        },
        {
            path: '/Hosts',
            name: 'Hosts',
            component: Hosts
        },
        {
            path: '/Users',
            name: 'Users',
            component: Users
        },
        {
            path: '/Config',
            name: 'Config',
            component: Config
        },
        {
            path: '/Limits',
            name: 'Limits',
            component: Limits
        },
        {
            path: '/Logs',
            name: 'Logs',
            component: Logs
        },
    ]
})
