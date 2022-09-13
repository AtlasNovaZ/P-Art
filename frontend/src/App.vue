<script lang="ts">
import { defineComponent } from "vue";
import Home from './pages/home.vue'
import axios from 'axios'

export default {
  setup() {
    axios.get('https://api.kanye.rest/')
  },
  name: "App",
};
</script>

<template>

  <router-view></router-view>
</template>



