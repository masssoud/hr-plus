<template>
    <div>
        <Breadcrumbs :items="[
            {to: {name: 'panel'}, label: 'داشبورد'},
        ]"></Breadcrumbs>
        <div class="uk-card uk-card-default uk-width-1-1">
            <div class="uk-card-header">
                <div class="uk-grid-small uk-flex-middle" uk-grid>
                    <div class="uk-width-expand">
                        <h3 class="uk-card-title uk-margin-remove-bottom">به پنل اچ‌آرپلاس خوش آمدید</h3>
                    </div>
                </div>
            </div>
            <div class="uk-card-body">
                <p>نمودارها و اطلاعات تحلیلی به زودی اضافه می‌شوند.</p>
            </div>
        </div>
    </div>
</template>

<script>
    import Breadcrumbs from "../components/Breadcrumbs";

    export default {
        name: 'Panel',
        components: {
            Breadcrumbs
        },
    };
</script>

<style scoped></style>
