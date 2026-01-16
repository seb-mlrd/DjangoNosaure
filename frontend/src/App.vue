<script setup>
  import { RouterView } from "vue-router"
</script>

<template>
  <div id="app">
    <header class="app-header">
      <h1 class="app-title">🦖 DinoSaur API</h1>

      <nav class="app-nav">
        <RouterLink to="/">Accueil</RouterLink>
        <RouterLink to="/dinos">Dinosaures</RouterLink>
        <RouterLink to="/categories">Categories</RouterLink>
      </nav>
    </header>

    <main class="app-content">
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
  /* App layout */
  #app {
    min-height: 100vh;
    background: linear-gradient(180deg, #0f1a14, #1e2d24);
    color: #eaeaea;
    font-family: "Trebuchet MS", "Segoe UI", sans-serif;
  }

  /* Header */
  .app-header {
    background: #0b120e;
    border-bottom: 2px solid #3e5a4b;
    padding: 1rem 2rem;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.7);
  }

  .app-title {
    margin: 0;
    font-size: 1.8rem;
    color: #cddc39;
    letter-spacing: 2px;
    text-shadow: 0 0 8px rgba(205, 220, 57, 0.5);
  }

  /* Navigation */
  .app-nav {
    margin-top: 0.5rem;
    display: flex;
    gap: 1.5rem;
  }

  .app-nav a {
    color: #8bc34a;
    text-decoration: none;
    font-weight: bold;
    position: relative;
  }

  .app-nav a::after {
    content: "";
    position: absolute;
    left: 0;
    bottom: -4px;
    width: 0;
    height: 2px;
    background: #cddc39;
    transition: width 0.3s ease;
  }

  .app-nav a:hover::after,
  .app-nav a.router-link-exact-active::after {
    width: 100%;
  }

  /* Content */
  .app-content {
    padding: 2rem;
  }
</style>
