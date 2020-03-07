export default [
    {
        path: 'categories',
        name: 'categories',
        component: () =>
            import(/* webpackChunkName: "categories" */ '../views/categories/Categories.vue'),
    },
    {
        path: 'categories/create',
        name: 'create-category',
        component: () =>
            import(/* webpackChunkName: "categories" */ '../views/categories/CreateCategory.vue'),
    },
    {
        path: 'categories/:id',
        name: 'view-category',
        component: () => import('../views/categories/CategoryView.vue')
    },
    {
        path: 'categories/:id/edit',
        name: 'edit-category',
        component: () => import('../views/categories/EditCategory.vue')
    },
]