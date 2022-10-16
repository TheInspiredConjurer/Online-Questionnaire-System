<template>
  <nav class="flex justify-between py-4 lower-shadow fixed top-0 w-[100%] bg-white">
    <router-link :to="{name: 'home'}" class="mx-4">
      <!-- TODO: insert logo once it exists-->
    </router-link>
    <div class="flex mx-4">
      <router-link :to="{name: 'home'}" class="mr-8 " >Home</router-link>
      <router-link :to="{name: 'questions'}" class="mr-8">Questions</router-link>
      <router-link :to="{name: 'solutions'}" class="mr-8">Solutions</router-link>
      <router-link :to="{name: 'login'}" class="mr-8">Login</router-link>
      <router-link :to="{name: 'register'}" class="mr-8">Register</router-link>
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
a {
  text-decoration: none;
  color: rgb(31 41 55);
  transition: 0.4s;
}

nav a.router-link-exact-active {
  color: #00838F; /* primary color */
}
</style>