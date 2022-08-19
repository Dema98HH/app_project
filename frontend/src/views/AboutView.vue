

<template>
  <h1>Here is a child component!</h1>
  <textarea type="text" v-model="text" />
  <button @click="send()">Click me!</button>
  <Child :message='message' class="mt-10"></Child>
</template>
  <Child />


<script>

import Child from '/home/dema/PycharmProjects/app/frontend/src/components/HelloWorld.vue'
  
export default {
  components: {
    Child
  },

  methods: {
    send(){
      this.message = this.text
      this.text = ''
    },
  },

  data(){
    return{
      text: '',
      message: '',
    }
  }
}
</script>
