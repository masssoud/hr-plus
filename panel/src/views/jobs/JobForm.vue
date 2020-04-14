<template>
    <ValidationObserver ref="form" v-slot="{ invalid }">
        <form @submit.prevent="ownOnSubmit" class="uk-form-stacked">
            <fieldset class="uk-fieldset">
                <div class="uk-margin">
                    <ValidationProvider name="عنوان" vid="title" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            عنوان
                        </label>
                        <div class="uk-form-controls">
                            <input v-model="title"
                                   class="uk-input"
                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                   type="text" placeholder="عنوان">
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="دسته‌بندی" vid="category_id" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            دسته‌بندی
                        </label>
                        <div class="uk-form-controls">
                            <select v-model="category_id" class="uk-select">
                                <option v-for="category in categories" :key="`category-${category.id}`"
                                        :value="category.id">
                                    {{category.title}}
                                </option>
                            </select>
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="توضیحات" vid="description"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            توضیحات
                        </label>
                        <textarea v-model="description"
                                  class="uk-textarea"
                                  v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                  rows="5"
                                  placeholder="توضیحات"></textarea>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="صلاحیت‌ها" vid="qualifications"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            صلاحیت‌ها
                        </label>
                        <textarea v-model="qualifications"
                                  class="uk-textarea"
                                  v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                  rows="5"
                                  placeholder="صلاحیت‌ها"></textarea>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="موارد مورد نیاز" vid="requirements"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            موارد مورد نیاز
                        </label>
                        <textarea v-model="requirements"
                                  class="uk-textarea"
                                  v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                  rows="5"
                                  placeholder="موارد مورد نیاز"></textarea>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="مواردی که داشتن آنها خوب است" vid="good_to_have"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            مواردی که داشتن آنها خوب است
                        </label>
                        <textarea v-model="good_to_have"
                                  class="uk-textarea"
                                  v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                  rows="5"
                                  placeholder="مواردی که داشتن آنها خوب است"></textarea>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="مزایا" vid="benefits"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            مزایا
                        </label>
                        <textarea v-model="benefits"
                                  class="uk-textarea"
                                  v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                  rows="5"
                                  placeholder="مزایا"></textarea>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="آیا موقعیت باز است؟" vid="is_open" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            آیا موقعیت باز است؟
                        </label>
                        <div class="uk-form-controls">
                            <select v-model="is_open" class="uk-select">
                                <option value="1">بله</option>
                                <option value="0">خیر</option>
                            </select>
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <button type="submit" class="uk-button uk-button-primary"
                            :disabled="invalid">ثبت
                    </button>
                </div>
            </fieldset>
        </form>
    </ValidationObserver>
</template>

<script>
    import {extend} from 'vee-validate';
    import UIKit from 'uikit';
    import AXIOS from '../../common/http-common';

    extend('required', {
        validate(value) {
            return {
                required: true,
                valid: ['', null, undefined].indexOf(value) === -1
            };
        },
        computesRequired: true
    });

    export default {
        name: "JobForm",
        props: ['info', 'onSubmit'],
        data: function () {
            return {
                title: this.info.title ?? '',
                description: this.info.description ?? '',
                is_open: (this.info.is_open) ? '1' : '0',
                qualifications: this.info.qualifications ?? '',
                requirements: this.info.requirements ?? '',
                good_to_have: this.info.good_to_have ?? '',
                benefits: this.info.benefits ?? '',
                category_id: this.info.category_id ?? '',
                categories: [],
            }
        },
        watch: {
            async $route() {
                await this.getCategories();
            }
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getCategories();
            });
        },
        methods: {
            async getCategories() {
                try {
                    const {data} = await AXIOS.get('jobs/categories/all/');
                    this.categories = data;
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    }
                }
            },
            async ownOnSubmit() {
                const formData = {
                    invalid: this.invalid,
                    title: this.title,
                    description: this.description,
                    is_open: this.is_open === '1',
                    requirements: this.requirements,
                    qualifications: this.qualifications,
                    good_to_have: this.good_to_have,
                    benefits: this.benefits,
                    category: this.category_id,
                };
                try {
                    const response = await this.onSubmit(formData);
                    this.$router.push({name: 'view-job', params: {id: response.id}});
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    } else if (error.constructor === ({}).constructor) {
                        for (const index of Object.keys(formData)) {
                            if (error[index]) {
                                this.$refs.form.setErrors({
                                    [index]: error[index]
                                });
                            }
                        }
                    }
                }
            }
        },

    }
</script>

<style scoped>

</style>