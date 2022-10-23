<template>
  <a :href="link" :class="small ? '' : 'm-4'">
    <img :class="small ? 'w-5' : 'w-16'" :src="logo" alt="" />
  </a>
</template>

<script>
export default {
  props: {
    link: {
      type: String,
      required: true
    },
    logo: {
      type: String,
      required: true
    },
    small: Boolean
  }
}
</script>
