<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'applicants'}, label: 'متقاضیان'},
            {to: {name: 'view-applicant', params:{id: item.id}}, label: item.full_name},
            {to: {name: 'edit-applicant', params:{id: item.id}}, label: 'ویرایش'},
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
                <ApplicantForm
                        :info="item"
                        :onSubmit="onSubmit"
                ></ApplicantForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";
    import ApplicantForm from "./ApplicantForm";

    export default {
        name: 'EditApplicant',
        data: function () {
            return {
                item: {
                    id: '',
                    cv: null,
                    job_posting: '',
                    full_name: '',
                    email: '',
                    mobile: '',
                    description: '',
                    status: '',
                    picture: null,
                },
            };
        },
        components: {
            Breadcrumbs,
            ApplicantForm
        },
        watch: {
            async $route() {
                await this.getApplicant();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getApplicant();
            });
        },
        methods: {
            async getApplicant() {
                try {
                    const id = parseInt((this.$route.params.id) ? this.$route.params.id : 0, 10);
                    const {data} = await AXIOS.get(`jobs/applicants/${id}/`);
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
                        const formData = new FormData();
                        formData.append('full_name', data.full_name);
                        if (data.cv) {
                            formData.append('cv', data.cv);
                        }
                        formData.append('job_posting', data.job_posting);
                        formData.append('email', data.email);
                        formData.append('mobile', data.mobile);
                        if (data.picture) {
                            formData.append('picture', data.picture);
                        }
                        formData.append('status', data.status);
                        const response = await AXIOS.patch(`jobs/applicants/${this.item.id}/`, formData);
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
