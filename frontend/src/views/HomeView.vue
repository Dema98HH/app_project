<template>
  <div id="app">

    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input type="text" class="form-control col-3 mx-2" placeholder="Name" v-model="students.name">
        <input type="text" class="form-control col-3 mx-2" placeholder="Course" v-model="students.course">
        <input type="text" class="form-control col-3 mx-2" placeholder="Rating" v-model="students.rating">
 <!--   <input v-model="geeting" />-->   
        <button class="btn btn-success">Submit</button>
      </div>
    </form>
    <table class="table">
      <thead>
        <th>Name:</th>
        <th>Course:</th>
        <th>Rating:</th>
        <th>Delete::</th>
      </thead>
      <tbody>
        <tr v-for="student in students" :key="student.id" @dblclick="$data.student = student">
          <td>{{ student.name }}</td>
          <td>{{ student.course }}</td>
          <td>{{ student.rating }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteStudent(student)">x</button>
          </td>
        </tr>
      </tbody>
    </table>

  </div>

</template>

<script>
import axios from 'axios'
import HelloWorld from '@/components/HelloWorld.vue'


export default {
  name: 'App',

  name: 'HomeView',
  components: {
    HelloWorld
  },

  data() {
    return {
      students: []
    }
  },
  components: {
  },
  mounted() {
      this.getLStudents()
  },
  methods: {
      getLStudents() {
          axios({
              method:'get',
              url: 'http://127.0.0.1:8000/api/students/',

          }).then(response => this.students = response.data);
      }
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>


