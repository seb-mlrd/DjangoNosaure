<script setup>
import { onMounted, computed } from "vue"
import { useDinosaurs } from "@/composables/useDinosaurs"
import { useRoute } from "vue-router"

const route = useRoute()
const categoryId = parseInt(route.params.id)

const { dinosaurs, loading, error, fetchDinosaurs } = useDinosaurs()

const filteredDinosaurs = computed(() => {
  return dinosaurs.value.filter(dino => 
    dino.category && dino.category.length > 0 && 
    dino.category.some(cat => cat.id === categoryId)
  )
})

onMounted(async () => {
  await fetchDinosaurs()
})
</script>

<template>
  <div class="category-details-page">
    <h1>🦕 Dinosaures de cette catégorie</h1>
    <p class="subtitle">Découvrez tous les dinosaures appartenant à cette classification</p>

    <p v-if="loading">Chargement...</p>
    <p v-else-if="error" class="error">{{ error }}</p>
    <p v-else-if="filteredDinosaurs.length === 0" class="empty">
      Aucun dinosaure trouvé dans cette catégorie
    </p>

    <div v-else class="dino-grid">
      <article
        v-for="dino in filteredDinosaurs"
        :key="dino.id"
        class="dino-card"
      >
        <h2>{{ dino.name }}</h2>
        <p class="scientific-name">{{ dino.scientific_name }}</p>

        <div class="dino-info">
          <p><strong>Taille :</strong> {{ dino.taille }} m</p>
          <p><strong>Poids :</strong> {{ dino.poid }} kg</p>
          <p><strong>Période :</strong> {{ dino.periode.name }}</p>
          <p><strong>Alimentation :</strong> {{ dino.alimentation.name }}</p>
        </div>

        <div
          v-if="dino.localisation && dino.localisation.length"
          class="dino-locations"
        >
          <p class="label">Localisation</p>
          <ul>
            <li v-for="loc in dino.localisation" :key="loc.id">
              {{ loc.continent }}
              <span v-if="loc.country">({{ loc.country }})</span>
            </li>
          </ul>
        </div>

        <router-link
          :to="`/dino/${dino.id}`"
          class="details-link"
        >
          Voir les détails →
        </router-link>
      </article>
    </div>
  </div>
</template>


<style scoped>
.category-details-page {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 1rem;
}

h1 {
  text-align: center;
  font-size: 2.4rem;
  color: #cddc39;
}

.subtitle {
  text-align: center;
  color: #aed581;
  margin-top: 0.4rem;
}

.error {
  color: #e57373;
  text-align: center;
  margin-top: 2rem;
}

.empty {
  text-align: center;
  margin-top: 2rem;
  color: #ccc;
}

/* GRID */
.dino-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.8rem;
  margin-top: 2.5rem;
}

/* CARD */
.dino-card {
  background: radial-gradient(circle at top, #2e3f34, #1b2620);
  border: 1px solid #3e5a4b;
  border-radius: 18px;
  padding: 1.8rem;
  display: flex;
  flex-direction: column;
  box-shadow:
    0 10px 24px rgba(0, 0, 0, 0.7),
    inset 0 0 15px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.dino-card:hover {
  transform: translateY(-8px) scale(1.03);
  box-shadow:
    0 16px 36px rgba(0, 0, 0, 0.9),
    inset 0 0 20px rgba(0, 0, 0, 0.5);
}

/* TITLE */
.dino-card h2 {
  margin: 0;
  font-size: 1.6rem;
  color: #cddc39;
}

.scientific-name {
  font-size: 0.9rem;
  font-style: italic;
  color: #9ccc65;
  margin-bottom: 1rem;
}

/* INFO */
.dino-info p {
  margin: 0.4rem 0;
  font-size: 0.95rem;
  color: #d0d0d0;
}

.dino-info strong {
  color: #aed581;
}

/* LOCATIONS */
.dino-locations {
  margin-top: 1rem;
}

.label {
  font-size: 0.85rem;
  color: #8bc34a;
  margin-bottom: 0.4rem;
  text-transform: uppercase;
  letter-spacing: 1px;
}

.dino-locations ul {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding: 0;
  list-style: none;
}

.dino-locations li {
  background: #4a6b3c;
  color: #e8f5e9;
  padding: 0.35rem 0.7rem;
  border-radius: 999px;
  font-size: 0.8rem;
}

/* BUTTON */
.details-link {
  margin-top: auto;
  text-align: center;
  padding: 0.7rem;
  border-radius: 12px;
  background: #3e5a4b;
  color: #e8f5e9;
  text-decoration: none;
  font-weight: 600;
  transition: background 0.3s ease, transform 0.3s ease;
}

.details-link:hover {
  background: #4a6b3c;
  transform: translateY(-2px);
}

/* MOBILE */
@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }
}
</style>
