<template>
  <div v-if="isLoaded">
    <ProcessingTestCase
        v-for="processingTestCase in processingTestCases"
        :key="processingTestCase"
        :test-case="processingTestCase"
    />
  </div>
  <div v-else>Loading...</div>
</template>

<script>
import ProcessingTestCase from "./ProcessingTestCase.vue";
import {HTTP} from "../plugins/axios.js";

export default {
  name: "TestCaseDetail",
  components: {ProcessingTestCase},
  props: {
    testCaseId: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      isLoaded: false,
      processingTestCases: [],
    }
  },
  mounted() {
    this.getTestCases()
  },
  methods: {
    getTestCases() {
      HTTP.get(`/api/test-cases/${this.testCaseId}/processing/`).then(({data}) => {
        this.processingTestCases = data
        this.isLoaded = true
      })
    }
  }
}
</script>
