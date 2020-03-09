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
            import(/* webpackChunkName: "create-job" */ '../views/jobs/CreateJob.vue'),
    },
    {
        path: 'jobs/:id',
        name: 'view-job',
        component: () =>
            import(/* webpackChunkName: "view-job" */ '../views/jobs/JobView.vue')
    },
    {
        path: 'jobs/:id/edit',
        name: 'edit-job',
        component: () =>
            import(/* webpackChunkName: "edit-job" */ '../views/jobs/EditJob.vue')
    },
]