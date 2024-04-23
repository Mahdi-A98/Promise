<template>
  <div id="wrapper">

    <Header/>
    
    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>

  </div>
</template>

<script setup>
  import {ref} from 'vue';
  import Header from "@/components/Header.vue";
</script>


<style lang="scss">
@import '../node_modules/bulma';
@import './index.css';
</style>
