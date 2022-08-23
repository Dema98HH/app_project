<template>
  <h1>This is a Products View!</h1>

  <div class="columns is-multiline">
    <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">Latest products</h2>
    </div>
    <div class="row">
    <div class="col-3 card p-2 m-2"
     v-for="product in latestProducts"
     v-bind:key="product.id"
    >

        <div>
            <div>
                <figure>
                <img :src="product.get_thumbnail">
                </figure>
                <h3>{{ product.name }}</h3>
                <p>${{ product.price }}</p>
            </div>
        </div>

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