<template>
    <nav class="navbar sticky top-0 bg-rose-900 bg-opacity-100  bg-gradient 0 z-50 transition-opacity duration-300" id="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand w-100 mt-0 p-0">
            <a class="navbar-itesm " href="/">
            <img class=" object-contain h-20 m-2 p-0  w-20 navbar-item mt-0"  src="@\assets\promise_logo2.png"/>
            </a>
            <a class="navbar-end p-2 mr-2 hover:bg-opacity-0">
                <div class="text-center rounded-full hover:bg-opacity-0 risng w-16 h-16 ring-slate-50 bg-opacity-90 p-2">
                    <i class="fa fa-2x fa-shopping-basket text-amber-500"></i>
                    <div class=" ring-1 z-20 ring-slate-50 ring-offset-1 rounded-full w-6 h-6 absolute lg:right-6 top-12 bg-red-500 bg-opacity-70 flex align-items-center justify-center">
                        <span class="text-slate-50">{{ cartItemsCount || 0 }}</span>
                    </div>
                </div>
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
            <!-- <a class="navbar-item"> -->
                <RouterLink to="/" class="navbar-item text-xl  font-bold  lg:text-yellow-300">
                    Home
                </RouterLink>
            <!-- </a> -->

            <a class="navbar-item text-xl  font-bold  lg:text-yellow-300 ">
                Documentation
            </a>

            <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link text-xl  font-bold  lg:text-yellow-300">
                More
                </a>

                <div class="navbar-dropdown">
                <a class="navbar-item text-xl">
                    About
                </a>
                <a class="navbar-item is-selected text-xl">
                    Jobs
                </a>
                <a class="navbar-item text-xl">
                    Contact
                </a>
                <hr class="navbar-divider">
                <a class="navbar-item text-xl">
                    Report an issue
                </a>
                </div>
            </div>
            </div>

            <div class="navbar-end">
            <div class="navbar-item">
                <div class="buttons">
                <a class="button is-primary text-xl">
                    <strong>Sign up</strong>
                </a>
                <a class="button is-light text-xl">
                    Log in
                </a>
                </div>
            </div>
            </div>
        </div>
    </nav>
    
</template>
<script setup>
import {ref, onMounted, computed} from 'vue';
import store from '@/store'
const showMobileMenu = ref(false);
const cart = ref(null)


onMounted(() => {
    cart.value = store.state.cart;
}) 

const cartItemsCount = computed(() =>{
    let count = 0;
    cart.value?.items.forEach(element => {
        count += parseInt(element.quantity)
    });
    return count
})

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
