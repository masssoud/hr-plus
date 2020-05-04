<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'users'}, label: 'کاربران'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">کاربران</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <router-link class="uk-button uk-button-default"
                             :to="{name: 'create-user'}">
                    ایجاد
                </router-link>
                <Table
                        :headers="{
                            full_name:'نام کامل',
                            is_staff:{
                                label: 'کارمند',
                                value: (item) => {
                                    return (item.is_staff)? 'بله':'خیر';
                                },
                            },
                            date_joined:{
                                label: 'تاریخ عضویت',
                                value: (item) => {
                                    return gregorianToJalali(item.date_joined, 'HH:mm:ss jYYYY/jMM/jDD');
                                },
                            },
                         }"
                        :count="count"
                        :items="users"
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
                                    deleteUser(item);
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
                        name="users"
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
        name: 'Users',
        components: {
            Pagination,
            Breadcrumbs,
            Table
        },
        data: function () {
            return {
                users: [],
                count: 0,
                next: null,
                previous: null,
            };
        },
        watch: {
            async $route() {
                await this.getUsers();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getUsers();
            });
        },
        methods: {
            async getUsers() {
                try {
                    const current = parseInt((this.$route.query.page) ? this.$route.query.page : 1, 10);
                    const {data} = await AXIOS.get(`users/users/?page=${current}`);
                    this.users = data.results;
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
                this.$router.push({name: 'edit-user', params: {id: item.id}});
            },
            goToViewPage(item) {
                this.$router.push({name: 'view-user', params: {id: item.id}});
            },
            deleteUser(item) {
                const labels = {
                    ok: 'بله',
                    cancel: 'خیر'
                };
                UIKit.modal.confirm('آیا از حذف اطمینان دارید؟', {labels}).then(async () => {
                    try {
                        await AXIOS.delete(`users/users/${item.id}`);
                        const current = parseInt((this.$route.query.page) ? this.$route.query.page : 1, 10);
                        if (current === 1) {
                            await this.getUsers();
                        } else {
                            this.$router.push({name: 'users'});
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
