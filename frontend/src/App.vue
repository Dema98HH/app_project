<template>
  <div id="app">
  <div>
    <nav>
      <router-link to="/">Home | </router-link>
      <router-link to="/about">About </router-link>
    </nav>
  </div>
  </div>
  <router-view/>
</template>

<script>


export default {
  name: 'App',
  data(){
    return {
      student: {},
      students: []
    }
  },

  async created(){
    await this.getStudents();
  },

  methods: {

    submitForm(){
      if (this.student.id === undefined){
        this.createStudent();

      } else {
        this.editStudent();
      }
    },
    async getStudents(){
      var response = await fetch('http://127.0.0.1:8000/api/students/')
      this.students = await response.json();
    },

    async createStudent() {
      await this.getStudents()

      await fetch('http://127.0.0.1:8000/api/students/', {
        method: 'post',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });

      await this.getStudents()
    },
    async editStudent(){
      await this.getStudents()

      await fetch(`http://127.0.0.1:8000/api/students/${this.student.id}/`, {
        method: 'put',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });

      await this.getStudents(),
      this.student = {}
    },

    async deleteStudent(student){
      await this.getStudents()

      await fetch(`http://127.0.0.1:8000/api/students/${student.id}/`, {
        method: 'delete',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(this.student)
      });

      await this.getStudents();
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
