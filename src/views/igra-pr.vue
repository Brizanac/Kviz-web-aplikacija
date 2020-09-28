<template>
  <div class="container">
      <div id="question-container" v-if="toggleQuestionContainer">
          <div id="question">{{currQuestion}}</div>
          <div id="answer-buttons" v-for="(question, index) in currentQuestion.answer" :key="index" class="btn-grid">
           <button @click="selectAnswer(question.correct)" class="btn">{{question.text}}</button>
          </div>
      </div>
      <div class="controls">
          <button v-if="!gameStarted" id="start-btn" @click="startGame" class="start-btn btn">Započni</button>
          <button id="next-btn" class="next-btn btn hide">Dalje</button>
      </div>
  </div>
</template>

<script>

export default {
  name: 'igra',
  data () {
    return {
      shuffledQuestions: [],
      currentQuestionIndex: [],
      gameStarted: false,
      toggleQuestionContainer: false,

      currQuestion: '',

    }
  },
  methods: {
    startGame () {
      this.gameStarted = true;
      this.shuffledQuestions = questions.sort(() => Math.random() - .5;
      this.currentQuestionIndex = 0;
      this.toggleQuestionContainer = true;
      this.setNextQuestion();
    },
    setNextQuestion () {
      this.resetState();
      this.showQuestion(this.shuffledQuestions[this.currentQuestionIndex]);
    },
    resetState () {

    },
    showQuestion (question) {
      this.currQuestion = question.question;
    },
    selectAnswer (correct) {

    }
  }

}


  methods: {

  //const startButton = document.getElementById('start-btn')
  const nextButton = document.getElementById('next-btn')
  const questionContainerElement = document.getElementById('question-container')
  const questionElement = document.getElementById('question')
  const answerButtonsElement = document.getElementById('answer-buttons')

  //let shuffledQuestions, currentQuestionIndex

  //startButton.addEventListener('click', startGame)
  nextButton.addEventListener('click', () => {
      currentQuestionIndex++
      setNextQuestion()
  })

  /*function startGame() {
  //startButton.classList.add('hide')
  //shuffledQuestions = questions.sort(() => Math.random() - .5)
  //currentQuestionIndex = 0
  //questionContainerElement.classList.remove('hide')
  //setNextQuestion()
}*/

/*
  function setNextQuestion() {
      resetState()
  showQuestion(shuffledQuestions[currentQuestionIndex])
}*/

  function showQuestion(question) {
  //questionElement.innerText = question.question
  question.answers.forEach(answer => {
      const button = document.createElement('button')
      button.innerText = answer.text
      button.classList.add('btn')
      if (answer.correct) {
      button.dataset.correct = answer.correct
      }
      button.addEventListener('click', selectAnswer)
      answerButtonsElement.appendChild(button)
  })
  }

  function resetState() {
      clearStatusClass(document.body)
      nextButton.classList.add('hide')
      while (answerButtonsElement.firstChild) {
          answerButtonsElement.removeChild
          (answerButtonsElement.firstChild)
      }
  }

  function selectAnswer (e) {
      const selectedButton = e.target
      const correct = selectedButton.dataset.correct
      setStatusClass(document.body, correct)
      Array.from(answerButtonsElement.children).forEach(button => {
          setStatusClass(button, button.dataset.correct)
      })
      if (shuffledQuestions.length > currentQuestionIndex + 1){
          nextButton.classList.remove('hide')
      } else {
          startButton.innerText = 'Restart'
          startButton.classList.remove('hide')
      }
  }

  function setStatusClass(element, correct){
      clearStatusClass(element)
      if (correct) {
          element.classList.add('correct')
      }   else {
          element.classList.add('wrong')
      }
  }

  function clearStatusClass(element) {
      element.classList.remove('correct')
      element.classList.remove('wrong')
  }

  /*const questions = [
      {
          question: 'Tko je najjači od navedenih?',
          answers: [
          {text: 'Gordan Giriček', correct: true},
          {text: 'Stanko Poklepović Špaco', correct: false},
          {text: 'Nikola Tesla', correct: false},
          {text: 'Špiro Guberina', correct: false},
          ]
      },

      {
          question: 'Drugo pitanje? ',
          answers: [
          {text: 'Na drugo pitanje', correct: false},
          {text: 'Ne znam odgovor', correct: false},
          {text: 'Naime drugo pitanje', correct: false},
          {text: 'je veoma čudnovato', correct: true},
          ]
      },
  ]*/



  }

}
</script>


<style scoped>

*, *::before, *::after {
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

:root {
    --hue-neutral: 200;
    --hue-wrong: 0;
    --hue-correct: 145;
}

body{
    --hue: var(--hue-neutral);
    padding: 0;
    margin: 0;
    display: flex;
    width: 100vw;
    height: 100vh;
    justify-content: center;
    align-items: center;
    background-color: hsl(var(--hue), 100%, 20%);
}

body.correct {
    --hue: var(--hue-correct);
}

body.wrong {
    --hue: var(--hue-wrong);
}

.container {
    width: 800px;
    max-width: 80%;
    background-color: white;
    border-radius: 5px;
    padding: 10px;
    box-shadow: 0 0 10px 2px;
}

.btn-grid {
    display: grid;
    grid-template-columns: repeat(2, auto);
    gap: 10px;
    margin: 20px 0;
}


.btn {
    --hue: var(--hue-neutral);
    border: 1px solid hsl(var(--hue), 100%, 30%);
    background-color: hsl(var(--hue), 100%, 50%);
    border-radius: 5px;
    padding: 5px 10px;
    color: white;
    outline: none;
}

.btn:hover {
    border-color: black;
}

.btn.correct {
    --hue: var(--hue-correct);
    color: black;
}

.btn.wrong {
    --hue: var(--hue-wrong);
}

.start-btn, .next-btn {
    font-size: 1.5rem;
    font-weight: bold;
    padding: 10px 20px;
}

.controls {
    display: flex;
    justify-content: center;
    align-items: center;
}

.hide {
    display: none;
}

</style>
