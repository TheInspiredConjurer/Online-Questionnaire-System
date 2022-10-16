<template>
  <div class="flex flex-col items-center smooth-shadow m-4 zoom">
    <h3>{{ headline }}</h3>
    <slot />
  </div>
</template>

<script setup>
defineProps({
  headline: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
/*
Tailwinds hover:scale-110 unfortunately didn't work, therefore I solved it
via usual CSS
 */
.zoom {
  transition: transform .2s;
}

.zoom:hover {
  transform: scale(1.1);
}
</style>