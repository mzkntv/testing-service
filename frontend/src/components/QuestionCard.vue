<template>
  <div v-if="isLoaded">
    <h2>{{ question.text }}</h2>
    <div>
      Варианты ответов:
      <div v-for="choice in question.choices" :key="choice.id">
        <input type="checkbox" :id="choice.id" :value="choice.id" v-model="selectedAnswers" />
        <label :for="choice">{{ choice.text }}</label>
      </div>
    </div>
    <button @click="reply">Ответить</button>
  </div>
  <div v-else>Loading...</div>
</template>

<script>
import { HTTP } from "../plugins/axios.js";

export default {
  name: "QuestionCard",
  props: {
    testCaseId: {
      type: String,
      required: true
    },
    processingId: {
      type: String,
      required: true
    },
    questionId: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      question: null,
      isLoaded: false,
      selectedAnswers: [],
    }
  },
  methods: {
    getQuestionInfo() {
      HTTP.get(`/api/questions/${this.questionId}/`).then(({data}) => {
        this.question = data
        this.isLoaded = true
      })
    },
    reply() {
      if (!this.selectedAnswers) return
      HTTP.post('/api/answer/', {
        question: this.questionId,
        processing_test_case: this.processingId,
        selected_choices: this.selectedAnswers
      }).then(({data}) => {
        if (data.next_question) {
          window.location = `http://127.0.0.1:5173/test-cases/${this.testCaseId}/processing/${this.processingId}/questions/${data.next_question}`
        } else {
          this.$router.push({name: 'test-case-results', params: {
            testCaseId: this.testCaseId,
            processingId: this.processingId,
          }})
        }

      })
    }
  },
  mounted() {
    this.getQuestionInfo()
  }
}
</script>
