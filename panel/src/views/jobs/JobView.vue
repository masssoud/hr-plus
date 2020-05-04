<template>
    <div v-if="item.id">
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
            {to: {name: 'jobs'}, label: 'موقعیت‌های شغلی'},
            {to: {name: 'view-job', params:{id: item.id}}, label: item.title},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">{{ item.title }}</h3>
                    </div>
                    <div class="uk-width-auto">
                        <router-link class="uk-button uk-button-default"
                                     :to="{name: 'applicants', query:{jobPosting: item.id}}">
                            متقاضیان
                        </router-link>
                        <router-link class="uk-button uk-button-default"
                                     :to="{name: 'edit-job', params:{id: item.id}}">
                            ویرایش
                        </router-link>
                        <button class="uk-button uk-button-danger" @click="deletePost()">حذف</button>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <dl class="uk-description-list">
                    <div class="uk-grid-match" uk-grid>
                        <div class="uk-width-1-2@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>شناسه</dt>
                                <dd>{{ item.id }}</dd>
                            </div>
                        </div>
                        <div class="uk-width-1-2@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>عنوان</dt>
                                <dd>{{ item.title }}</dd>

                            </div>
                        </div>
                        <div class="uk-width-1-2@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>دسته‌بندی</dt>
                                <dd>{{ item.category_title }}</dd>

                            </div>
                        </div>
                        <div class="uk-width-1-2@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>آیا موقعیت باز است؟</dt>
                                <dd>{{ (item.is_open)? 'بله':'خیر' }}</dd>

                            </div>
                        </div>
                        <div class="uk-width-1-1@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>توضیحات</dt>
                                <dd v-html="item.description"></dd>

                            </div>
                        </div>
                        <div class="uk-width-1-1@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>صلاحیت‌ها</dt>
                                <dd v-html="item.qualifications"></dd>

                            </div>
                        </div>
                        <div class="uk-width-1-1@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>موارد مورد نیاز</dt>
                                <dd v-html="item.requirements"></dd>

                            </div>
                        </div>
                        <div class="uk-width-1-1@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>مواردی که داشتن آنها خوب است</dt>
                                <dd v-html="item.good_to_have"></dd>

                            </div>
                        </div>
                        <div class="uk-width-1-1@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>مزایا</dt>
                                <dd v-html="item.benefits"></dd>

                            </div>
                        </div>
                        <div class="uk-width-1-2@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>زمان ایجاد</dt>
                                <dd>{{ gregorianToJalali(item.created_at, 'HH:mm:ss jYYYY/jMM/jDD') }}</dd>

                            </div>
                        </div>
                        <div class="uk-width-1-2@m uk-grid-item-match ">
                            <div class="uk-card uk-card-default uk-card-body uk-box-shadow-small">
                                <dt>زمان آخرین ویرایش</dt>
                                <dd>{{ gregorianToJalali(item.updated_at, 'HH:mm:ss jYYYY/jMM/jDD') }}</dd>
                            </div>
                        </div>
                    </div>
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
        name: 'JobView',
        data: function () {
            return {
                item: {
                    id: null,
                    title: null,
                    description: null,
                    is_open: null,
                    qualifications: null,
                    requirements: null,
                    good_to_have: null,
                    benefits: null,
                    created_at: null,
                    updated_at: null,
                    category: null,
                    category_title: null,
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
                    const {data} = await AXIOS.get(`jobs/job-postings/${id}/`);
                    this.item = data;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            deletePost() {
                const labels = {
                    ok: 'بله',
                    cancel: 'خیر'
                };
                UIKit.modal.confirm('آیا از حذف اطمینان دارید؟', {labels}).then(async () => {
                    try {
                        await AXIOS.delete(`jobs/job-postings/${this.item.id}`);
                        this.$router.push({name: 'jobs'});
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
