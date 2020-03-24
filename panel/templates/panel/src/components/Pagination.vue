<template>
    <ul class="uk-pagination">
        <li v-if="previous && parseInt(previous) !== 1">
            <router-link
                    :to="{name, query:{page: previous, ...query}}">
                قبلی
            </router-link>
        </li>
        <li v-if="previous && parseInt(previous) === 1">
            <router-link
                    :to="{name, query: {...query}}">
                قبلی
            </router-link>
        </li>
        <li v-if="next">
            <router-link
                    :to="{name, query:{page: next, ...query}}">
                بعدی
            </router-link>
        </li>
    </ul>
</template>

<script>
    export default {
        name: "Pagination",
        props: ['name', 'next', 'previous'],
        data: function () {
            const query = this.$route.query;
            const clonedQuery = Object.assign({}, query);
            clonedQuery['page'] = null;
            delete clonedQuery.page;
            return {
                query: clonedQuery,
            }
        },
        watch: {
            $route() {
                const query = this.$route.query;
                const clonedQuery = Object.assign({}, query);
                clonedQuery['page'] = null;
                delete clonedQuery.page;
                this.query = clonedQuery;
            }
        },
    }
</script>

<style scoped>

</style>