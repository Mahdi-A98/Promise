import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: []
    },
    token: '',
    isAuthenticated: false,
    isLoading: false
  },
  getters: {
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart'));
      }
      else {
        localStorage.setItem('cart', JSON.stringify(state.cart));
      }
    },
    addToCart(state, item) {
      const exists = state.cart.items.filter(i => i.product.sku === item.product.sku);
      if (exists.length) {
        console.log(JSON.stringify(exists[0]))
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity);
      }
      else {
        state.cart.items.push(item);
      }
      localStorage.setItem('cart', JSON.stringify(state.cart));
    },
    setIsLoading(state, status) {
      state.isLoading = status;
    }
  },
  actions: {
  },
  modules: {
  }
})
