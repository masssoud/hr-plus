import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import store from './store';
import {categories, jobs, users, profile, applicants} from './routes/index.js';

Vue.use(Router);

const router = new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/login',
            name: 'login',
            // route level code-splitting
            // this generates a separate chunk (login.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () =>
                import(/* webpackChunkName: "login" */ './views/Login.vue')
        },
        {
            path: '/dashboard',
            component: () =>
                import(/* webpackChunkName: "dashboard" */ './views/Dashboard.vue'),
            children: [
                {
                    path: '/',
                    name: 'panel',
                    component: () =>
                        import(/* webpackChunkName: "panel" */ './views/Panel.vue'),
                },
                ...categories,
                ...jobs,
                ...users,
                ...profile,
                ...applicants,
            ],
            meta: {
                authRequired: true
            }
        }
    ]
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.authRequired)) {
        if (!store.state.isAuthenticated) {
            next({
                path: '/login'
            });
        } else {
            next();
        }
    } else {
        if (store.state.isAuthenticated) {
            next({
                path: '/dashboard'
            });
        } else {
            next();
        }
    }
    store.dispatch('emptyErrors');
});

export default router;
