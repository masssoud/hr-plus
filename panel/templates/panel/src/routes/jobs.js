export default [
    {
        path: 'jobs',
        name: 'jobs',
        component: () =>
            import(/* webpackChunkName: "jobs" */ '../views/jobs/Jobs.vue'),
    },
    {
        path: 'jobs/create',
        name: 'create-job',
        component: () =>
            import(/* webpackChunkName: "jobs" */ '../views/jobs/CreateJob.vue'),
    },
    {
        path: 'jobs/:id',
        name: 'view-job',
        component: () => import('../views/jobs/JobView.vue')
    },
    {
        path: 'jobs/:id/edit',
        name: 'edit-job',
        component: () => import('../views/jobs/EditJob.vue')
    },
]