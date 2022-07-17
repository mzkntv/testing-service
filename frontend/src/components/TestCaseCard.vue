<template>
  <div>
    <h4>{{ title }}</h4>
    <button type="button" @click="startTest">{{ btnText }}</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "TestCaseCard",
  props: {
    id: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    btnText: {
      type: String,
      required: false,
      default: 'Начать',
    }
  },
  methods: {
    startTest() {
      axios.post(`http://127.0.0.1:5173/api/test-case/${id}/processing`, {

      }).then(() => console.log('success'))
    }
  }
}
</script>
