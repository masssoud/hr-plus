export default [
    {
        path: 'users',
        name: 'users',
        component: () =>
            import(/* webpackChunkName: "users" */ '../views/users/Users.vue'),
    },
    {
        path: 'users/create',
        name: 'create-user',
        component: () =>
            import(/* webpackChunkName: "users" */ '../views/users/CreateUser.vue'),
    },
    {
        path: 'users/:id',
        name: 'view-user',
        component: () => import('../views/users/UserView.vue')
    },
    {
        path: 'users/:id/edit',
        name: 'edit-user',
        component: () => import('../views/users/EditUser.vue')
    },
]