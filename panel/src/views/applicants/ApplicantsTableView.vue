<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'applicants-table-view'}, label: 'متقاضیان'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">متقاضیان</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <router-link class="uk-button uk-button-default"
                             :to="{name: 'create-applicant'}">
                    ایجاد
                </router-link>
                <div class="filters uk-margin-top">
                    <div class="uk-column-1-2@m">
                        <div>
                            <label class="uk-form-label">
                                موقعیت شغلی
                            </label>
                            <div class="uk-form-controls">
                                <select v-model="selectedFilters.job" @change="filter" class="uk-select">
                                    <option value="0">
                                        همه موارد
                                    </option>
                                    <option
                                            v-for="job in jobs"
                                            :key="`jobs-filter-${job.id}`"
                                            :value="job.id"
                                    >
                                        {{job.title}}
                                    </option>
                                </select>
                            </div>
                        </div>
                        <div>
                            <label class="uk-form-label">
                                وضعیت
                            </label>
                            <div class="uk-form-controls">
                                <select v-model="selectedFilters.status" @change="filter" class="uk-select">
                                    <option value="">
                                        همه موارد
                                    </option>
                                    <option
                                            v-for="(status, key) in applicationStatuses"
                                            :key="`statuses-filter-${key}`"
                                            :value="key"
                                    >
                                        {{status}}
                                    </option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="uk-column-1-1">
                        <div>
                            <label class="uk-form-label">
                                نام متقاضی
                            </label>
                            <div class="uk-form-controls">
                                <input v-model="selectedFilters.full_name"
                                       class="uk-input"
                                       v-debounce:1000ms="stoppedTyping"
                                       type="text" placeholder="نام متقاضی">
                            </div>
                        </div>
                    </div>
                </div>
                <div class="uk-flex uk-flex-center uk-margin-top">
                    <div>
                        <div class="uk-button-group">
                            <router-link class="uk-button uk-button-default"
                                         uk-icon="grid"
                                         :activeClass="$route.name === 'applicants' ? 'uk-button-primary':''"
                                         :to="{name: 'applicants'}">
                            </router-link>
                            <router-link class="uk-button uk-button-default"
                                         uk-icon="table"
                                         :activeClass="$route.name === 'applicants-table-view' ? 'uk-button-primary':''"
                                         :to="{name: 'applicants-table-view'}">
                            </router-link>
                        </div>
                    </div>
                </div>
                <Table
                        :headers="{
                            full_name:'نام و نام خانوادگی',
                            status:{
                                label: 'وضعیت',
                                value: (item) => {
                                    return applicationStatuses[item.status] ? applicationStatuses[item.status] : 'نامعلوم';
                                },
                            },
                            job_posting_title:'موقعیت شغلی',
                            created_at:{
                                label: 'تاریخ درخواست',
                                value: (item) => {
                                    return gregorianToJalali(item.created_at, 'HH:mm:ss jYYYY/jMM/jDD');
                                },
                            }
                         }"
                        :count="count"
                        :items="applicants"
                        :actions="{
                            view: {
                                callbackFunction: (item) => {
                                    goToViewPage(item);
                                },
                                label: 'مشاهده',
                                icon: 'info',
                            },
                            edit: {
                                callbackFunction: (item) => {
                                    goToEditPage(item);
                                },
                                label: 'ویرایش',
                                icon: 'pencil',
                            },
                        }"
                >
                </Table>
                <Pagination
                        :next="next"
                        :previous="previous"
                        name="applicants-table-view"
                ></Pagination>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Table from '../../components/Table';
    import Pagination from "../../components/Pagination";
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";
    import JalaliDateHelper from "../../helpers/jalali_date.js";
    import {mapState} from 'vuex';

    export default {
        name: 'ApplicantsTableView',
        components: {
            Pagination,
            Breadcrumbs,
            Table
        },
        data: function () {
            return {
                applicants: [],
                selectedFilters: {
                    job: parseInt((this.$route.query.jobPosting) ? this.$route.query.jobPosting : 0, 0),
                    status: ((this.$route.query.status) ? this.$route.query.status : ''),
                    full_name: ((this.$route.query.fullName) ? this.$route.query.fullName : ''),
                },
                jobs: [],
                count: 0,
                next: null,
                previous: null,
            };
        },
        watch: {
            async $route() {
                this.selectedFilters = {
                    job: parseInt((this.$route.query.jobPosting) ? this.$route.query.jobPosting : 0, 0),
                    status: ((this.$route.query.status) ? this.$route.query.status : ''),
                    full_name: ((this.$route.query.fullName) ? this.$route.query.fullName : ''),
                };
                await this.getApplicants();
            }
        },
        computed: {
            ...mapState(['applicationStatuses', 'errors', 'errorMessage'])
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getJobs();
                await this.getApplicants();
            });
        },
        methods: {
            async getApplicants() {
                try {
                    const current = parseInt((this.$route.query.page) ? this.$route.query.page : 1, 10);
                    const jobPosting = parseInt((this.$route.query.jobPosting) ? this.$route.query.jobPosting : 0, 0);
                    const status = (this.$route.query.status) ? this.$route.query.status : '';
                    const fullName = (this.$route.query.fullName) ? this.$route.query.fullName : '';
                    let queryParam = `page=${current}`;
                    if (jobPosting !== 0) {
                        queryParam += `&job_posting=${jobPosting}`;
                    }
                    if (status !== '') {
                        queryParam += `&status=${status}`;
                    }
                    if (fullName !== '') {
                        queryParam += `&full_name=${fullName}`;
                    }
                    const {data} = await AXIOS.get(`jobs/applicants/?${queryParam}`);
                    this.applicants = data.results;
                    this.count = data.count;
                    this.next = (data.next) ? current + 1 : null;
                    this.previous = (data.previous) ? current - 1 : null;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
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
            goToEditPage(item) {
                this.$router.push({name: 'edit-applicant', params: {id: item.id}});
            },
            goToViewPage(item) {
                this.$router.push({name: 'view-applicant', params: {id: item.id}});
            },
            stoppedTyping() {
                const fullName = (this.$route.query.fullName) ? this.$route.query.fullName : '';
                if (fullName !== this.selectedFilters.full_name) {
                    this.filter();
                }
            },
            filter() {
                const query = {};
                if (this.selectedFilters.job !== 0) {
                    query['jobPosting'] = this.selectedFilters.job;
                }
                if (this.selectedFilters.status !== '') {
                    query['status'] = this.selectedFilters.status;
                }
                if (this.selectedFilters.full_name !== '') {
                    query['fullName'] = this.selectedFilters.full_name;
                }
                this.$router.push({name: 'applicants-table-view', query});
            },
            gregorianToJalali: JalaliDateHelper.gregorianToJalali,
        },
    };
</script>

<style scoped></style>
