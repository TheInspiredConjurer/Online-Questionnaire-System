<template>
  <nav class="flex justify-between py-4 smooth-shadow fixed top-0 w-[100%]">
    <router-link :to="{name: 'home'}" class="mx-4">
      <img class="w-12" :src="oqslogo" alt="ows-logo"/>
    </router-link>
    <div class="flex mx-4 items-center">
      <router-link :to="{name: 'home'}" class="mr-8 " >Home</router-link>
      <router-link :to="{name: 'questions'}" class="mr-8">Questions</router-link>
      <router-link :to="{name: 'solutions'}" class="mr-8">Solutions</router-link>
      <router-link :to="{name: 'login'}" class="mr-8">Login</router-link>
      <router-link :to="{name: 'register'}" class="mr-8">Register</router-link>
      <logo-link :logo="githubLogoUrl" link="https://github.com/TheInspiredConjurer/Online-Questionnaire-System" small/>
    </div>
  </nav>
</template>

<script setup>
import githubLogoUrl from '@/assets/github-logo-light.png'
import LogoLink from "@/components/LogoLink.vue";
import oqslogo from "@/assets/oqs_logo.svg";
</script>

<style scoped>
/*
Could not find an easy way to solve this with tailwind the same way, therefore
kept it like this. Feel free to replace it with the tailwind counterparts when
you find them.
 */
a {
  text-decoration: none;
  color: rgb(243 244 246);
  transition: 0.4s;
}

nav a.router-link-exact-active {
  color: #00838F; /* primary color */
}
</style>