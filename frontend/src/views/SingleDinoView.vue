<script setup>
import { onMounted } from "vue"
import { useDinosaurs } from "@/composables/useDinosaurs"
import { useRoute } from "vue-router"

const route = useRoute()
const dinoId = route.params.id

const { dinosaurs, loading, error, fetchDinosaurById } = useDinosaurs()

onMounted(async () => {
  fetchDinosaurById(dinoId)
})
console.log(dinosaurs)
</script>
<template>
  <div class="dino-details-page">
    <p v-if="loading">Chargement...</p>
    <p v-if="error" class="error">{{ error }}</p>

    <div v-if="!loading" class="dino-details-card">
      <h1>{{ dinosaurs.name }} 🦖</h1>

      <div class="dino-main">
        <img v-if="dinosaurs.image" :src="dinosaurs.image" :alt="dinosaurs.name" class="dino-image" />
        <div class="dino-info">
          <p v-if="dinosaurs.taille"><strong>Taille :</strong> {{ dinosaurs.taille }} m</p>
          <p v-if="dinosaurs.poid"><strong>Poids :</strong> {{ dinosaurs.poid }} kg</p>
          <p v-if="dinosaurs.periode"><strong>Période :</strong> {{ dinosaurs.periode.name }}</p>
          <p v-if="dinosaurs.alimentation"><strong>Alimentation :</strong> {{ dinosaurs.alimentation.name }}</p>
        </div>
      </div>

      <div
        v-if="dinosaurs.localisation && dinosaurs.localisation.length"
        class="dino-locations"
      >
        <p v-if="dinosaurs.localisation" class="label">Localisation</p>
        <ul>
          <li v-for="loc in dinosaurs.localisation" :key="loc.id">
            {{ loc.continent }}
          </li>
        </ul>
      </div>
      <div 
        v-if="dinosaurs.fact" 
        class="dino-fact"
      >
        {{ dinosaurs.fact}}
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

.dino-fact {
  margin-top: 2rem;
  padding: 1rem;
  background: #394d36;
  border-left: 5px solid #aed581;
  color: #e0e0e0;
  font-style: italic;
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.5);
  white-space: pre-line;
}
</style>
