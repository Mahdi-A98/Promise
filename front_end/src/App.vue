<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Promise shop</strong></router-link>
        
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @mouseleave="changeBurger" @click="changeBurger">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>
        </div>
        <div class="navbar-item">
          <div class="buttons">
            <router-link to="/login" class="button is-light">Log in</router-link>
            <router-link to="/login" class="button is-success">
              <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              <span>Cart</span>
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2021</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu : false,
    }
  },
  methods: {
    changeBurger() {
      this.showMobileMenu = ! this.showMobileMenu;
    }
  }
  
}
</script>


<style lang="scss">
@import '../node_modules/bulma';
// footer {
//   position:absolute;
//   width:100%;
//   bottom: 0px !important;
// }
</style>
