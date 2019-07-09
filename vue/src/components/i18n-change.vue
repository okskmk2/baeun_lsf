<template>
<span class="row-in ai-center">
  <i class="material-icons">language</i>
  <select v-model="i18n.locale" @change="updateHtmlLang()" style="margin-left: 6px">
    <option v-for="lang in support_langs" :key="lang">{{lang}}</option>
  </select>
</span>
</template>
<script>
import i18n from "../i18n";
export default {
  data() {
    return {
      i18n: i18n,
      support_langs: ["ko", "en", "ja", "zh"]
    }
  },
  methods:{
    updateHtmlLang(){
      document.querySelector('html').setAttribute('lang', this.$i18n.locale);
    }
  }
};
</script>