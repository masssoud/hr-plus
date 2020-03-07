<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'users'}, label: 'کاربران'},
            {to: {name: 'view-user', params:{id: item.id}}, label: item.full_name},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">{{ item.full_name }}</h3>
                    </div>
                    <div class="uk-width-auto">
                        <router-link class="uk-button uk-button-default"
                                     :to="{name: 'edit-user', params:{id: item.id}}">
                            ویرایش
                        </router-link>
                        <button class="uk-button uk-button-danger" @click="deleteUser()">حذف</button>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <dl class="uk-description-list">
                    <dt>شناسه</dt>
                    <dd>{{ item.id }}</dd>
                    <hr>
                    <dt>نام</dt>
                    <dd>{{ item.first_name }}</dd>
                    <hr>
                    <dt>نام خانوادگی</dt>
                    <dd>{{ item.last_name }}</dd>
                    <hr>
                    <dt>نام کاربری</dt>
                    <dd>{{ item.username }}</dd>
                    <hr>
                    <dt>آدرس ایمیل</dt>
                    <dd>{{ item.email }}</dd>
                    <hr>
                    <dt>آیا کاربر کارمند است؟</dt>
                    <dd>{{ (item.is_staff) ? 'بله' : 'خیر' }}</dd>
                    <hr>
                    <dt>آیا کاربر فعال است؟</dt>
                    <dd>{{ (item.is_active) ? 'بله' : 'خیر' }}</dd>
                    <hr>
                    <dt>تاریخ عضویت</dt>
                    <dd>{{ (item.date_joined) ? gregorianToJalali(item.date_joined, 'HH:mm:ss YYYY/MM/DD'):'' }}</dd>
                    <hr>
                    <dt>تاریخ آخرین ورود</dt>
                    <dd>{{ (item.last_login) ? gregorianToJalali(item.last_login, 'HH:mm:ss YYYY/MM/DD'):'' }}</dd>
                    <hr>
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

    export default {
        name: 'UserView',
        data: function () {
            return {
                item: {
                    id: null,
                    full_name: null,
                    first_name: null,
                    last_name: null,
                    last_login: null,
                    is_superuser: false,
                    username: null,
                    email: null,
                    is_staff: false,
                    is_active: false,
                    date_joined: null,
                },
            };
        },
        components: {
            Breadcrumbs
        },
        watch: {
            async $route() {
                await this.getUser();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getUser();
            });
        },
        methods: {
            async getUser() {
                try {
                    const id = parseInt((this.$route.params.id) ? this.$route.params.id : 0, 10);
                    const {data} = await AXIOS.get(`users/users/${id}/`);
                    this.item = data;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            deleteUser() {
                const labels = {
                    ok: 'بله',
                    cancel: 'خیر'
                };
                UIKit.modal.confirm('آیا از حذف اطمینان دارید؟', {labels}).then(async () => {
                    try {
                        await AXIOS.delete(`users/users/${this.item.id}`);
                        this.$router.push({name: 'users'});
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
