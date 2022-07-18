<template>
  <div>
    <h4>Тестирование № {{ testCase?.id }}</h4>
    <ul>
      <li>Дата начала - {{ testCase?.started_at }}</li>
      <li>Статус - {{ testCase?.status }}</li>
    </ul>
    <router-link
        v-if="canShowContinueButton"
        :to="{name: 'question-detail', params: {testCaseId: testCase?.test_case, processingId: testCase?.id, questionId: testCase?.current_question}}"
    >
      Продолжить
    </router-link>
    <router-link v-if="canShowResultsButton" :to="{name: 'test-case-results', params: {testCaseId: testCase.test_case, processingId: testCase.id}}">
      Посмотреть результаты
    </router-link>
  </div>
</template>

<script>
export default {
  name: "ProcessingTestCase",
  props: {
    testCase: {
      type: Object,
      required: true,
    }
  },
  computed: {
    canShowContinueButton() {
      return this.testCase.status === 'В процессе'
    },
    canShowResultsButton() {
      return this.testCase.status === 'Завершено'
    }
  }
}
</script>
