<template>
    <div id="app">
        <Header></Header>
        <div id="mid">
            <globalMenu class="gnb"></globalMenu>
            <router-view id="content"/>
        </div>
        <Footer></Footer>
    </div>
</template>
<script>
    import Header from '../components/Header'
    import Footer from '../components/Footer'
    import globalMenu from "../components/global-menu";

    export default {
        name: "app",
        data() {
            return {};
        },
        components: {globalMenu, Footer, Header}
    };
</script>