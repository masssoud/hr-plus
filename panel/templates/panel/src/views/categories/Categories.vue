<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'categories'}, label: 'دسته‌بندی‌ها'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">دسته‌بندی‌ها</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <router-link class="uk-button uk-button-default"
                             :to="{name: 'create-category'}">
                    ایجاد
                </router-link>
                <Table
                        :headers="{title:'عنوان'}"
                        :count="count"
                        :items="categories"
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
                                    deleteCategory(item);
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
                        name="categories"
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

    export default {
        name: 'Categories',
        components: {
            Pagination,
            Breadcrumbs,
            Table
        },
        data: function () {
            return {
                categories: [],
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
                    const {data} = await AXIOS.get(`jobs/categories/?page=${current}`);
                    this.categories = data.results;
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
                this.$router.push({name: 'edit-category', params: {id: item.id}});
            },
            goToViewPage(item) {
                this.$router.push({name: 'view-category', params: {id: item.id}});
            },
            deleteCategory(item) {
                const labels = {
                    ok: 'بله',
                    cancel: 'خیر'
                };
                UIKit.modal.confirm('آیا از حذف اطمینان دارید؟', {labels}).then(async () => {
                    try {
                        await AXIOS.delete(`jobs/categories/${item.id}`);
                        const current = parseInt((this.$route.query.page) ? this.$route.query.page : 1, 10);
                        if (current === 1) {
                            await this.getPosts();
                        } else {
                            this.$router.push({name: 'categories'});
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
        },
    };
</script>

<style scoped></style>
