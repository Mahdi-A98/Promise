<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <h1>Welcome to promise shop </h1>
        <p>best product finder </p>
      </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest Products</h2>
      </div>

      <div class=" column is-3" v-for="product in paginatedProducts" v-bind:key="product.id">
        <div class="box">
          <figure class="image mb-4">
            <img :src="product.get_thumbnail">
          </figure>
          <h3 class="is-size-4">{{ product.name }}</h3>
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
    getPaginatedProducts() {
      axios
        .get('/api/inventory/product/all/')
        .then(response => {
          this.paginatedProducts = response.data
        })
        .catch(error => {
          console.log(error)
        })
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