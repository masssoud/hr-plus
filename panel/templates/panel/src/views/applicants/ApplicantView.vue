<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'applicants'}, label: 'متقاضیان'},
            {to: {name: 'view-applicant', params:{id: item.id}}, label: item.full_name},
        ]"></Breadcrumbs>
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
                                    <img @click="showPicture" v-if="item.picture" class="avatar" :src="item.picture"
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
                                        فایل رزومه
                                    </a>
                                </dd>
                            </div>
                        </div>
                        <div class="uk-width-1-2@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>وضعیت</dt>
                                <dd>
                                    {{
                                    applicationStatuses[item.status] ? applicationStatuses[item.status]:'نامعلوم'
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
                </dl>
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
