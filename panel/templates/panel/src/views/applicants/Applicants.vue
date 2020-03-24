<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'applicants'}, label: 'متقاضیان'},
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
                    <div class="">
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
                <div class="draggable-container">
                    <div
                            v-for="(group, groupIndex) in groups"
                            :key="`group-${group.id}`"
                            class="uk-width-1-4 draggable-group"
                    >
                        <h5 class="draggable-group-title">{{ group.name }} <span>{{ `${group.count} مورد` }}</span></h5>
                        <draggable
                                :list="groups[groupIndex].items"
                                group="people"
                                @change="movedApplicant(group.id, $event)"
                        >
                            <div
                                    class="draggable-group-item"
                                    v-for="item in group.items"
                                    :key="`applicant-${item.id}`"
                            >
                                <p
                                        class="uk-margin-remove"
                                        @click="goToViewPage(item)"
                                >
                                    {{ item.full_name }}
                                </p>
                                <router-link
                                        class="draggable-group-item-edit"
                                        :to="{name: 'edit-applicant', params: {id: item.id}}">
                                    <span uk-icon="icon: pencil"></span>
                                </router-link>
                            </div>
                            <div
                                    v-if="group.next !== null"
                                    slot="footer"
                                    role="group"
                                    aria-label="Basic example"
                                    key="footer"
                            >
                                <a @click="moreApplicants(group)"
                                   class="uk-button uk-width-1-1 uk-button-default">
                                    بیشتر
                                    <div v-if="group.loading" uk-spinner="ratio: 0.5"></div>
                                </a>
                            </div>
                        </draggable>
                    </div>
                </div>
            </div>
        </div>
        <div v-if="loading" class="uk-overlay-primary uk-position-cover"></div>
        <div v-if="loading" class="uk-overlay uk-position-center uk-light">
            <div uk-spinner="ratio: 4"></div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";
    import JalaliDateHelper from "../../helpers/jalali_date.js";
    import {mapState} from 'vuex';
    import draggable from 'vuedraggable';

    export default {
        name: 'Applicants',
        components: {
            Breadcrumbs,
            draggable
        },
        data: function () {
            return {
                loading: false,
                groups: [],
                selectedFilters: {
                    job: parseInt((this.$route.query.jobPosting) ? this.$route.query.jobPosting : 0, 0),
                },
                jobs: [],

            };
        },
        watch: {
            async $route() {
                this.selectedFilters = {
                    job: parseInt((this.$route.query.jobPosting) ? this.$route.query.jobPosting : 0, 0),
                };
                this.groups = [];
                this.initiate();
                await this.getApplicants();
            }
        },
        computed: {
            ...mapState(['applicationStatuses', 'errors', 'errorMessage'])
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getJobs();
                this.initiate();
                await this.getApplicants();
            });
        },
        methods: {
            initiate() {
                const statuses = Object.keys(this.applicationStatuses);
                for (let index = 0; index < statuses.length; index++) {
                    const group = {
                        id: statuses[index],
                        name: this.applicationStatuses[statuses[index]],
                        items: [],
                        count: 0,
                        current: 0,
                        loading: false,
                        next: null,
                        previous: null,
                    };
                    this.groups.push(group);
                }
            },
            async moreApplicants(group) {
                await this.getApplicants((group.current + 1), group.id);
            },
            async getApplicants(page = 1, status = undefined) {
                try {
                    const jobPosting = parseInt((this.$route.query.jobPosting) ? this.$route.query.jobPosting : 0, 0);
                    let queryParam = `page=${page}`;
                    if (jobPosting !== 0) {
                        queryParam += `&job_posting=${jobPosting}`;
                    }
                    if (status === undefined) {
                        const statuses = Object.keys(this.applicationStatuses);
                        for (let index = 0; index < statuses.length; index++) {
                            queryParam += `&status=${statuses[index]}`;
                            const groupIndex = this.groups.findIndex(group => group.id === statuses[index]);
                            if (groupIndex >= 0) {
                                this.groups[groupIndex].loading = true;
                                const {data} = await AXIOS.get(`jobs/applicants/?${queryParam}`);
                                this.addDataToGroup(data, groupIndex, page);
                            }
                        }
                    } else {
                        queryParam += `&status=${status}`;
                        const groupIndex = this.groups.findIndex(group => group.id === status);
                        if (groupIndex >= 0) {
                            this.groups[groupIndex].loading = true;
                            const {data} = await AXIOS.get(`jobs/applicants/?${queryParam}`);
                            this.addDataToGroup(data, groupIndex, page);
                        }
                    }
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            addDataToGroup(data, groupIndex, current) {
                this.groups[groupIndex].count = data.count;
                this.groups[groupIndex].next = data.next;
                this.groups[groupIndex].previous = data.previous;
                this.groups[groupIndex].current = current;
                this.groups[groupIndex].loading = false;
                data.results.forEach((element) => {
                    this.groups[groupIndex].items.push(element);
                });
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
            goToViewPage(item) {
                this.$router.push({name: 'view-applicant', params: {id: item.id}});
            },
            filter() {
                const query = {};
                if (this.selectedFilters.job !== 0) {
                    query['jobPosting'] = this.selectedFilters.job;
                }
                this.$router.push({name: 'applicants', query});
            },
            gregorianToJalali: JalaliDateHelper.gregorianToJalali,
            async movedApplicant(id, evt) {
                this.loading = true;
                try {
                    if (evt.added) {
                        const applicant = evt.added.element;
                        await AXIOS.patch(`jobs/applicants/${applicant.id}/`,
                            {status: id});
                    }
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
                this.loading = false;
            }
        },
    };
</script>

<style scoped lang="less">
    .draggable-container {
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
        white-space: nowrap;
        margin-top: 8px;
        overflow-x: auto;
        overflow-y: hidden;

        .draggable-group {
            border: #dadbde 2px solid;
            background: #ebecf0;
            border-radius: 5px;
            margin: 0 4px 8px;
            height: 100%;
            display: inline-block;
            vertical-align: top;
            white-space: nowrap;

            .draggable-group-title {
                padding: 4px;
                position: relative;

                span {
                    position: absolute;
                    top: 0;
                    right: 0;
                    margin: 4px;
                    border: #0f0f0f solid 1px;
                    border-radius: 5px;
                    padding: 2px;
                    font-size: 10px;
                    opacity: 0.8;
                }
            }

            .draggable-group-item {
                position: relative;
                background: #fff;
                color: #000;
                margin: 3px;
                padding: 4px;
                border-radius: 5px;
                cursor: pointer;
                max-width: 100%;
                white-space: initial;
                word-wrap: break-word;

                .draggable-group-item-edit {
                    position: absolute;
                    top: 0;
                    right: 0;
                    color: #000;
                    border: #0f0f0f solid 1px;
                    border-radius: 5px;
                    margin: 2px;
                    opacity: 0.25;
                }

                &:hover {
                    .draggable-group-item-edit {
                        opacity: 0.5;

                        &:hover {
                            opacity: 1;
                        }
                    }
                }
            }
        }
    }
</style>

