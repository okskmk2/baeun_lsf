<template>
  <div id="app">
    <header>
      <div class="header-inner">
        <div class="brand">
          <div class="menu-icon-box">
            <i class="material-icons menu-icon">menu</i>
          </div>
          <img src="../assets/favicon_v2.png" alt="logo" class="logo" />
          <span class="brand-text">{{$t('brand')}}</span>
        </div>
        <div class="menu">
          <globalMenu class="gnb"></globalMenu>
          <div class="unb">
            <i18nChange></i18nChange>
          </div>
        </div>
      </div>
    </header>
    <router-view class="container" />
    <footer>
      <div class="container">
        <i class="fa fa-facebook-official fa-fw" aria-hidden="true"></i>
        <i class="fa fa-instagram fa-fw" aria-hidden="true"></i>
      </div>
    </footer>
  </div>
</template>

<i18n>
ko:
  brand: 바은
  brand_sub: 소프트웨어 개발사
en:
  brand: Baeun
  brand_sub: Software Company
</i18n>

<script>
import i18nChange from "../components/i18n-change";
import globalMenu from "../components/global-menu";

export default {
  name: "app",
  data() {
    return {
      modalOpen: false
    };
  },
  components: { i18nChange, globalMenu },
  mounted() {
    document.querySelector(".menu-icon").addEventListener("click", function() {
      document.querySelector(".menu").classList.toggle("show");
    });
    let as = document.querySelectorAll(".menu a");
    for (let index = 0; index < as.length; index++) {
      as[index].addEventListener("click", function() {
        document.querySelector(".menu").classList.toggle("show");
      });
    }
  }
};
</script>