<template>
  <nav
    class="flex justify-between py-4 smooth-shadow-black dark:smooth-shadow-white fixed top-0 w-[100%]"
  >
    <router-link :to="{ name: 'home' }" class="mx-4">
      <img
        class="w-12"
        :src="isDarkMode ? lightOqslogo : darkOqslogo"
        alt="ows-logo"
      />
    </router-link>
    <div class="flex mx-4 items-center">
      <router-link :to="{ name: 'home' }" class="mr-8">Home</router-link>
      <router-link :to="{ name: 'questions' }" class="mr-8"
        >Questions</router-link
      >
      <router-link :to="{ name: 'solutions' }" class="mr-8"
        >Solutions</router-link
      >
      <router-link :to="{ name: 'login' }" class="mr-8">Login</router-link>
      <router-link :to="{ name: 'register' }" class="mr-8"
        >Register</router-link
      >
      <logo-link
        :logo="isDarkMode ? lightGithubLogoUrl : darkGithubLogoUrl"
        link="https://github.com/TheInspiredConjurer/Online-Questionnaire-System"
        small
      />
      <DarkModeToggleButton v-model="isDarkMode" />
    </div>
  </nav>
</template>

<script setup>
import lightGithubLogoUrl from '@/assets/github-logo-light.png'
import darkGithubLogoUrl from '@/assets/github-logo-dark.png'
import LogoLink from '@/components/LogoLink.vue'
import darkOqslogo from '@/assets/oqs-logo-dark.svg'
import lightOqslogo from '@/assets/oqs-logo-light.svg'
import DarkModeToggleButton from '@/components/DarkModeToggleButton.vue'
import { computed } from 'vue'

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['update:modelValue'])

const isDarkMode = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})
</script>

<style scoped>
/*
Could not find an easy way to solve this with tailwind the same way, therefore
kept it like this. Feel free to replace it with the tailwind counterparts when
you find them.
 */
nav a.router-link-exact-active {
  color: #00838f; /* primary color */
}
</style>
