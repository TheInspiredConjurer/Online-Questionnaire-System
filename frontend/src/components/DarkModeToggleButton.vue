<template>
  <div class="flex">
    <span class="mx-4">{{ modelValue ? 'dark' : 'light' }}</span>
    <input v-model="isDarkMode" type="checkbox" />
  </div>
</template>

<script setup>
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
