<template>
    <ValidationObserver ref="form" v-slot="{ invalid }">
        <form @submit.prevent="ownOnSubmit" class="uk-form-stacked">
            <fieldset class="uk-fieldset">
                <div class="uk-margin">
                    <ValidationProvider name="نام" vid="first_name" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            نام
                        </label>
                        <div class="uk-form-controls">
                            <input v-model="first_name"
                                   class="uk-input"
                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                   type="text" placeholder="نام">
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="نام خانوادگی" vid="last_name" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            نام خانوادگی
                        </label>
                        <div class="uk-form-controls">
                            <input v-model="last_name"
                                   class="uk-input"
                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                   type="text" placeholder="نام خانوادگی">
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="نام کاربری" vid="username" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            نام کاربری
                        </label>
                        <div class="uk-form-controls">
                            <input v-model="username"
                                   class="uk-input"
                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                   type="text" placeholder="نام کاربری">
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="آدرس ایمیل" vid="email" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            آدرس ایمیل
                        </label>
                        <div class="uk-form-controls">
                            <input v-model="email"
                                   class="uk-input"
                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                   type="email" placeholder="آدرس ایمیل">
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin" v-if="id">
                    <a class="uk-button uk-button-default" @click="showPasswordField">
                        <span v-if="!show_password_field">تغییر کلمه عبور</span>
                        <span v-if="show_password_field">عدم تغییر کلمه عبور</span>
                    </a>
                </div>
                <div class="uk-margin" v-if="show_password_field">
                    <ValidationProvider name="گذرواژه" vid="password" :rules="(id === '')? 'required':''"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            گذرواژه
                        </label>
                        <div class="uk-form-controls">
                            <input v-model="password"
                                   class="uk-input"
                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                   type="password" placeholder="گذرواژه">
                        </div>
                        <div v-if="errors.length>0">
                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                {{ error }}
                            </div>
                        </div>
                    </ValidationProvider>
                </div>
                <div class="uk-margin">
                    <ValidationProvider name="آیا کاربر کارمند است؟" vid="is_staff" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            آیا کاربر کارمند است؟
                        </label>
                        <div class="uk-form-controls">
                            <select v-model="is_staff" class="uk-select">
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
                    <ValidationProvider name="آیا کاربر فعال است؟" vid="is_active" rules="required"
                                        v-slot="{ errors }">
                        <label
                                class="uk-form-label"
                                v-bind:class="{ 'uk-text-danger': (errors.length>0) }"
                        >
                            آیا کاربر فعال است؟
                        </label>
                        <div class="uk-form-controls">
                            <select v-model="is_active" class="uk-select">
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
        name: "UserForm",
        props: ['info', 'onSubmit'],
        data: function () {
            return {
                id: this.info.id ?? '',
                first_name: this.info.first_name ?? '',
                last_name: this.info.last_name ?? '',
                password: '',
                username: this.info.username ?? '',
                email: this.info.email ?? '',
                is_staff: (this.info.is_staff) ? '1' : '0',
                is_active: (this.info.is_active) ? '1' : '0',
                show_password_field: (!this.info.id),
            }
        },
        methods: {
            showPasswordField() {
                this.show_password_field = !this.show_password_field;
                if (!this.show_password_field) {
                    this.password = ''
                }
            },
            async ownOnSubmit() {
                const formData = {
                    invalid: this.invalid,
                    first_name: this.first_name,
                    last_name: this.last_name,
                    username: this.username,
                    email: this.email,
                    password: this.password,
                    is_staff: this.is_staff === '1',
                    is_active: this.is_active === '1',
                };
                try {
                    const response = await this.onSubmit(formData);
                    this.$router.push({name: 'view-user', params: {id: response.id}});
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