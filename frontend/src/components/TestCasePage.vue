<template>
  <div>
    <h1>Сервис проведения тестирования</h1>
    <select v-model="period">
      <option disabled value="">Выберите один из вариантов</option>
      <option>Доступные</option>
      <option>В процессе</option>
      <option>Завершенные</option>
    </select>
    <div v-if="period">
      <TestCaseCard v-for="test_case in test_cases" :title="test_case.title" :id="test_case.id" :key="test_case.id" />
    </div>
  </div>
</template>

<script>
import TestCaseCard from "./TestCaseCard.vue";
import axios from "axios";

export default {
  name: "TestCasePage",
  components: {TestCaseCard},
  data() {
    return {
      period: null,
      test_cases: null,
    }
  },
  mounted() {
    document.cookie = 'csrftoken=XXkRmNUkpDf0KHXoc3rh9eZBo7Q8clkHgRwBuuAoJlHyVIpkpp5Nh1jJ3EooUujC; sessionid=voqwe9lpejkcn60zzr68ge9upi2k6ll3'
  },
  watch: {
    period(newPeriod) {
      axios.get('http://127.0.0.1:5173/api/test-cases/', {
        withCredentials: true,
        headers: {
          'X-CSRFToken': 'XXkRmNUkpDf0KHXoc3rh9eZBo7Q8clkHgRwBuuAoJlHyVIpkpp5Nh1jJ3EooUujC',
        }
      }).then(({data}) => {
        this.test_cases = data
      })
    }
  }
}
</script>
