<template>
  <div>
    <div class="flex justify-between my-4">
      <router-link :to="{name: 'home'}">Home Button</router-link>
      <div class="flex mx-4">
        <router-link :to="{name: 'home'}" class="mr-4" >Home</router-link>
        <router-link :to="{name: 'about'}">About</router-link>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<style scoped>
</style>
