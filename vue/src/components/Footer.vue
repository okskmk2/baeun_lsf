<template>
    <footer>
        <div class="row jc-between">
            <div>
                <i18nChange></i18nChange>
            </div>
            <div>&copy;Baeun</div>
        </div>
    </footer>
</template>

<script>
    import i18nChange from "../components/i18n-change";

    export default {
        name: "Footer",
        components: {i18nChange}
    }
</script>
