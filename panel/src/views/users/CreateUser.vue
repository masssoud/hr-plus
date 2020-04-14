<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'users'}, label: 'کاربران'},
            {to: {name: 'create-user'}, label: 'ایجاد کاربر'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">ایجاد کاربر</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <UserForm
                        :info="{}"
                        :onSubmit="onSubmit"
                ></UserForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UserForm from "./UserForm";

    export default {
        name: 'CreateUser',
        components: {
            Breadcrumbs,
            UserForm
        },
        methods: {
            async onSubmit(data) {
                if (!data.invalid) {
                    try {
                        const response = await AXIOS.post(`users/users/`,
                            {
                                first_name: data.first_name,
                                last_name: data.last_name,
                                username: data.username,
                                email: data.email,
                                is_staff: data.is_staff,
                                is_active: data.is_active,
                                password: data.password,
                            }
                        );
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
