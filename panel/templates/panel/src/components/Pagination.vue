<template>
    <ul class="uk-pagination">
        <li v-if="previous && parseInt(previous) !== 1">
            <router-link
                    :to="{name, query:{page: previous}}">
                قبلی
            </router-link>
        </li>
        <li v-if="previous && parseInt(previous) === 1">
            <router-link
                    :to="{name}">
                قبلی
            </router-link>
        </li>
        <li v-if="next">
            <router-link
                    :to="{name, query:{page: next}}">
                بعدی
            </router-link>
        </li>
    </ul>
</template>

<script>
    export default {
        name: "Pagination",
        props: ['name', 'next', 'previous'],
    }
</script>

<style scoped>

</style>