<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'users'}, label: 'کاربران'},
            {to: {name: 'view-user', params:{id: item.id}}, label: item.full_name},
            {to: {name: 'edit-user', params:{id: item.id}}, label: 'ویرایش'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">ویرایش</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <UserForm
                        :info="item"
                        :onSubmit="onSubmit"
                ></UserForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";
    import UserForm from "./UserForm";

    export default {
        name: 'EditUser',
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
            Breadcrumbs,
            UserForm
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
                    this.item.category_id = data.category;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            async onSubmit(data) {
                if (!data.invalid) {
                    try {
                        const values = {
                            first_name: data.first_name,
                            last_name: data.last_name,
                            username: data.username,
                            email: data.email,
                            is_staff: data.is_staff,
                            is_active: data.is_active,
                        };
                        if (data.password) {
                            values.password = data.password;
                        }
                        const response = await AXIOS.patch(`users/users/${this.item.id}/`, values);
                        return response.data;
                    } catch (e) {
                        return Promise.reject(e);
                    }
                }
            }
        },
    };
</script>

<style scoped></style>
