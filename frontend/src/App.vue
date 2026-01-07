<template>
  <div class="app-container">
    <Sidebar />
    <div class="main-content">
      <Header :title="currentTitle" />
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useRoute } from 'vue-router';
import Sidebar from './components/Sidebar.vue';
import Header from './components/Header.vue';
import './assets/main.css';

const route = useRoute();
const currentTitle = computed(() => route.meta.title || 'Tableau de Bord');
</script>

<style>
/* No extra styles needed here as we imported main.css */
</style>
