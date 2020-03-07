<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'categories'}, label: 'دسته‌بندی‌ها'},
            {to: {name: 'create-category'}, label: 'ایجاد دسته‌بندی'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">ایجاد دسته‌بندی</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <CategoryForm
                        :info="{}"
                        :onSubmit="onSubmit"
                ></CategoryForm>
            </div>
        </div>
    </div>
</template>

<script>
    import AXIOS from '../../common/http-common';
    import Breadcrumbs from "../../components/Breadcrumbs";
    import CategoryForm from "./CategoryForm";

    export default {
        name: 'CreateCategory',
        components: {
            Breadcrumbs,
            CategoryForm
        },
        methods: {
            async onSubmit(data) {
                if (!data.invalid) {
                    try {
                        const response = await AXIOS.post(`jobs/categories/`,
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
