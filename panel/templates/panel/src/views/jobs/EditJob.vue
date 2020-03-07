<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'jobs'}, label: 'موقعیت‌های شغلی'},
            {to: {name: 'view-job', params:{id: item.id}}, label: item.title},
            {to: {name: 'edit-job', params:{id: item.id}}, label: 'ویرایش'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">ویرایش</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <JobForm
                        :info="item"
                        :onSubmit="onSubmit"
                ></JobForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";
    import JobForm from "./JobForm";

    export default {
        name: 'EditJob',
        data: function () {
            return {
                item: {
                    id: null,
                    title: null,
                    description: null,
                    is_open: null,
                    qualifications: null,
                    good_to_have: null,
                    benefits: null,
                    created_at: null,
                    updated_at: null,
                    category: null,
                },
            };
        },
        components: {
            Breadcrumbs,
            JobForm
        },
        watch: {
            async $route() {
                await this.getPost();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getPost();
            });
        },
        methods: {
            async getPost() {
                try {
                    const id = parseInt((this.$route.params.id) ? this.$route.params.id : 0, 10);
                    const {data} = await AXIOS.get(`jobs/job-postings/${id}/`);
                    this.item = data;
                    this.item.category_id = data.category;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            async onSubmit(data) {
                if (!data.invalid) {
                    try {
                        const response = await AXIOS.put(`jobs/job-postings/${this.item.id}/`,
                            {
                                title: data.title,
                                description: data.description,
                                is_open: data.is_open,
                                qualifications: data.qualifications,
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
