<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <div class=" row justify-center">
          <h1 class="fs-1 text-fuchsia-200 max-w-max justify-center jus" style="text-shadow:  0 0 3px #FF0000, 0 0 5px #0000FF;">Welcome to promise shop </h1>
        </div>
        <div class="row justify-center">
          <p class="fs-2  max-w-max text-red-500" style="text-shadow:  0 0 5px #FF0000;">best product finder </p>
        </div>
      </div>
    </section>

    <div class="columns is-multiline justify-between">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

      <div class="column is-2 is-3-tablet" v-for="product in paginatedProducts" v-bind:key="product.id">
        <div class="box has-background-light row">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail">
          </figure>
          <div class="container break-words h-10 overflow-ellipsis">
            <p class="text-lg text-center">{{ product.name }}</p>
          </div>
          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4"> View details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from "axios"
export default {
  name: 'HomeView',
  data() {
    return {
      paginatedProducts: []
    }
  },
  components: {
  },
  mounted() {
    this.getPaginatedProducts()
  },
  methods: {
    async getPaginatedProducts() {
      this.$store.commit('setIsLoading', true)
      await axios
        .get('/api/inventory/product/all/')
        .then(response => {
          this.paginatedProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
        this.$store.commit('setIsLoasing', false)
    }
  }
}
</script>
<style scoped>
  .image {
    margin-top: -1.25 rem;
    margin-left: -1.25 rem;
    margin-right: -1.25 rem;
  }
</style>