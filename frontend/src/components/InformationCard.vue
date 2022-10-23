<template>
  <div
    class="flex flex-col items-center boxing-black dark:boxing-white m-4 rounded zoom"
  >
    <h3>{{ headline }}</h3>
    <slot />
  </div>
</template>

<script>
export default {
  props: {
    headline: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
/*
Tailwinds hover:scale-110 unfortunately didn't work, therefore I solved it
via usual CSS. Feel free to replace this with the tailwind counterparts once
you get it working.
 */
.zoom {
  transition: transform 0.2s;
}

.zoom:hover {
  transform: scale(1.1);
}
</style>
