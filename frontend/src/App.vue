<template>
  <div :class="isDarkMode ? ['dark'] : []" class="bg-white dark:bg-neutral-800 flex flex-col h-[100%]">
    <nav-bar v-model="isDarkMode" class="text-gray-800 dark:text-gray-100 bg-white dark:bg-neutral-800"/>
    <!-- add top margin to account for nav-bar height-->
    <router-view class="mt-20 text-gray-800 dark:text-gray-100 bg-white dark:bg-neutral-800 grow"/>
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import NavBar from "@/components/NavBar.vue";
import {ref} from "vue";

const isDarkMode = ref(true)
</script>


<style scoped>
</style>
