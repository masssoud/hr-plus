<template>
    <div>
        <Header></Header>
        <div class="uk-section uk-section-small uk-flex uk-flex-middle uk-text-center"
             style="min-height: calc((100vh - 80px));">
            <div class="uk-width-3-5 uk-margin-auto">
                <div class="uk-container">
                    <ValidationObserver ref="form" v-slot="{ invalid }">
                        <form @submit.prevent="onSubmit">
                            <fieldset class="uk-fieldset">
                                <legend class="uk-legend">ورود</legend>
                                <div class="uk-margin">
                                    <ValidationProvider name="نام کاربری" vid="username" rules="required"
                                                        v-slot="{ errors }">
                                        <div class="uk-inline uk-width-3-4">
                                            <span class="uk-form-icon" uk-icon="icon: user"></span>
                                            <input v-model="username"
                                                   class="uk-input"
                                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                                   type="text" placeholder="نام کاربری">
                                        </div>
                                        <div class="uk-inline uk-width-3-4" v-if="errors.length>0">
                                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                                {{ error }}
                                            </div>
                                        </div>
                                    </ValidationProvider>
                                </div>
                                <div class="uk-margin">
                                    <ValidationProvider name="کلمه عبور" vid="password" rules="required"
                                                        v-slot="{ errors }">
                                        <div class="uk-inline uk-width-3-4">
                                            <span class="uk-form-icon" uk-icon="icon: lock"></span>
                                            <input v-model="password"
                                                   class="uk-input"
                                                   v-bind:class="{ 'uk-form-danger': (errors.length>0) }"
                                                   type="password" placeholder="کلمه عبور">
                                        </div>
                                        <div class="uk-inline uk-width-3-4" v-if="errors.length>0">
                                            <div class="uk-text-danger" v-for="(error, index) in errors" :key="index">
                                                {{ error }}
                                            </div>
                                        </div>
                                    </ValidationProvider>
                                </div>
                                <div class="uk-margin">
                                    <button type="submit" class="uk-button uk-button-primary uk-width-3-4"
                                            :disabled="invalid">ورود
                                    </button>
                                </div>
                            </fieldset>
                        </form>
                    </ValidationObserver>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import {mapState} from 'vuex';
    import {extend} from 'vee-validate';
    import Header from '../components/Header';

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
        name: 'Home',
        components: {
            Header,
        },
        data: function () {
            return {
                username: '',
                password: ''
            };
        },
        watch: {
            errors: {
                handler: function (errorBag) {
                    if (errorBag.username) {
                        this.$refs.form.setErrors({
                            username: errorBag.username
                        });
                    }
                    if (errorBag.password) {
                        this.$refs.form.setErrors({
                            password: errorBag.password
                        });
                    }
                },
                deep: true
            },
        },
        computed: {
            ...mapState(['errors', 'errorMessage'])
        },
        methods: {
            onSubmit() {
                if (!this.invalid) {
                    this.$store.dispatch('userLogin', {
                        username: this.username,
                        password: this.password
                    });
                }
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">

</style>