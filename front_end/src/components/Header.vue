<template>
    <nav class="navbar sticky top-0 bg-sky-500 bg-opacity-35" role="navigation" aria-label="main navigation">
        <div class="navbar-brand w-100">
            <a class="navbar-itesm " href="https://bulma.io">
            <img class=" object-contain h-20 m-2 p-0  w-20 navbar-item"  src="@\assets\pUntitled2.png"/>
            </a>

            <a role="button" class="navbar-burger mr-5" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample" @click="changeBurger">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
        </div>
        <div id="navbarBasicExample" class="navbar-menu rounded fixed bg-opacity-20 lg:static  top-20  z-5" v-bind:class="{'is-active': showMobileMenu}">
            <div class="navbar-start">
            <a class="navbar-item">
                Home
            </a>

            <a class="navbar-item">
                Documentation
            </a>

            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link">
                More
                </a>

                <div class="navbar-dropdown">
                <a class="navbar-item">
                    About
                </a>
                <a class="navbar-item is-selected">
                    Jobs
                </a>
                <a class="navbar-item">
                    Contact
                </a>
                <hr class="navbar-divider">
                <a class="navbar-item">
                    Report an issue
                </a>
                </div>
            </div>
            </div>

            <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                <a class="button is-primary">
                    <strong>Sign up</strong>
                </a>
                <a class="button is-light">
                    Log in
                </a>
                </div>
            </div>
            </div>
        </div>
    </nav>
    
</template>
<script setup>
import {ref} from 'vue';
const showMobileMenu = ref(false);

function changeBurger() {
    showMobileMenu.value = ! showMobileMenu.value;
}

window.addEventListener('scroll', function() {
    const navbar = document.getElementById('navbar');
    const scrollPosition = window.scrollY;
    // const navbarOpacity = scrollPosition <= 35 ? 100 : 35;
    // navbar.style.opacity = navbarOpacity / 100;
    const scrolledDown = scrollPosition <= 35 ? false : true;
    if (scrolledDown == true) {
        navbar.classList.replace('bg-opacity-100', 'bg-opacity-75');
    }
    else {
        navbar.classList.replace('bg-opacity-75', 'bg-opacity-100');
    }
});
</script>
<!-- <template>
    <nav class="navbar is-dark">
        <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Promise shop</strong></router-link>
        </div>
        <a class="navbar-burger iss-1 bg-success is-pulled-risght" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="changeBurger">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        </a>


        <div class="navbar-menu is-pullesd-right" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
            <div class="navbar-end">
            <router-link to="/summer" class="navbar-item">Summer</router-link>
            <router-link to="/winter" class="navbar-item">Winter</router-link>
            </div>
            <div class="navbar-item">
            <div class="buttons">
                <router-link to="/login" class="button is-light">Log in</router-link>
                <router-link to="/login" class="button is-success">
                <span class="icon"><i class="fa fa-shopping-cart"></i></span>
                <span>Cart</span>
                </router-link>
            </div>
            </div>
        </div>
    </nav>
</template> -->
