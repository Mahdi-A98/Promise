<template>
  <div id="wrapper">

    <Header/>
    
    <section class="section">
      <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': store.state.isLoading}">
        <div class="lds-dual-ring"></div>
      </div>
      <router-view/>
    </section>

    
  </div>
  <footer class="footer">
    <p class="has-text-centered">Copyright (c) 2021</p>
  </footer>
</template>

<script setup>
  import {ref, onBeforeMount } from 'vue';
  import Header from "@/components/Header.vue";
  import store from './store';

  onBeforeMount(() => {
    console.log("onBeforMount")
    store.commit('initializeStore');
  })
</script>


<style lang="scss">
@import '../node_modules/bulma';
@import './index.css';
</style>
