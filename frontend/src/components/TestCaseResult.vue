<template>
  <div v-if="isLoaded">
    <div>
      Количество правильных ответов - {{ result.correct_answers }}/{{ result.all_answers }}
    </div>
    <div>
      Процент правильных ответов - {{ result.percent }}
    </div>
  </div>
  <div v-else>Loading...</div>
  <router-link :to="{name: 'test-case-list'}">На главную</router-link>
</template>

<script>
import { HTTP } from "../plugins/axios.js";

export default {
  name: "TestCaseResult",
  props: {
    testCaseId: {
      type: String,
      required: true
    },
    processingId: {
      type: String,
      required: true
    },
  },
  data() {
    return {
      isLoaded: false,
      result: null,
    }
  },
  methods: {
    getResults() {
      HTTP.get(`/api/test-cases/${this.testCaseId}/processing/${this.processingId}/result/`).then(({data}) => {
        this.result = data
        this.isLoaded = true
      })
    }
  },
  mounted() {
    this.getResults()
  }
}
</script>
