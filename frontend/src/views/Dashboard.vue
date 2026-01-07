<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <p>Welcome to the Dairy Farm Management System.</p>
    <div class="actions">
      <router-link to="/cows" class="btn">View Cows</router-link>
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 20px;
}
.actions {
  margin-top: 20px;
}
.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}
.btn:hover {
  background-color: #45a049;
}
</style>
