<template>
    <div>
        <span class="uk-text-muted uk-text-small">نمایش {{items.length}} مورد از {{count}} مورد</span>
        <table class="uk-table uk-table-hover uk-table-divider">
            <thead>
            <tr>
                <th v-for="(header,index) in headers" :key="`table-header-${index}`">{{ getLabel(header)}}</th>
                <th v-if="actions">عملیات</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item,index) in items" :key="`table-item-${index}`">
                <td v-for="(header,headerIndex) in headers" :key="`table-item-data-${index}-${headerIndex}`">
                    {{ getValue(item, header, headerIndex)}}
                </td>
                <td v-if="actions">
                    <ul class="uk-iconnav">
                        <li
                                v-for="(action, actionIndex) in actions"
                                :key="`table-item-action-${index}-${actionIndex}`"
                        >
                            <a @click="execute(action.callbackFunction, item)" :uk-icon="`icon: ${action.icon}`"
                               :title="action.label">
                            </a>
                        </li>
                    </ul>
                </td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: "Table",
        props: ['headers', 'count', 'items', 'actions'],
        methods: {
            execute(callbackFunction, item) {
                callbackFunction(item);
            },
            getValue(item, header, headerIndex) {
                if (header.constructor === ({}).constructor) {
                    return header.value(item);
                }
                return item[headerIndex];
            },
            getLabel(header) {
                if (header.constructor === ({}).constructor) {
                    return header.label;
                }
                return header;
            }
        },
    }
</script>

<style scoped>

</style>