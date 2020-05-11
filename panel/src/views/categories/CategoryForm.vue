<template>
    <ValidationObserver ref="form" v-slot="{ invalid }">
        <form @submit.prevent="ownOnSubmit" class="uk-form-stacked">
            <fieldset class="uk-fieldset">
                <div class="uk-grid-match" uk-grid>
                    <div class="uk-width-1-1@m uk-grid-item-match ">
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
                    </div>
                    <div class="uk-width-1-1@m uk-grid-item-match ">
                        <div class="uk-margin">
                            <ValidationProvider name="توضیحات" vid="description"
                                                v-slot="{ errors }">
                                <label
                                        class="uk-form-label"
                                        v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                                >
                                    توضیحات
                                </label>
                                <ckeditor
                                        :editor="editor"
                                        v-model="description"
                                        class="uk-textarea"
                                        v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                        rows="5"
                                        placeholder="توضیحات"
                                        :config="editorConfig"></ckeditor>
                                <div v-if="errors.length>0">
                                    <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                        {{ error }}
                                    </div>
                                </div>
                            </ValidationProvider>
                        </div>
                    </div>
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
    import ClassicEditor from 'ckeditor-custom-build';

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
        name: "CategoryForm",
        props: ['info', 'onSubmit'],
        data: function () {
            return {
                editor: ClassicEditor,
                editorConfig: {
                    language: 'fa',
                    toolbar: {
                        items: [
                            'heading',
                            '|',
                            'bold',
                            'italic',
                            'link',
                            'bulletedList',
                            'numberedList',
                            '|',
                            'indent',
                            'outdent',
                            '|',
                            'blockQuote',
                            'insertTable',
                            'alignment',
                            'undo',
                            'redo'
                        ]
                    },
                    table: {
                        contentToolbar: [
                            'tableColumn',
                            'tableRow',
                            'mergeTableCells'
                        ]
                    },
                },
                title: this.info.title ?? '',
                description: this.info.description ?? '',
            }
        },
        methods: {
            async ownOnSubmit() {
                const formData = {
                    invalid: this.invalid,
                    title: this.title,
                    description: this.description,
                };
                try {
                    const response = await this.onSubmit(formData);
                    this.$router.push({name: 'view-category', params: {id: response.id}});
                } catch (e) {
                    const error = e.response.data;
                    if (error.detail) {
                        UIKit.notification(`<span uk-icon='icon: warning'></span>${error.detail}`, {status: 'danger'});
                    } else if (error.constructor === ({}).constructor) {
                        if (error.title) {
                            this.$refs.form.setErrors({
                                title: error.title
                            });
                        }
                        if (error.description) {
                            this.$refs.form.setErrors({
                                description: error.description
                            });
                        }
                    }
                }
            }
        },

    }
</script>

<style scoped>

</style>