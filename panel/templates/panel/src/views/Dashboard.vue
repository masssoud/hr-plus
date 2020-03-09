<template>
    <div>
        <Header></Header>
        <div class="uk-section uk-section-small uk-flex uk-padding-remove-vertical">
            <div class="uk-card uk-card-default uk-card-body uk-width-1-5@m uk-visible@m"
                 style="min-height: calc((100vh - 80px));">
                <ul class="uk-nav-default uk-nav-parent-icon" uk-nav>
                    <router-link tag='li'
                                 activeClass="uk-active"
                                 :exact="true"
                                 to="/dashboard">
                        <a><span uk-icon="icon: home"></span> داشبورد</a>
                    </router-link>
                    <router-link tag='li'
                                 activeClass="uk-active"
                                 to="/dashboard/categories">
                        <a><span uk-icon="icon: list"></span> دسته‌بندی‌ها</a>
                    </router-link>
                    <router-link tag='li'
                                 activeClass="uk-active"
                                 to="/dashboard/jobs">
                        <a><span uk-icon="icon: thumbnails"></span> موقعیت‌های شغلی</a>
                    </router-link>
                    <router-link tag='li'
                                 activeClass="uk-active"
                                 to="/dashboard/users">
                        <a><span uk-icon="icon: users"></span>کاربران</a>
                    </router-link>
                </ul>
            </div>
            <div id="side-menu" uk-offcanvas="mode: push; overlay: true">
                <div class="uk-offcanvas-bar">
                    <div class="uk-panel panel-default">
                        <ul class="uk-nav-default uk-nav-parent-icon" uk-nav>
                            <router-link tag='li'
                                         activeClass="uk-active"
                                         :exact="true"
                                         to="/dashboard">
                                <a><span uk-icon="icon: home"></span> داشبورد</a>
                            </router-link>
                            <router-link tag='li'
                                         activeClass="uk-active"
                                         to="/dashboard/categories">
                                <a><span uk-icon="icon: list"></span> دسته‌بندی‌ها</a>
                            </router-link>
                            <router-link tag='li'
                                         activeClass="uk-active"
                                         to="/dashboard/jobs">
                                <a><span uk-icon="icon: thumbnails"></span> موقعیت‌های شغلی</a>
                            </router-link>
                            <router-link tag='li'
                                         activeClass="uk-active"
                                         to="/dashboard/users">
                                <a><span uk-icon="icon: users"></span>کاربران</a>
                            </router-link>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="uk-width-1-1">
                <div class="uk-container uk-padding-small">
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Header from '../components/Header';
    import {mapState} from 'vuex';

    export default {
        name: 'Dashboard',
        components: {
            Header,
        },
        computed: {
            ...mapState(['errors', 'errorMessage'])
        },
        mounted: function () {
            this.$nextTick(async () => {
                await this.getSharedData();
            });
        },
        methods: {
            getSharedData() {
                if (!this.invalid) {
                    this.$store.dispatch('getApplicationStatuses');
                }
            }
        }
    };
</script>

<style scoped></style>
