export default [
    {
        path: 'applicants',
        name: 'applicants',
        component: () =>
            import(/* webpackChunkName: "applicants" */ '../views/applicants/Applicants.vue'),
    },
    {
        path: 'applicants/table-view',
        name: 'applicants-table-view',
        component: () =>
            import(/* webpackChunkName: "applicants-table-view" */ '../views/applicants/ApplicantsTableView.vue'),
    },
    {
        path: 'applicants/create',
        name: 'create-applicant',
        component: () =>
            import(/* webpackChunkName: "create-applicant" */ '../views/applicants/CreateApplicant.vue'),
    },
    {
        path: 'applicants/:id',
        name: 'view-applicant',
        component: () =>
            import(/* webpackChunkName: "view-applicant" */ '../views/applicants/ApplicantView.vue')
    },
    {
        path: 'applicants/:id/edit',
        name: 'edit-applicant',
        component: () =>
            import(/* webpackChunkName: "edit-applicant" */ '../views/applicants/EditApplicant.vue')
    },
    {
        path: 'applicants/:id/status-history',
        name: 'applicant-status-history',
        component: () =>
            import(/* webpackChunkName: "applicant-status-history" */ '../views/applicants/ApplicantStatusHistory.vue')
    },
]