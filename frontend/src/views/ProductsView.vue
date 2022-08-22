<template>
  <h1>This is a Products View!</h1>

  <div class="columns is-multiline">
    <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
    </div>
    <div class="column is-3"
     v-for="product in latestProducts"
     v-bind:key="product.id"
    >
    <div class="box">
        <h2>{{ product.name }}</h2>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'


export default {
    name: 'Products',
    data() {
        return {
            latestProducts: []
        }
    },
    components: {
    },
    mounted() {
        this.getLatestProducts()
    },
    methods: {
        getLatestProducts() {
            axios({
                method:'get',
                url: 'http://127.0.0.1:8000/api/v1/latest-products/',

            }).then(response => this.latestProducts = response.data);
        }
    }

}
</script>