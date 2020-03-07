<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'profile'}, label: 'پروفایل'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">پروفایل</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <dl class="uk-description-list">
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
                </dl>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";

    export default {
        name: 'Profile',
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
                    const {data} = await AXIOS.get(`users/users/current-user/`);
                    this.item = data;
                    this.item.category_id = data.category;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
        },
    };
</script>

<style scoped></style>
