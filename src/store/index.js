import { createStore } from 'vuex'

export default createStore({
  // varijable, liste, rijecnici
  state: {
    user: {},
    questions: []
  },
  // mjenjaju vrijednost varijabli iz state-a. Jedina pravilna pohrana podataka u vuex
  mutations: {
    setUser (state, payload) {
      state.user = payload
    },
    setQuestions (state, payload) {
      state.questions = payload
    }
  },
  // akcije pozivaju mutacije
  actions: {
  },
  // ako zelis imati vise storova: storeA, storeB. To se koristi kad imas jako puno stvari ovdje
  modules: {
  },
  // dohvacanje stvari
  getters: {
    getQuestions: state => {
      return state.questions
    },
    getUser: state => {
      return state.user
    }
  }
})
