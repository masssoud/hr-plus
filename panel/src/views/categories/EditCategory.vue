<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'categories'}, label: 'دسته‌بندی‌ها'},
            {to: {name: 'view-category', params:{id: item.id}}, label: item.title},
            {to: {name: 'edit-category', params:{id: item.id}}, label: 'ویرایش'},
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
                <CategoryForm
                        :info="item"
                        :onSubmit="onSubmit"
                ></CategoryForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import UIKit from "uikit";
    import CategoryForm from "./CategoryForm";

    export default {
        name: 'EditCategory',
        data: function () {
            return {
                item: {
                    id: null,
                    title: null,
                    description: null,
                },
            };
        },
        components: {
            Breadcrumbs,
            CategoryForm
        },
        watch: {
            async $route() {
                await this.getPost();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getPost();
            });
        },
        methods: {
            async getPost() {
                try {
                    const id = parseInt((this.$route.params.id) ? this.$route.params.id : 0, 10);
                    const {data} = await AXIOS.get(`jobs/categories/${id}/`);
                    this.item = data;
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
                        const response = await AXIOS.put(`jobs/categories/${this.item.id}/`,
                            {title: data.title, description: data.description});
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
