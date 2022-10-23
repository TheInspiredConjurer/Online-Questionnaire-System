<template>
  <div class="flex">
    <span class="mx-4">{{ modelValue ? 'dark' : 'light' }}</span>
    <input v-model="isDarkMode" type="checkbox" />
  </div>
</template>

<script>
export default {
  props: {
    modelValue: {
      type: Boolean,
      required: true
    }
  },
  emits: ['update:modelValue'],
  computed: {
    isDarkMode: {
      get() {
        return this.modelValue
      },
      set(value) {
        this.$emit('update:modelValue', value)
      }
    }
  }
}
</script>
