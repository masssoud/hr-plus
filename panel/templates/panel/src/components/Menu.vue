<template>
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
                     to="/dashboard/applicants">
            <a><span uk-icon="icon: file-edit"></span> متقاضیان</a>
        </router-link>
        <router-link tag='li'
                     activeClass="uk-active"
                     to="/dashboard/users">
            <a><span uk-icon="icon: users"></span>کاربران</a>
        </router-link>
    </ul>
</template>

<script>
    export default {
        name: "Menu",
    }
</script>

<style scoped>

</style>