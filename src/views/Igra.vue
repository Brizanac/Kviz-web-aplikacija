<template>
  <div class="container">
      <div id="question-container" v-if="gameStarted">
          <div id="question">{{currQuestion[1]}}</div>
          <div id="answer-buttons" v-for="question in currQuestion[3]" :key="question[0]" class="btn-grid">
           <button :id="'btn-' + question[0]" @click="selectAnswer(question)" :disabled="questionDone" class="btn">{{question[1]}}</button>
          </div>
          <div class="timer-wrapper">
            <div>{{sec}}</div>
            <div id="time-line"></div>
          </div>
      </div>

      <div class="controls">
          <button v-if="!gameStarted && !endGame" id="start-btn" @click="startGame" class="StartPovratak btn">Započni</button>
          <button v-if="gameStarted && !endGame" id="next-btn" @click="nextQuestion" class="next-btn btn hide">Dalje</button>
      </div>
      <div v-if="endGame">
      <h3>Igra je gotova!</h3>
      <p>Točnih odgovora: {{correctAnswers}}</p>
      <p>Netočnih odgovora: {{wrongAnswers}}</p>
      <button class="StartPovratak"><router-link to="/home" >Povratak na kategorije</router-link></button>
      </div>
  </div>
</template>

<script>

export default {
  name: 'Igra',
  data () {
    return {
      questions: this.$store.getters.getQuestions,
      shuffledQuestions: [],
      currentQuestionIndex: [],
      gameStarted: false,
      questionDone: false,
      currQuestion: '' ,
      correctAnswers: 0 ,
      wrongAnswers: 0 ,
      endGame: false,

      sec: 15,
      timeLineEl: ""
    }
  },
  watch: {
    gameStarted () {
      this.timeLineEl = document.querySelector("#time-line");
      console.log('t: #2 ', this.timeLineEl);
    }
  },
  methods: {
    startGame () {
      this.currentQuestionIndex = this.randomList(this.questions);

      this.currQuestion = this.questions[this.currentQuestionIndex];
      this.questions.splice(this.currentQuestionIndex, 1);
      this.gameStarted = true;

      this.countTime();
      //this.currentQuestionIndex = 0;
      //this.toggleQuestionContainer = true;
      //this.setNextQuestion();
    },
    selectAnswer (q) {
      let btn = document.querySelector('#btn-' + q[0]);
      if (q[2] === "1") {
        btn.style.backgroundColor = 'green';
          this.correctAnswers++;
      } else {
        btn.style.backgroundColor = 'red';
          this.wrongAnswers++;
      }
      this.questionDone = true;
    },
    nextQuestion () {
      if (this.questions.length > 0) {
        this.questionDone = false;
        this.currentQuestionIndex = this.randomList(this.questions);
        this.currQuestion = this.questions[this.currentQuestionIndex];
        this.questions.splice(this.currentQuestionIndex, 1);
        this.countReset();
      } else {
        this.gameStarted = false;
        this.endGame = true;
        this.countReset();
      }

    },
    randomList (rand) {
      return Math.floor(Math.random() * rand.length);
    },

    countTime () {
      if (this.sec == 0) {
        this.wrongAnswers++;
        this.nextQuestion();
        this.countReset();
        if (this.questions.length >= 0)  this.countTime();
      } else {
        setTimeout(() => {
          this.sec--;
          let w = this.sec / 15 * 100;
          this.timeLineEl.style.width = w + "%";
          this.countTime();
        }, 1000)
      }
    },
    countReset () {
      this.sec = 15;
      this.timeLineEl.style.width = "100%";
    }
  }
}
</script>

<style>
  .correct {
    background-color: 'green';
  }
  .wrong {
  background-color: 'red'
  }
  .time-wrapper {
    width: 100%;
    padding: 25px 100px;
    margin: 25px 0;
  }
#time-line {
  margin: 25px 0;
  width: 100%;
  background-color: red;
  height: 10px;
  border-radius: 5px;
}

.StartPovratak {
margin: 250px 0;
width: 50%;
background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%);
border-radius: 5px;
padding: 5px 10px;
outline: none;
color: #9b111e;
font-size: 20px;
}

.btn {
  height: 150%;
  width: 30%;
  border-radius: 5px;
  padding: 5px 10px;
  outline: none;
}

.btn:hover {
    border-color: black;
}

#answer-buttons {
  grid-template-columns: 100ch auto;
  margin-left: 485px;
}

.btn-grid {
    display: grid;
    gap: 10px;
    margin: 20px 0;
}

</style>
