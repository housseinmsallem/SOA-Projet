<template>
  <div class="sidebar">
    <div class="sidebar-header">
      <i class="fas fa-cow"></i>
      <h1>Ferme Manager</h1>
    </div>

    <!-- Tableau de bord -->
    <div class="menu-category">
      <div class="category-title" @click="toggleCategory('dashboard')">
        <i class="fas fa-chart-pie"></i>
        <span>Tableau de bord</span>
      </div>
      <ul class="menu-items" :class="{ collapsed: collapsedCategories.dashboard }">
        <li><router-link to="/"><i class="fas fa-home"></i> <span>Vue d'ensemble</span></router-link></li>
        <li><router-link to="/statistics"><i class="fas fa-chart-line"></i> <span>Statistiques</span></router-link></li>
        <li><router-link to="/notifications"><i class="fas fa-bell"></i> <span>Notifications</span></router-link></li>
      </ul>
    </div>

    <!-- Gestion des ressources -->
    <div class="menu-category">
      <div class="category-title" @click="toggleCategory('resources')">
        <i class="fas fa-boxes"></i>
        <span>Gestion des ressources</span>
      </div>
      <ul class="menu-items" :class="{ collapsed: collapsedCategories.resources }">
        <li><router-link to="/personnel"><i class="fas fa-users"></i> <span>Personnel</span></router-link></li>
        <li><router-link to="/external"><i class="fas fa-user-md"></i> <span>Intervenants externes</span></router-link></li>
        <li><router-link to="/machines"><i class="fas fa-tractor"></i> <span>Machines</span></router-link></li>
        <li><router-link to="/tools"><i class="fas fa-tools"></i> <span>Outillage</span></router-link></li>
        <li><router-link to="/spareparts"><i class="fas fa-cog"></i> <span>Pièces de rechange</span></router-link></li>
        <li><router-link to="/fuels"><i class="fas fa-gas-pump"></i> <span>Carburants</span></router-link></li>
      </ul>
    </div>

    <!-- Alimentation des vaches -->
    <div class="menu-category">
      <div class="category-title" @click="toggleCategory('feeding')">
        <i class="fas fa-utensils"></i>
        <span>Alimentation des vaches</span>
      </div>
      <ul class="menu-items" :class="{ collapsed: collapsedCategories.feeding }">
        <li><router-link to="/diet-plan"><i class="fas fa-list-alt"></i> <span>Plan alimentaire</span></router-link></li>
        <li><router-link to="/rations"><i class="fas fa-weight"></i> <span>Rations</span></router-link></li>
        <li><router-link to="/scheduling"><i class="fas fa-clock"></i> <span>Programmation</span></router-link></li>
        <li><router-link to="/consumption"><i class="fas fa-chart-bar"></i> <span>Suivi consommation</span></router-link></li>
      </ul>
    </div>

    <!-- Gestion du troupeau -->
    <div class="menu-category">
      <div class="category-title" @click="toggleCategory('herd')">
        <i class="fas fa-cow"></i>
        <span>Gestion du troupeau</span>
      </div>
      <ul class="menu-items" :class="{ collapsed: collapsedCategories.herd }">
        <li><router-link to="/identification"><i class="fas fa-id-card"></i> <span>Identification</span></router-link></li>
        <li><router-link to="/lifecycle"><i class="fas fa-history"></i> <span>Cycle de vie</span></router-link></li>
        <li><router-link to="/health"><i class="fas fa-heartbeat"></i> <span>Santé</span></router-link></li>
        <li><router-link to="/vaccinations"><i class="fas fa-syringe"></i> <span>Vaccinations</span></router-link></li>
      </ul>
    </div>

    <!-- Gestion de production -->
    <div class="menu-category">
      <div class="category-title" @click="toggleCategory('production')">
        <i class="fas fa-tint"></i>
        <span>Gestion de production</span>
      </div>
      <ul class="menu-items" :class="{ collapsed: collapsedCategories.production }">
        <li><router-link to="/quantification"><i class="fas fa-weight"></i> <span>Quantification</span></router-link></li>
        <li><router-link to="/quality"><i class="fas fa-flask"></i> <span>Qualité du lait</span></router-link></li>
        <li><router-link to="/milking"><i class="fas fa-calendar"></i> <span>Planning de traite</span></router-link></li>
        <li><router-link to="/storage"><i class="fas fa-temperature-low"></i> <span>Stockage</span></router-link></li>
        <li><router-link to="/deliveries"><i class="fas fa-truck"></i> <span>Livraisons</span></router-link></li>
      </ul>
    </div>

    <!-- État et analyse -->
    <div class="menu-category">
      <div class="category-title" @click="toggleCategory('analysis')">
        <i class="fas fa-chart-line"></i>
        <span>État et analyse</span>
      </div>
      <ul class="menu-items" :class="{ collapsed: collapsedCategories.analysis }">
        <li><router-link to="/reports"><i class="fas fa-file-alt"></i> <span>Rapports</span></router-link></li>
        <li><router-link to="/stats"><i class="fas fa-chart-pie"></i> <span>Statistiques</span></router-link></li>
        <li><router-link to="/balance"><i class="fas fa-balance-scale"></i> <span>Bilan</span></router-link></li>
        <li><router-link to="/costs"><i class="fas fa-search-dollar"></i> <span>Analyse coûts</span></router-link></li>
        <li><router-link to="/forecasts"><i class="fas fa-project-diagram"></i> <span>Prévisions</span></router-link></li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';

const collapsedCategories = reactive({
  dashboard: false,
  resources: false,
  feeding: false,
  herd: false,
  production: false,
  analysis: false
});

const toggleCategory = (category) => {
  collapsedCategories[category] = !collapsedCategories[category];
};
</script>
