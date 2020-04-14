<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'jobs'}, label: 'موقعیت‌های شغلی'},
            {to: {name: 'create-job'}, label: 'ایجاد موقعیت شغلی'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">ایجاد موقعیت شغلی</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <JobForm
                        :info="{}"
                        :onSubmit="onSubmit"
                ></JobForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import JobForm from "./JobForm";

    export default {
        name: 'CreateJob',
        components: {
            Breadcrumbs,
            JobForm
        },
        methods: {
            async onSubmit(data) {
                if (!data.invalid) {
                    try {
                        const response = await AXIOS.post(`jobs/job-postings/`,
                            {
                                title: data.title,
                                description: data.description,
                                is_open: data.is_open,
                                qualifications: data.qualifications,
                                requirements: data.requirements,
                                good_to_have: data.good_to_have,
                                benefits: data.benefits,
                                category: data.category,
                            });
                        return response.data;
                    } catch (e) {
                        return Promise.reject(e);
                    }
                }
            }
        },
    };
</script>

<style scoped></style>
