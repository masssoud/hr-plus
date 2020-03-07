<template>
    <div>
        <nav class="uk-navbar-container uk-navbar-respect" uk-navbar>
            <div class="uk-navbar-left">
                <ul class="uk-navbar-nav">
                    <li class="uk-visible@m">
                        <router-link to="/">
                            <img alt="فناپ پلاس" src="../assets/logo.svg" uk-img>
                        </router-link>
                    </li>
                    <li class="uk-hidden@m">
                        <router-link to="/">
                            <img alt="فناپ پلاس" src="../assets/logo.png" uk-img>
                        </router-link>
                    </li>
                    <li v-if="isAuthenticated" class="uk-hidden@m">
                        <a uk-icon="icon: menu" uk-toggle="target: #side-menu">
                        </a>
                    </li>
                </ul>
            </div>
            <div class="uk-navbar-right">
                <ul class="uk-navbar-nav">
                    <router-link v-if="!isAuthenticated" tag='li'
                                 to="/login">
                        <a>ورود</a>
                    </router-link>
                    <router-link v-if="isAuthenticated" tag='li'
                                 :to="{ name: 'profile' }">
                        <a title="پروفایل" uk-icon="icon: user"></a>
                    </router-link>
                    <li v-if="isAuthenticated">
                        <a href="javascript:void(0)" @click="logout">{{ `خروج (${user.name})` }}</a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
    import {mapState} from 'vuex';

    export default {
        name: "Header",
        computed: {
            ...mapState(['isAuthenticated', 'user'])
        },
        methods: {
            logout() {
                this.$store.dispatch('userSignOut');
            }
        }
    }
</script>

<style scoped>

</style>