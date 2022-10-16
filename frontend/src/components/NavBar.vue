<template>
  <nav class="flex justify-between py-4">
    <router-link :to="{name: 'home'}" class="mx-4">OQS
    </router-link>
    <div class="flex mx-4">
      <router-link :to="{name: 'home'}" class="mr-4" >Home</router-link>
      <router-link :to="{name: 'questions'}" class="mr-4">Questions</router-link>
      <router-link :to="{name: 'solutions'}" class="mr-4">Solutions</router-link>
      <router-link :to="{name: 'login'}" class="mr-4">Login</router-link>
      <router-link :to="{name: 'register'}" class="mr-4">Register</router-link>
      <a href="https://github.com/TheInspiredConjurer/Online-Questionnaire-System">
        <img class="w-5" :src="githubLogoUrl" alt="github logo">
      </a>
    </div>
  </nav>
</template>

<script setup>
import githubLogoUrl from '@/assets/github-logo.png'
</script>

<style scoped>
nav {
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.2);
}
</style>