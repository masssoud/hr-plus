<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
    import UIkit from 'uikit';
    import Icons from 'uikit/dist/js/uikit-icons';

    UIkit.use(Icons);

    export default {
        name: 'App',
        components: {}
    }
</script>

<style lang="less">
    @import "assets/style.less";
</style>
