<template>
    <ValidationObserver ref="form" v-slot="{ invalid }">
        <form @submit.prevent="ownOnSubmit" class="uk-form-stacked">
            <fieldset class="uk-fieldset">
                <div class="uk-grid-match" uk-grid>
                    <div class="uk-width-1-2@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="نام و نام خانوادگی" vid="full_name" rules="required"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    نام و نام خانوادگی
                                </label>
                                <div class="uk-form-controls">
                                    <input v-model="full_name"
                                           class="uk-input"
                                           v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                           type="text" placeholder="نام و نام خانوادگی">
                                </div>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                    <div class="uk-width-1-2@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="آدرس ایمیل" vid="email" rules="required"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    آدرس ایمیل
                                </label>
                                <div class="uk-form-controls">
                                    <input v-model="email"
                                           class="uk-input"
                                           v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                           type="text" placeholder="آدرس ایمیل">
                                </div>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                    <div class="uk-width-1-2@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="شماره موبایل" vid="mobile" rules="required"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    شماره موبایل
                                </label>
                                <div class="uk-form-controls">
                                    <input v-model="mobile"
                                           class="uk-input"
                                           v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                           type="text" placeholder="شماره موبایل">
                                </div>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                    <div class="uk-width-1-2@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="موقعیت شغلی" vid="job_posting" rules="required"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    موقعیت شغلی
                                </label>
                                <div class="uk-form-controls">
                                    <select v-model="job_posting" class="uk-select">
                                        <option v-for="job in jobs" :key="`job-posting-${job.id}`"
                                                :value="job.id">
                                            {{job.title}}
                                        </option>
                                    </select>
                                </div>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                    <div class="uk-width-1-2@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="تصویر" vid="picture" rules=""
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    تصویر
                                </label>
                                <div uk-form-custom>
                                    <input type="file" @change="onPictureChange">
                                    <button class="uk-button uk-button-default" type="button" tabindex="-1">تصویر
                                    </button>
                                </div>
                                <div class="uk-margin-top" v-if="id && picture">
                                    <img :src="picture" width="200">
                                </div>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                    <div class="uk-width-1-2@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="رزومه" vid="cv" rules="required"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    رزومه
                                </label>
                                <div uk-form-custom>
                                    <input type="file" @change="onCVChange">
                                    <button class="uk-button uk-button-default" type="button" tabindex="-1">رزومه
                                    </button>
                                </div>
                                <div class="uk-margin-top" v-if="id && cv">
                                    <a class="uk-button uk-button-default" @click="showCV">
                                        مشاهده فایل رزومه
                                    </a>
                                </div>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                    <div v-if="id" class="uk-width-1-2@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="وضعیت" vid="status" rules="required"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    وضعیت
                                </label>
                                <div class="uk-form-controls">
                                    <select v-model="status" class="uk-select">
                                        <option v-for="(status, key) in applicationStatuses" :key="`status-${key}`"
                                                :value="key">
                                            {{status}}
                                        </option>
                                    </select>
                                </div>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                    <div class="uk-width-1-1@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="توضیحات" vid="description"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    توضیحات
                                </label>
                                <ckeditor
                                        :editor="editor"
                                        v-model="description"
                                        class="uk-textarea"
                                        v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                        rows="5"
                                        placeholder="توضیحات"
                                        :config="editorConfig"></ckeditor>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
                </div>
                    <div id="cv-modal" uk-modal>
                        <div class="uk-modal-dialog uk-width-1-1 uk-height-1-1">
                            <button class="uk-modal-close-outside" type="button" uk-close></button>
                            <iframe class="uk-width-1-1 uk-height-1-1" :src="cv" frameborder="0"></iframe>
                        </div>
                    </div>
                <div class="uk-margin">
                    <button type="submit" class="uk-button uk-button-primary"
                            :disabled="invalid">ثبت
                    </button>
                </div>
            </fieldset>
        </form>
    </ValidationObserver>
</template>

<script>
    import {extend} from 'vee-validate';
    import UIKit from 'uikit';
    import {mapState} from 'vuex';
    import AXIOS from '../../common/http-common';
    import ClassicEditor from 'hd-my-ckeditor-custom-build';

    extend('required', {
        validate(value) {
            return {
                required: true,
                valid: ['', null, undefined].indexOf(value) === -1
            };
        },
        computesRequired: true
    });

    export default {
        name: "ApplicantForm",
        props: ['info', 'onSubmit'],
        data: function () {
            return {
                editor: ClassicEditor,
                editorConfig: {
                    language: 'fa',
                    toolbar: {
                        items: [
                            'heading',
                            '|',
                            'bold',
                            'italic',
                            'link',
                            'bulletedList',
                            'numberedList',
                            '|',
                            'indent',
                            'outdent',
                            '|',
                            'blockQuote',
                            'insertTable',
                            'alignment',
                            'undo',
                            'redo'
                        ]
                    },
                    table: {
                        contentToolbar: [
                            'tableColumn',
                            'tableRow',
                            'mergeTableCells'
                        ]
                    },
                },
                id: this.info.id ?? '',
                cv: this.info.cv ?? null,
                cvData: null,
                job_posting: this.info.job_posting ?? '',
                full_name: this.info.full_name ?? '',
                email: this.info.email ?? '',
                mobile: this.info.mobile ?? '',
                description: this.info.description ?? '',
                status: this.info.status ?? '',
                picture: this.info.picture ?? null,
                pictureData: null,
                jobs: [],
            }
        },
        watch: {
            async $route() {
                await this.getJobs();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getJobs();
            });
        },
        computed: {
            ...mapState(['applicationStatuses', 'errors', 'errorMessage'])
        },
        methods: {
            onPictureChange(e) {
                const files = e.target.files || e.dataTransfer.files;
                if (files.length > 0) {
                    this.pictureData = files[0];
                }
                if (this.pictureData) {
                    this.$refs.form.setErrors({
                        picture: []
                    });
                }
            },
            onCVChange(e) {
                const files = e.target.files || e.dataTransfer.files;
                if (files.length > 0) {
                    this.cvData = files[0];
                }
                if (this.cvData) {
                    this.$refs.form.setErrors({
                        cv: []
                    });
                }
            },
            async getJobs() {
                try {
                    const {data} = await AXIOS.get(`jobs/job-postings/all`);
                    this.jobs = data;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            showCV() {
                UIKit.modal('#cv-modal').show();
            },
            async ownOnSubmit() {
                const formData = {
                    invalid: this.invalid,
                    cv: this.cvData,
                    job_posting: this.job_posting,
                    full_name: this.full_name,
                    email: this.email,
                    mobile: this.mobile,
                    description: this.description,
                    status: this.status,
                    picture: this.pictureData,
                };
                try {
                    const response = await this.onSubmit(formData);
                    this.$router.push({name: 'view-applicant', params: {id: response.id}});
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    } else if (error.constructor === ({}).constructor) {
                        for (const index of Object.keys(formData)) {
                            if (error[index]) {
                                this.$refs.form.setErrors({
                                    [index]: error[index]
                                });
                            }
                        }
                    }
                }
            }
        },

    }
</script>

<style scoped>

</style>