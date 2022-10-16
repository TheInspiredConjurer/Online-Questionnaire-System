<template>
  <div>
    <nav-bar />
    <router-view />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from "@/components/NavBar.vue";
</script>


<style scoped>
</style>
