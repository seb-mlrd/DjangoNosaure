<script setup>
import { RouterLink } from "vue-router"
</script>

<template>
  <section class="home-page">
    <header class="hero">
      <h1>🦖 DinoDex</h1>
      <p>
        Une encyclopédie moderne dédiée aux dinosaures.
        Explore les espèces, leurs périodes et leurs habitats.
      </p>

      <RouterLink to="/dinos" class="cta">
        Explorer les dinosaures
      </RouterLink>
    </header>

    <section class="features">
      <article>
        <h2>🦴 Espèces</h2>
        <p>Découvrez des dizaines de dinosaures détaillés.</p>
      </article>

      <article>
        <h2>🌍 Localisation</h2>
        <p>Où vivaient-ils ? Sur quels continents ?</p>
      </article>

      <article>
        <h2>⏳ Périodes</h2>
        <p>Du Trias au Crétacé.</p>
      </article>
    </section>
  </section>
</template>

<style scoped>
.home-page {
  min-height: 100vh;
  background: linear-gradient(180deg, #0f1a14, #1e2d24);
  color: #eaeaea;
  padding: 3rem 2rem;
  font-family: "Trebuchet MS", "Segoe UI", sans-serif;
}

/* Hero */
.hero {
  max-width: 800px;
  margin: 0 auto 4rem;
  text-align: center;
}

.hero h1 {
  font-size: 3rem;
  color: #cddc39;
  letter-spacing: 3px;
  margin-bottom: 1.2rem;
  text-shadow: 0 0 12px rgba(205, 220, 57, 0.6);
}

.hero p {
  font-size: 1.15rem;
  color: #cfd8dc;
  line-height: 1.7;
}

/* CTA */
.cta {
  display: inline-block;
  margin-top: 2rem;
  padding: 0.9rem 2.2rem;
  background: #8bc34a;
  color: #0f1a14;
  font-weight: bold;
  border-radius: 999px;
  text-decoration: none;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.cta:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.6);
}

/* Features */
.features {
  max-width: 1000px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 2rem;
}

.features article {
  background: radial-gradient(circle at top, #2e3f34, #1b2620);
  border: 1px solid #3e5a4b;
  border-radius: 18px;
  padding: 1.6rem;
  text-align: center;
  box-shadow:
    0 8px 20px rgba(0, 0, 0, 0.7),
    inset 0 0 12px rgba(0, 0, 0, 0.4);
}

.features h2 {
  color: #aed581;
  margin-bottom: 0.6rem;
}

.features p {
  font-size: 0.95rem;
  color: #d0d0d0;
}
</style>
