<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'applicants'}, label: 'متقاضیان'},
            {to: {name: 'view-applicant', params:{id: item.id}}, label: item.full_name},
        ]"></Breadcrumbs>
        <div uk-grid>
            <div class="uk-width-3-4@m">
                <div class="uk-card uk-card-default uk-width-1-1">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <div class="uk-width-expand">
                                <h3 class="uk-card-title uk-margin-remove-bottom">{{ item.full_name }}</h3>
                            </div>
                            <div class="uk-width-auto">
                                <router-link class="uk-button uk-button-default"
                                             :to="{name: 'edit-applicant', params:{id: item.id}}">
                                    ویرایش
                                </router-link>
                                <router-link class="uk-button uk-button-default"
                                             :to="{name: 'applicant-status-history', params:{id: item.id}}">
                                    مشاهده تایم‌لاین تغییرات وضعیت
                                </router-link>
                            </div>
                        </div>
                    </div>
                    <div class="uk-card-body">
                        <dl class="uk-description-list">
                            <div class="uk-grid-match" uk-grid>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>شناسه</dt>
                                        <dd>{{ item.id }}</dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>نام و نام خانوادگی</dt>
                                        <dd>
                                            <img @click="showPicture" v-if="item.picture" class="avatar"
                                                 :src="item.picture"
                                                 :alt="item.full_name">
                                            {{ item.full_name }}
                                        </dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>آدرس ایمیل</dt>
                                        <dd>{{ item.email }}</dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>شماره موبایل</dt>
                                        <dd>{{ item.mobile }}</dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>موقعیت شغلی</dt>
                                        <dd>{{ item.job_posting_title }}</dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>رزومه</dt>
                                        <dd>
                                            <a :href="item.cv" target="_blank" class="uk-button uk-button-default">
                                                دریافت فایل رزومه
                                            </a>
                                            <button class="uk-button uk-button-default" @click="showCV">
                                                مشاهده فایل رزومه
                                            </button>
                                        </dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>وضعیت</dt>
                                        <dd>
                                            {{
                                            applicationStatuses[item.status] ?
                                            applicationStatuses[item.status]:'نامعلوم'
                                            }}
                                        </dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>توضیحات</dt>
                                        <dd v-html="item.description"></dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>زمان ایجاد</dt>
                                        <dd>{{ gregorianToJalali(item.created_at, 'HH:mm:ss YYYY/MM/DD') }}</dd>
                                    </div>
                                </div>
                                <div class="uk-width-1-2@m uk-grid-item-match ">
                                    <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                        <dt>زمان آخرین ویرایش</dt>
                                        <dd>{{ gregorianToJalali(item.updated_at, 'HH:mm:ss YYYY/MM/DD') }}</dd>
                                    </div>
                                </div>
                            </div>
                            <div id="cv-modal" uk-modal>
                                <div class="uk-modal-dialog uk-width-1-1 uk-height-1-1">
                                    <button class="uk-modal-close-outside" type="button" uk-close></button>
                                    <iframe class="uk-width-1-1 uk-height-1-1" :src="item.cv" frameborder="0"></iframe>
                                </div>
                            </div>
                        </dl>
                    </div>
                </div>
            </div>
            <div class="uk-width-1-4@m">
                <ValidationObserver ref="form" v-slot="{ invalid }">
                    <form @submit.prevent="submitComment" class="uk-margin-top">
                        <fieldset class="uk-fieldset">
                            <div class="uk-width-1-1 uk-grid-item-match ">
                                <div class="uk-margin">
                                    <ValidationProvider name="نظر" vid="comment"
                                                        v-slot="{ errors }">
                                                <textarea v-model="comment"
                                                          class="uk-textarea"
                                                          v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                                          rows="5"
                                                          placeholder="نظر"></textarea>
                                        <div v-if="errors.length>0">
                                            <div class="uk-text-danger" v-for="(error, index) in errors"
                                                 :key="index">
                                                {{ error }}
                                            </div>
                                        </div>
                                    </ValidationProvider>
                                    <button type="submit" class="uk-button uk-button-primary uk-width-1-1"
                                            :disabled="invalid">ثبت
                                    </button>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </ValidationObserver>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";
    import JalaliDateHelper from "../../helpers/jalali_date";
    import {mapState} from 'vuex';

    export default {
        name: 'ApplicantView',
        data: function () {
            return {
                item: {
                    id: '',
                    cv: null,
                    job_posting: '',
                    job_posting_title: '',
                    full_name: '',
                    email: '',
                    mobile: '',
                    description: '',
                    status: '',
                    picture: null,
                },
                comment: '',
            };
        },
        components: {
            Breadcrumbs
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
        computed: {
            ...mapState(['applicationStatuses', 'errors', 'errorMessage'])
        },
        methods: {
            async submitComment() {
                try {
                    const formData = new FormData();
                    formData.append('body', this.comment);
                    formData.append('applicant', this.item.id);
                    await AXIOS.post(`jobs/comments/`, formData);
                    this.comment = '';
                    this.$refs.form.setErrors({
                        comment: []
                    });
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    } else if (error.constructor === ({}).constructor) {
                        if (error['body']) {
                            this.$refs.form.setErrors({
                                comment: error['body']
                            });
                        }
                    }
                }
            },
            async getApplicant() {
                try {
                    const id = parseInt((this.$route.params.id) ? this.$route.params.id : 0, 10);
                    const {data} = await AXIOS.get(`jobs/applicants/${id}/`);
                    this.item = data;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            showPicture() {
                UIKit.modal.dialog(`<img src="${this.item.picture}">`);
            },
            showCV() {
                UIKit.modal('#cv-modal').show();
            },
            gregorianToJalali: JalaliDateHelper.gregorianToJalali,
        },
    };
</script>

<style scoped>
    .avatar {
        border-radius: 50%;
        width: 60px;
        height: 60px;
        object-fit: cover;
        cursor: pointer;
    }
</style>
