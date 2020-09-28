<template>
<!--cemu sluzi ovaj div, jesam li ga kopirao ili beskoristan? -->
	<div class="text-md-center">
		<h2 style="color: #FCE043;
background-image: linear-gradient(315deg, #537895 0%, #09203f 74%);">Mindrunner 2.0</h2>
		<div class="_pocetna">
			<form v-if="toggleLogin" @submit="login" class="klasaprijava">
			<h3> Prijava </h3>

					<input id="username" type="text" v-model="user.username" placeholder="Unesi korisničko ime" class="txtb">
					<input id="password" type="password" v-model="user.pass" placeholder="Unesi lozinku" class="txtb">

				<button type="submit" class="signup-btn">Prijava</button>
				<button @click="toggleLogin = false" class="ipak">Kreiraj Račun</button>
			</form>
			<form v-if="!toggleLogin" @submit="registerIt" class="klasaregistracija">
			<h3> Registracija </h3>

					<input id="name" type="text" v-model="register.ime" placeholder="Unesi ime" class="txtb">
					<input id="lastName" type="text" v-model="register.prezime" placeholder="Unesi prezime" class="txtb">
					<input id="username" type="text" v-model="register.username" placeholder="Unesi korisničko ime" class="txtb">
					<input id="email" type="email" v-model="register.email" placeholder="Unesi email" class="txtb">
					<input id="password" type="password" v-model="register.pass" placeholder="Unesi lozinku" class="txtb">

				<button type="submit" class="reg-btn">Registracija</button>
				<button @click="toggleLogin = true" class="ipak">Ipak imate račun?</button>
			</form>
		</div>

	</div>
</template>


<script>
	export default {
	name: 'Registracija',
		data() {
			return {
				toggleLogin: true,
				register:{
					ime: "",
					prezime: "",
					username:"",
					email:"",
					pass:""
				},
				user:{
					username: "",
					pass: ""
				}
			}
		},
		methods:{
			registerIt() {
			event.preventDefault();
				console.log('podaci: ', this.login);
				axios.post('/registracija', this.register)
					.then((response) => {
						this.register.name = "";
						this.register.lastName = "";
						this.register.username = "";
						this.register.email = "";
						this.register.password = "";
						this.toggleLogin = true;
					})
					.catch((e) => {
					console.log('Doslo je do greske: ', e);
					});
			},
			//asinkrona funkcija ide liniju po liniju i čeka
			async login() {
				// stopira refresh stranice, jer se funkcije poziva iz forme
				event.preventDefault();
				await axios.post('/signup', this.user)
					.then((response) => {
						console.log('res: ', response);
						this.$store.commit('setUser', response.data.korisnik);
						this.$router.replace({name: 'Home'});
					})
					.catch((e) => {
					console.log('Doslo je do greske: ', e);
					});

			}
		}
	}
</script>

<style>

.klasaprijava{
	width: 300px;
	padding: 20px;
	text-align: center;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	overflow: hidden;
}

.klasaregistracija{
	width: 300px;
	padding: 20px;
	text-align: center;
	position: absolute;
	top: 50%;
	left: 50%;
	transform: translate(-50%, -50%);
	overflow: hidden;
}

.klasaprijava h3{
	margin-top: 100px;
	font-family: 'Roboto', cursive;
	color: #06437a;
	font-site: 40px;
}

.klasaregistracija h3{
	margin-top: 100px;
	font-family: 'Roboto', cursive;
	color: #06437a;
	font-site: 40px;
}

.klasaprijava input{
	display: block;
	width: 100%;
	padding: 0 16px;
	height: 44px;
	text-align: center;
	box-sizing: border-box;
	outline: none;
	border: none;
}

.klasaregistracija input{
	display: block;
	width: 100%;
	padding: 0 16px;
	height: 44px;
	text-align: center;
	box-sizing: border-box;
	outline: none;
	border: none;
}

.txtb {
	margin: 20px 0;
	background: rgba(255,255,255,.5);
	border-radius: 6px;
}

.signup-btn{
	margin-top: 60px;
	margin-bottom: 20px;
	background: #06437a;
	color: #fff;
	border-radius: 44px;
	cursor: pointer;
	transition: 0.8s;
	width: 300px;
	height: 35px;
}

.signup-btn:hover{
	transform: scale(0.96);
}

.reg-btn{
	margin-top: 1px;
	margin-bottom: 10px;
	background: #06437a;
	color: #fff;
	border-radius: 44px;
	cursor: pointer;
	transition: 0.8s;
	width: 300px;
	height: 35px;
}

.reg-btn:hover{
	transform: scale(0.96);
}

.ipak{
	text-decoration: none;
	color: #06437a;
	font-family: "montserrat",sans-serif;
	font-size: 14px;
	padding: 5px;
	transition: 0.8s;
}

.ipak:hover{
	background: rgba(0,0,0,.3);
}
</style>
