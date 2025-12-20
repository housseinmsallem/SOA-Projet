<script setup>
import { ref } from 'vue';
import './style.css';

const activeSection = ref('overview');
const collapsedCategories = ref([]);

const toggleCategory = (category) => {
  if (collapsedCategories.value.includes(category)) {
    collapsedCategories.value = collapsedCategories.value.filter(c => c !== category);
  } else {
    collapsedCategories.value.push(category);
  }
};

const isCollapsed = (category) => collapsedCategories.value.includes(category);

const setActiveSection = (section) => {
  activeSection.value = section;
};
</script>

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
            <ul class="menu-items" :class="{ collapsed: isCollapsed('dashboard') }">
                <li :class="{ active: activeSection === 'overview' }" @click="setActiveSection('overview')"><i class="fas fa-home"></i> <span>Vue d'ensemble</span></li>
                <li :class="{ active: activeSection === 'statistics' }" @click="setActiveSection('statistics')"><i class="fas fa-chart-line"></i> <span>Statistiques</span></li>
                <li :class="{ active: activeSection === 'notifications' }" @click="setActiveSection('notifications')"><i class="fas fa-bell"></i> <span>Notifications</span></li>
            </ul>
        </div>
        
        <!-- Gestion des ressources -->
        <div class="menu-category">
            <div class="category-title" @click="toggleCategory('resources')">
                <i class="fas fa-boxes"></i>
                <span>Gestion des ressources</span>
            </div>
            <ul class="menu-items" :class="{ collapsed: isCollapsed('resources') }">
                <li :class="{ active: activeSection === 'personnel' }" @click="setActiveSection('personnel')"><i class="fas fa-users"></i> <span>Personnel</span></li>
                <li :class="{ active: activeSection === 'external' }" @click="setActiveSection('external')"><i class="fas fa-user-md"></i> <span>Intervenants externes</span></li>
                <li :class="{ active: activeSection === 'machines' }" @click="setActiveSection('machines')"><i class="fas fa-tractor"></i> <span>Machines</span></li>
                <li :class="{ active: activeSection === 'tools' }" @click="setActiveSection('tools')"><i class="fas fa-tools"></i> <span>Outillage</span></li>
                <li :class="{ active: activeSection === 'spareparts' }" @click="setActiveSection('spareparts')"><i class="fas fa-cog"></i> <span>Pièces de rechange</span></li>
                <li :class="{ active: activeSection === 'fuels' }" @click="setActiveSection('fuels')"><i class="fas fa-gas-pump"></i> <span>Carburants</span></li>
            </ul>
        </div>
        
        <!-- Alimentation des vaches -->
        <div class="menu-category">
            <div class="category-title" @click="toggleCategory('feeding')">
                <i class="fas fa-utensils"></i>
                <span>Alimentation des vaches</span>
            </div>
            <ul class="menu-items" :class="{ collapsed: isCollapsed('feeding') }">
                <li :class="{ active: activeSection === 'diet-plan' }" @click="setActiveSection('diet-plan')"><i class="fas fa-list-alt"></i> <span>Plan alimentaire</span></li>
                <li :class="{ active: activeSection === 'rations' }" @click="setActiveSection('rations')"><i class="fas fa-weight"></i> <span>Rations</span></li>
                <li :class="{ active: activeSection === 'scheduling' }" @click="setActiveSection('scheduling')"><i class="fas fa-clock"></i> <span>Programmation</span></li>
                <li :class="{ active: activeSection === 'consumption' }" @click="setActiveSection('consumption')"><i class="fas fa-chart-bar"></i> <span>Suivi consommation</span></li>
            </ul>
        </div>
        
        <!-- Gestion du troupeau -->
        <div class="menu-category">
            <div class="category-title" @click="toggleCategory('herd')">
                <i class="fas fa-cow"></i>
                <span>Gestion du troupeau</span>
            </div>
            <ul class="menu-items" :class="{ collapsed: isCollapsed('herd') }">
                <li :class="{ active: activeSection === 'identification' }" @click="setActiveSection('identification')"><i class="fas fa-id-card"></i> <span>Identification</span></li>
                <li :class="{ active: activeSection === 'lifecycle' }" @click="setActiveSection('lifecycle')"><i class="fas fa-history"></i> <span>Cycle de vie</span></li>
                <li :class="{ active: activeSection === 'health' }" @click="setActiveSection('health')"><i class="fas fa-heartbeat"></i> <span>Santé</span></li>
                <li :class="{ active: activeSection === 'vaccinations' }" @click="setActiveSection('vaccinations')"><i class="fas fa-syringe"></i> <span>Vaccinations</span></li>
            </ul>
        </div>
        
        <!-- Gestion de production -->
        <div class="menu-category">
            <div class="category-title" @click="toggleCategory('production')">
                <i class="fas fa-tint"></i>
                <span>Gestion de production</span>
            </div>
            <ul class="menu-items" :class="{ collapsed: isCollapsed('production') }">
                <li :class="{ active: activeSection === 'quantification' }" @click="setActiveSection('quantification')"><i class="fas fa-weight"></i> <span>Quantification</span></li>
                <li :class="{ active: activeSection === 'quality' }" @click="setActiveSection('quality')"><i class="fas fa-flask"></i> <span>Qualité du lait</span></li>
                <li :class="{ active: activeSection === 'milking' }" @click="setActiveSection('milking')"><i class="fas fa-calendar"></i> <span>Planning de traite</span></li>
                <li :class="{ active: activeSection === 'storage' }" @click="setActiveSection('storage')"><i class="fas fa-temperature-low"></i> <span>Stockage</span></li>
                <li :class="{ active: activeSection === 'deliveries' }" @click="setActiveSection('deliveries')"><i class="fas fa-truck"></i> <span>Livraisons</span></li>
            </ul>
        </div>
        
        <!-- État et analyse -->
        <div class="menu-category">
            <div class="category-title" @click="toggleCategory('analysis')">
                <i class="fas fa-chart-line"></i>
                <span>État et analyse</span>
            </div>
            <ul class="menu-items" :class="{ collapsed: isCollapsed('analysis') }">
                <li :class="{ active: activeSection === 'reports' }" @click="setActiveSection('reports')"><i class="fas fa-file-alt"></i> <span>Rapports</span></li>
                <li :class="{ active: activeSection === 'stats' }" @click="setActiveSection('stats')"><i class="fas fa-chart-pie"></i> <span>Statistiques</span></li>
                <li :class="{ active: activeSection === 'balance' }" @click="setActiveSection('balance')"><i class="fas fa-balance-scale"></i> <span>Bilan</span></li>
                <li :class="{ active: activeSection === 'costs' }" @click="setActiveSection('costs')"><i class="fas fa-search-dollar"></i> <span>Analyse coûts</span></li>
                <li :class="{ active: activeSection === 'forecasts' }" @click="setActiveSection('forecasts')"><i class="fas fa-project-diagram"></i> <span>Prévisions</span></li>
            </ul>
        </div>
    </div>
    
    <!-- Main Content -->
    <div class="main-content">
        <div class="dashboard-header">
            <h1 class="dashboard-title">Tableau de Bord</h1>
            <div class="user-info">
                <div class="user-welcome">
                    <div class="user-name">Mohamed HMIDEN</div>
                    <div class="user-role">Administrateur</div>
                </div>
                <div class="user-avatar">MH</div>
            </div>
        </div>
        
        <!-- Vue d'ensemble (Section active par défaut) -->
        <div v-show="activeSection === 'overview'" class="content-section active">
            <!-- Stats Overview -->
            <div class="stats-section">
                <h2 class="section-title"><i class="fas fa-chart-line"></i> Aperçu des indicateurs</h2>
                
                <div class="stats-cards">
                    <div class="stat-card">
                        <div class="stat-icon cows-icon">
                            <i class="fas fa-cow"></i>
                        </div>
                        <div class="stat-info">
                            <h3>142</h3>
                            <p>Vaches enregistrées</p>
                        </div>
                    </div>
                    
                    <div class="stat-card">
                        <div class="stat-icon milk-icon">
                            <i class="fas fa-tint"></i>
                        </div>
                        <div class="stat-info">
                            <h3>1,245 L</h3>
                            <p>Production aujourd'hui</p>
                        </div>
                    </div>
                    
                    <div class="stat-card">
                        <div class="stat-icon health-icon">
                            <i class="fas fa-heartbeat"></i>
                        </div>
                        <div class="stat-info">
                            <h3>3</h3>
                            <p>Alertes santé</p>
                        </div>
                    </div>
                    
                    <div class="stat-card">
                        <div class="stat-icon food-icon">
                            <i class="fas fa-utensils"></i>
                        </div>
                        <div class="stat-info">
                            <h3>82%</h3>
                            <p>Niveau stock alimentation</p>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Quick Actions -->
            <div class="stats-section">
                <h2 class="section-title"><i class="fas fa-bolt"></i> Actions rapides</h2>
                
                <div class="quick-actions">
                    <div class="action-card">
                        <div class="action-icon"><i class="fas fa-plus"></i></div>
                        <div class="action-text">Nouvelle traite</div>
                    </div>
                    
                    <div class="action-card">
                        <div class="action-icon"><i class="fas fa-notes-medical"></i></div>
                        <div class="action-text">Enregistrer soin</div>
                    </div>
                    
                    <div class="action-card">
                        <div class="action-icon"><i class="fas fa-clipboard-list"></i></div>
                        <div class="action-text">Vérifier stock</div>
                    </div>
                    
                    <div class="action-card">
                        <div class="action-icon"><i class="fas fa-syringe"></i></div>
                        <div class="action-text">Programmer vaccination</div>
                    </div>
                </div>
            </div>
            
            <!-- Recent Activities -->
            <div class="recent-activities">
                <div class="activities-header">
                    <h2 class="activities-title"><i class="fas fa-history"></i> Activités récentes</h2>
                    <a href="#" class="view-all">Voir tout</a>
                </div>
                
                <ul class="activity-list">
                    <li class="activity-item">
                        <div class="activity-icon" style="background-color: #E8F5E9; color: #4CAF50;">
                            <i class="fas fa-syringe"></i>
                        </div>
                        <div class="activity-content">
                            <p class="activity-text">Vaccination de 5 génisses effectuée par Dr. Martin</p>
                            <span class="activity-time">Il y a 2 heures</span>
                        </div>
                    </li>
                    
                    <li class="activity-item">
                        <div class="activity-icon" style="background-color: #E3F2FD; color: #2196F3;">
                            <i class="fas fa-tint"></i>
                        </div>
                        <div class="activity-content">
                            <p class="activity-text">Traite du matin complétée - 1245L collectés</p>
                            <span class="activity-time">Il y a 4 heures</span>
                        </div>
                    </li>
                    
                    <li class="activity-item">
                        <div class="activity-icon" style="background-color: #FFF8E1; color: #FFC107;">
                            <i class="fas fa-truck-loading"></i>
                        </div>
                        <div class="activity-content">
                            <p class="activity-text">Livraison d'aliments reçue - 2 tonnes de fourrage</p>
                            <span class="activity-time">Hier, 15:30</span>
                        </div>
                    </li>
                    
                    <li class="activity-item">
                        <div class="activity-icon" style="background-color: #FFEBEE; color: #F44336;">
                            <i class="fas fa-exclamation-triangle"></i>
                        </div>
                        <div class="activity-content">
                            <p class="activity-text">Alerte: Stock d'aliments critique - Commander ASAP</p>
                            <span class="activity-time">Hier, 11:45</span>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
        
        <!-- Autres sections (Structure placeholder) -->
        <div v-show="activeSection === 'statistics'" class="content-section">
            <div class="module-content">
                <div class="module-header">
                    <h2 class="module-title"><i class="fas fa-chart-line"></i> Statistiques de production</h2>
                </div>
                <p>Graphiques et analyses statistiques sur la production laitière.</p>
            </div>
        </div>
        
        <div v-show="activeSection === 'notifications'" class="content-section">
            <div class="module-content">
                <div class="module-header">
                    <h2 class="module-title"><i class="fas fa-bell"></i> Notifications</h2>
                </div>
                <p>Liste des alertes et notifications du système.</p>
            </div>
        </div>
        
        <div v-show="activeSection === 'personnel'" class="content-section">
            <div class="module-content">
                <div class="module-header">
                    <h2 class="module-title"><i class="fas fa-users"></i> Gestion du personnel</h2>
                </div>
                <p>Interface de gestion des employés de la ferme.</p>
            </div>
        </div>

        <!-- Generic Placeholder for other sections -->
        <div v-show="!['overview', 'statistics', 'notifications', 'personnel'].includes(activeSection)" class="content-section">
             <div class="module-content">
                <div class="module-header">
                    <h2 class="module-title"><i class="fas fa-info-circle"></i> {{ activeSection }}</h2>
                </div>
                <p>Section {{ activeSection }} en cours de développement.</p>
            </div>
        </div>
        
    </div>
</template>
