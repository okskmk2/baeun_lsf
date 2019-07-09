<template>
    <header>
        <div>
            <i class="material-icons menu-icon">menu</i>
            <span class="brand-text">{{$t('brand')}}</span>
        </div>
        <div>
            <button class="big-btn">Submit</button>
            <input type="search">
            <i class="material-icons">search</i>
            <i class="material-icons" style="margin-left: 20px">account_circle</i>
        </div>
    </header>
</template>
<i18n>
ko:
    brand: LSF
en:
    brand: LSF
</i18n>
<script>
    export default {
        name: "Header"
    }
</script>