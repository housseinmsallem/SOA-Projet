<template>
  <div class="cows-list">
    <h1>Cows Management</h1>
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else v-for="cow in cows" :key="cow.cow_id">
      <span>{{ cow.barn }}</span>
      <span>{{ cow.tag_number }}</span>
      <span>{{ cow.birth_rate }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import useResource from '../composables/useResource';
import { CowsApi } from '../api/resources.api';
const { cows, loading, error } = useResource(CowsApi);
</script>

<style scoped>
.cows-list {
  padding: 20px;
}
.cows-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}
.cows-table th,
.cows-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
.cows-table th {
  background-color: #f2f2f2;
}
.error {
  color: red;
}
</style>
