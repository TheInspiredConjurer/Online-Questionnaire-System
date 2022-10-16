<template>
  <div class="flex flex-row h-[100vh] max-h-[100vh]">
    <div class="flex flex-col">
      <div class="w-6 h-6 mr-2">
        <img alt="Vue logo" src="@/assets/logo.svg" width="24" height="24" />
      </div>

      <div>
        <nav class="flex">
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">About</RouterLink>
        </nav>
      </div>
    </div>

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>


<style scoped>
</style>
