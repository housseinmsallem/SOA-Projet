<template>
  <div class="dashboard-header">
    <h1 class="dashboard-title">{{ title }}</h1>
    <div class="user-info">
      <div class="user-welcome">
        <div class="user-name">Mohamed HMIDEN</div>
        <div class="user-role">Administrateur</div>
      </div>
      <div class="user-avatar">MH</div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    default: 'Tableau de Bord'
  }
})
</script>
