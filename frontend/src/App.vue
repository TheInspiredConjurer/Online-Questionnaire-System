<template>
  <div>
    <nav-bar />
    <!-- add top margin to account for nav-bar height-->
    <router-view class="mt-20"/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavBar from "@/components/NavBar.vue";
</script>


<style scoped>
</style>
