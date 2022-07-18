<template>
  <div>
    <h4>{{ title }}</h4>
    <router-link :to="{name: 'test-case-detail', params: {testCaseId}}">История</router-link>
    <button type="button" @click="startTest">{{ startBtnText }}</button>
  </div>
</template>

<script>
import {HTTP} from "../plugins/axios.js";

export default {
  name: "TestCaseCard",
  props: {
    testCaseId: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    startBtnText: {
      type: String,
      required: false,
      default: 'Начать',
    }
  },
  methods: {
    startTest() {
      HTTP.post(`/api/test-cases/${this.testCaseId}/processing/`).then(({data}) => {
        console.log(data)
        this.$router.push({
          name: 'question-detail',
          params: {testCaseId: this.testCaseId, processingId: data?.id, questionId: data?.current_question}
        })
      })
    }
  }
}
</script>
