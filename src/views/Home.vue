<template>
  <div id="home">
    <h3 style="color: #FCDE46;
background-image: linear-gradient(315deg, #537895 0%, #09203f 74%);">{{user[1]}} {{user[2]}}</h3>
    <button @click="signOut" class="logout">Odjava</button>
    <div style="width: 100%;">
      <div style="padding: 30px;">
        <ul class="card-wrapper">
          <li v-for="(k,index) in kategorije" :key="k.id" @click="odaberiKategoriju(k)" class="card">
            <img :src="k.images.sample" class="slike">
            <div class="card-text">{{k.name}}</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>

import img1 from "../assets/kategorija-0.jpg";
import img2 from "../assets/kategorija-1.jpg";
import img3 from "../assets/kategorija-2.jpg";
import img4 from "../assets/kategorija-3.jpg";
import img5 from "../assets/kategorija-4.jpg";
import img6 from "../assets/kategorija-5.jpg";

export default {
  name: 'Home',
  data () {
    return {
      user: this.$store.getters.getUser,
      kategorije: [
        {
        id: 1,
        name: 'Umjetnost',
        images: {
                sample: img1
            }
        },
        {
        id: 2,
        name: 'Knjizevnost',
        images: {
                sample: img2
            }
        },
        {
        id: 3,
        name: 'Znanost',
        images: {
                sample: img3
            }
        },
        {
        id: 4,
        name: 'Astronomija',
        images: {
                sample: img4
            }
        },
        {
        id: 5,
        name: 'Sport',
        images: {
                sample: img5
            }
        },
        {
        id: 6,
        name: 'Povijest',
        images: {
                sample: img6
            }
        }
      ]
    }
  },
  methods: {
    async odaberiKategoriju (kategorija) {
      await axios.get('/pitanja/' + kategorija.id)
        .then((r) => {
          console.log('r: ', r);
          this.$store.commit('setQuestions', r.data.pitanja);
          this.$router.replace({name: 'Igra'})
        })
        .catch((e) => {
          console.log('Doslo je do pogreske: Error: ', e);
        })
    },
    signOut () {
      this.$store.commit('setUser', {});
      this.$router.replace({name: 'Registracija'});
    },
  }
}
</script>

<style scoped>

.card-wrapper {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  list-style-type: none;
  justify-content: center;
}
.card {
  border: 1px solid transparent;
  border-radius: 10px;
  height: 210px;
  margin-right: 100px;
  margin-bottom: 12px;
  background-color: #ffffff;
  overflow: hidden;
  transition: 500ms ease-out;
}
.card-img {
  width: 150px;
  height: auto;
  display: block;
  padding: 0;
  margin: 0;
  position: relative;
}
.card-text {
  margin-top: -120px;
  margin-left: 36px;
  text-align: center;
  position: absolute;
  color: #FF6347;
  font-size: 28px;

}
.card:hover {
  transform: scale(1.2);
  box-shadow: 0 0 15px 3px #d7d7d7;
}

.logout {
  border: none;
  padding: 3px 20px;
  text-align: center;
  display: inline-block;
  color: #FCDE46;
  background-color: #203C5A;
}

.slike {
  height: 100%;
  width: auto;
}
</style>
