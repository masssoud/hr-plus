<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'applicants'}, label: 'متقاضیان'},
            {to: {name: 'create-applicant'}, label: 'ایجاد متقاضی'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">ایجاد متقاضی</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <ApplicantForm
                        :info="{}"
                        :onSubmit="onSubmit"
                ></ApplicantForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import ApplicantForm from "./ApplicantForm";

    export default {
        name: 'CreateApplicant',
        components: {
            Breadcrumbs,
            ApplicantForm
        },
        methods: {
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
                        const response = await AXIOS.post(`jobs/applicants/`, formData);
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
