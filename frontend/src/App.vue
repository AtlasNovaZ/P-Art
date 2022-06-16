<script lang="ts">
import { defineComponent } from "vue";
import Home from './pages/home.vue'

export default defineComponent({
  setup() {

  }
})

</script>

<template>
  <nav class="z-100 bg-stone-900 shadow-lg  border-b-4 border-indigo-600 overflow-y-hidden">
    <div class="container flex flex-wrap justify-between py-3 items-center mx-auto shadow-lg  ">
      <a href="#" class="flex items-center">
        <h1 class="text-4xl self-center font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-500  to-fuchsia-500"> P-Art</h1>
      </a>
      <div class="hidden w-full md:block md:w-auto" id="mobile-menu">
        <ul class="flex flex-col mt-4 md:flex-row md:space-x-8 md:mt-0 md:text-sm md:font-medium">
          <li>
            <router-link :to="{ path: '/' }" class="block py-2 pr-4 pl-3 text-white text-xl md:bg-transparent dark:text-white">
              Home
            </router-link>
          </li>
          <li>
            <router-link :to="{ path: '/about' }" class="block py-2 pr-4 pl-3 text-white text-xl md:bg-transparent dark:text-white">
              About
              </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <router-view></router-view>
</template>



