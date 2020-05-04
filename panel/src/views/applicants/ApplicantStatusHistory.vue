<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'applicants'}, label: 'متقاضیان'},
            {to: {name: 'view-applicant', params:{id: item.id}}, label: item.full_name},
            {to: {name: 'applicant-status-history', params:{id: item.id}}, label: 'تایم‌لاین تغییرات وضعیت'},
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
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <div id="timeline">
                    <!-- Timeline Item, copy from here to create various boxes -->
                    <div class="timeline-item" v-for="(status, index) in history"
                         :key="`status-history-${status.id}`">
                        <!--Icon inside the circle-->
                        <div class="timeline-icon">
                            <span uk-icon="icon: check; ratio: 1.5"></span>
                        </div>
                        <!-- Content from timeline box and position (right or left)-->
                        <div
                                class="timeline-content"
                                v-bind:class="{ 'right': (index % 2 === 0), 'left': (index % 2 === 1) }"
                        >
                            <h2>
                                {{applicationStatuses[status.status] ? applicationStatuses[status.status] : 'نامعلوم'}}
                            </h2>
                            <p>
                                <span class="uk-text-muted">
                                    تاریخ:
                                    {{ gregorianToJalali(status.created_at, 'HH:mm:ss jYYYY/jMM/jDD') }}
                                </span>
                                <br>
                                <span class="uk-text-muted">
                                    کاربر:
                                    {{ (status.user_full_name) ? status.user_full_name : 'سیستم' }}
                                </span>
                            </p>
                        </div>
                    </div>
                </div>
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
        name: 'ApplicantStatusHistory',
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
                history: [],
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
                    const history = await AXIOS.get(`jobs/applicants/${id}/history/`);
                    this.history = history.data;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            gregorianToJalali: JalaliDateHelper.gregorianToJalali,
        },
    };
</script>

<style lang="scss" scoped>
    @import "../../assets/timeline/timeline";
</style>
