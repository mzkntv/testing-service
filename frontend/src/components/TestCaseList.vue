<template>
  <div v-if="isLoaded">
    <TestCaseCard
        v-for="test_case in test_cases"
        :title="test_case.title"
        :test-case-id="test_case.id"
        :key="test_case.id"
    />
  </div>
  <div v-else>
    Loading...
  </div>
</template>

<script>
import TestCaseCard from "./TestCaseCard.vue";
import { HTTP } from "../plugins/axios.js";

export default {
  name: "TestCaseList",
  components: {
    TestCaseCard
  },
  data() {
    return {
      period: null,
      test_cases: null,
      isLoaded: false,
    }
  },
  mounted() {
    this.getAvailableTestCases()
  },
  methods: {
    getAvailableTestCases() {
      HTTP.get(`/api/test-cases/`).then(({data}) => {
        this.test_cases = data
        this.isLoaded = true
      })
    }
  }
}
</script>
