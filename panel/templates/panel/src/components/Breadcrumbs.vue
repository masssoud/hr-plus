<template>
    <ul class="uk-breadcrumb">
        <li v-for="(item,index) in items" :key="`breadcrumbs-${index}`">
            <router-link v-if="index < (items.length - 1)" :to="item.to">{{ item.label }}</router-link>
            <span v-if="index === (items.length - 1)">{{ item.label }}</span>
        </li>
    </ul>
</template>

<script>
    export default {
        name: "Breadcrumbs",
        props: ['items'],
    }
</script>

<style scoped>

</style>