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
            import(/* webpackChunkName: "create-user" */ '../views/users/CreateUser.vue'),
    },
    {
        path: 'users/:id',
        name: 'view-user',
        component: () =>
            import(/* webpackChunkName: "view-user" */ '../views/users/UserView.vue')
    },
    {
        path: 'users/:id/edit',
        name: 'edit-user',
        component: () =>
            import(/* webpackChunkName: "edit-user" */ '../views/users/EditUser.vue')
    },
]