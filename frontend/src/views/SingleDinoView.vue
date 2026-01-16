<script setup>
import { onMounted } from "vue"
import { useDinosaurs } from "@/composables/useDinosaurs"
import { useRoute } from "vue-router"

const route = useRoute()
const dinoId = route.params.id

const { dinosaurs, loading, error, fetchDinosaurById } = useDinosaurs()
let dino = dinosaurs

onMounted(async () => {
  fetchDinosaurById(dinoId)
})
</script>

<template>
  <div class="dino-details-page">
    <p v-if="loading">Chargement...</p>
    <p v-if="error" class="error">{{ error }}</p>

    <div v-if="dino && !loading" class="dino-details-card">
      <h1>{{ dino.name }} 🦖</h1>

      <div class="dino-main">
        <img :src="dino.image.url" :alt="dino.name" class="dino-image" />

        <div class="dino-info">
          <p><strong>Taille :</strong> {{ dino.taille }} m</p>
          <p><strong>Poids :</strong> {{ dino.poid }} kg</p>
          <p><strong>Période :</strong> {{ dino.periode.name }}</p>
          <p><strong>Alimentation :</strong> {{ dino.alimentation.name }}</p>
          <p><strong>Découverte :</strong> {{ dino.fact }}</p>
        </div>
      </div>

      <div
        v-if="dino.localisation && dino.localisation.length"
        class="dino-locations"
      >
        <p class="label">Localisation</p>
        <ul>
          <li v-for="loc in dino.localisation" :key="loc.id">
            {{ loc.continent }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dino-details-page {
  max-width: 900px;
  margin: 2rem auto;
  padding: 1rem;
}

.dino-details-card {
  background: radial-gradient(circle at top, #2e3f34, #1b2620);
  border: 1px solid #3e5a4b;
  border-radius: 18px;
  padding: 2rem;
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.7),
    inset 0 0 15px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.dino-details-card:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 16px 36px rgba(0, 0, 0, 0.9),
    inset 0 0 20px rgba(0, 0, 0, 0.5);
}

.dino-details-card h1 {
  color: #cddc39;
  font-size: 2rem;
  border-bottom: 1px solid rgba(205, 220, 57, 0.4);
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
  text-align: center;
}

.dino-main {
  display: flex;
  flex-wrap: wrap;
  gap: 2rem;
  align-items: center;
  justify-content: center;
}

.dino-image {
  max-width: 300px;
  border-radius: 18px;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.6);
}

.dino-info p {
  margin: 0.5rem 0;
  font-size: 1rem;
  color: #d0d0d0;
}

.dino-info strong {
  color: #aed581;
}

.dino-locations {
  margin-top: 2rem;
  text-align: center;
}

.dino-locations .label {
  font-size: 0.85rem;
  color: #8bc34a;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.dino-locations ul {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: center;
  padding: 0;
  list-style: none;
}

.dino-locations li {
  background: #4a6b3c;
  color: #e8f5e9;
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  font-size: 0.85rem;
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.4);
}
</style>
