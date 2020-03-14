<template>
    <div>
        <Header></Header>
        <div class="uk-section uk-section-small uk-flex uk-padding-remove-vertical">
            <div class="uk-card uk-card-default uk-card-body uk-width-1-5@m uk-visible@m"
                 style="min-height: calc((100vh - 80px));">
                <Menu></Menu>
            </div>
            <div id="side-menu" uk-offcanvas="mode: push; overlay: true">
                <div class="uk-offcanvas-bar">
                    <div class="uk-panel panel-default">
                        <Menu></Menu>
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
    import Menu from '../components/Menu';
    import {mapState} from 'vuex';

    export default {
        name: 'Dashboard',
        components: {
            Header,
            Menu,
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
