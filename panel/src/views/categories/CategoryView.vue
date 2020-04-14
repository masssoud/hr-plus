<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'categories'}, label: 'دسته‌بندی‌ها'},
            {to: {name: 'view-category', params:{id: item.id}}, label: item.title},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">{{ item.title }}</h3>
                    </div>
                    <div class="uk-width-auto">
                        <router-link class="uk-button uk-button-default"
                                     :to="{name: 'edit-category', params:{id: item.id}}">
                            ویرایش
                        </router-link>
                        <button class="uk-button uk-button-danger" @click="deleteCategory()">حذف</button>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <dl class="uk-description-list">
                    <dt>شناسه</dt>
                    <dd>{{ item.id }}</dd>
                    <dt>عنوان</dt>
                    <dd>{{ item.title }}</dd>
                    <dt>توضیحات</dt>
                    <dd v-html="item.description"></dd>
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
        name: 'CategoryView',
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
            Breadcrumbs
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
            deleteCategory() {
                const labels = {
                    ok: 'بله',
                    cancel: 'خیر'
                };
                UIKit.modal.confirm('آیا از حذف اطمینان دارید؟', {labels}).then(async () => {
                    try {
                        await AXIOS.delete(`jobs/categories/${this.item.id}`);
                        this.$router.push({name: 'categories'});
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
        },
    };
</script>

<style scoped></style>
