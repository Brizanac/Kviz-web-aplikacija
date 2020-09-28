<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data () {
    return {
      ime: 'Ivan'
    }
  },
  watch: {

  },
  // ovo se prvo odvija u procesu stvaranja komponente
  created () {
    //this.ime = 'Nikola';
    //this.$store.state.ime = 'Ivan';
    //this.$store.commit('setIme', 'Ivan');
    //this.ime = this.$store.getter.getIme;
    this.saljemString();
  },
  methods: {
    async dohvacanjeIzBaze () {
      await axios.get('/ime')
            .then((response) => {
              console.log('Response: ', response);
              this.ime = response.data.ime;
            })
            .catch((error) => {
              console.log('Error: ', error);
            })
    },
    saljemPodatke () {
      let podaci = {
        userCode: '123123',
        firstName: 'Ivan'
      }
      axios.post('/member', podaci)
      .then((response) => {
        console.log('Response: ', response);
        this.ime = response.data.ime;
      })
      .catch((error) => {
        console.log('Error: ', error);
      })
    },
    saljemString() {
    axios.get('/signup/' + 'VUE JE SOU')
      .then((response) => {
        console.log('Response: ', response.data.status);
      })
      .catch((error) => {
        console.log('Error: ', error);
      })
    }
  },
  computed: {

  },
  components: {
    HelloWorld
  }
}
</script>
