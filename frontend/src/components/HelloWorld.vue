<template>
  <button class="btn btn-danger" @click="count++">
    You clicked me {{ count }} times.
  </button>
</template>


<script>

export default {
  data() {
    return {
      count: 0
    }
  }
}
</script>
