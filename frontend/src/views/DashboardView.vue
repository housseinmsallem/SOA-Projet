<template>
  <div class="content-section active">
    <!-- Stats Overview -->
    <div class="stats-section">
      <h2 class="section-title">
        <i class="fas fa-chart-line"></i> Aperçu des indicateurs
      </h2>

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
        <h2 class="activities-title">
          <i class="fas fa-history"></i> Activités récentes
        </h2>
        <a href="#" class="view-all">Voir tout</a>
      </div>

      <ul class="activity-list">
        <li class="activity-item">
          <div
            class="activity-icon"
            style="background-color: #e8f5e9; color: #4caf50"
          >
            <i class="fas fa-syringe"></i>
          </div>
          <div class="activity-content">
            <p class="activity-text">
              Vaccination de 5 génisses effectuée par Dr. Martin
            </p>
            <span class="activity-time">Il y a 2 heures</span>
          </div>
        </li>

        <li class="activity-item">
          <div
            class="activity-icon"
            style="background-color: #e3f2fd; color: #2196f3"
          >
            <i class="fas fa-tint"></i>
          </div>
          <div class="activity-content">
            <p class="activity-text">
              Traite du matin complétée - 1245L collectés
            </p>
            <span class="activity-time">Il y a 4 heures</span>
          </div>
        </li>

        <li class="activity-item">
          <div
            class="activity-icon"
            style="background-color: #fff8e1; color: #ffc107"
          >
            <i class="fas fa-truck-loading"></i>
          </div>
          <div class="activity-content">
            <p class="activity-text">
              Livraison d'aliments reçue - 2 tonnes de fourrage
            </p>
            <span class="activity-time">Hier, 15:30</span>
          </div>
        </li>

        <li class="activity-item">
          <div
            class="activity-icon"
            style="background-color: #ffebee; color: #f44336"
          >
            <i class="fas fa-exclamation-triangle"></i>
          </div>
          <div class="activity-content">
            <p class="activity-text">
              Alerte: Stock d'aliments critique - Commander ASAP
            </p>
            <span class="activity-time">Hier, 11:45</span>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
const data = ref([]);
const loading = ref(true);
const error = ref(null);
const fetchData = async () => {
  loading = true;
  error = null;
  try {
    const response = await fetch('http://localhost:8080/cows');
    if (!response.ok) {
      throw new Error('HTTP Error!');
    }
    this.data = await response.json();
  } catch (error) {
    this.error = error.message;
  } finally {
    this.loading = false;
  }
};
</script>
