<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'jobs'}, label: 'موقعیت‌های شغلی'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">موقعیت‌های شغلی</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <router-link class="uk-button uk-button-default"
                             :to="{name: 'create-job'}">
                    ایجاد
                </router-link>
                <Table
                        :headers="{
                            title:'عنوان',
                            created_at:{
                                label: 'تاریخ ایجاد',
                                value: (item) => {
                                    return gregorianToJalali(item.created_at, 'HH:mm:ss YYYY/MM/DD');
                                },
                            }
                         }"
                        :count="count"
                        :items="jobs"
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
                            delete: {
                                callbackFunction: (item) => {
                                    deletePost(item);
                                },
                                label: 'حذف',
                                icon: 'trash',
                            },
                        }"
                >
                </Table>
                <Pagination
                        :next="next"
                        :previous="previous"
                        name="jobs"
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

    export default {
        name: 'Jobs',
        components: {
            Pagination,
            Breadcrumbs,
            Table
        },
        data: function () {
            return {
                jobs: [],
                count: 0,
                next: null,
                previous: null,
            };
        },
        watch: {
            async $route() {
                await this.getPosts();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getPosts();
            });
        },
        methods: {
            async getPosts() {
                try {
                    const current = parseInt((this.$route.query.page) ? this.$route.query.page : 1, 10);
                    const {data} = await AXIOS.get(`jobs/job-postings/?page=${current}`);
                    this.jobs = data.results;
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
            goToEditPage(item) {
                this.$router.push({name: 'edit-job', params: {id: item.id}});
            },
            goToViewPage(item) {
                this.$router.push({name: 'view-job', params: {id: item.id}});
            },
            deletePost(item) {
                const labels = {
                    ok: 'بله',
                    cancel: 'خیر'
                };
                UIKit.modal.confirm('آیا از حذف اطمینان دارید؟', {labels}).then(async () => {
                    try {
                        await AXIOS.delete(`jobs/job-postings/${item.id}`);
                        const current = parseInt((this.$route.query.page) ? this.$route.query.page : 1, 10);
                        if (current === 1) {
                            await this.getPosts();
                        } else {
                            this.$router.push({name: 'jobs'});
                        }
                    } catch (e) {
                        const error = e.response.data;
                        if (error.detail) {
                            UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                        }
                    }
                }, () => {
                    //Do Nothing
                });
            },
            gregorianToJalali: JalaliDateHelper.gregorianToJalali,
        },
    };
</script>

<style scoped></style>
