<template>
  <button class="btn btn-danger" @click="count++">
    You clicked me {{ count }} times.
  </button>
  <div>
    Received: {{message}}
  </div>
</template>



<script>

export default {

  data() {
    return {
      count: 0,
    }
  },

props: ['message']

}
</script>
