<template>
  <div class="flex">
    <span class="mx-4">{{ modelValue ? "dark" : "light" }}</span>
    <input type="checkbox" v-model="modelValue" @change="$emit('update:modelValue', modelValue)">
  </div>
</template>

<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    required: true
  }
})

defineEmits(['update:modelValue'])
</script>