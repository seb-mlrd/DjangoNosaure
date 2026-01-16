<script setup>
  import { onMounted } from "vue"
  import { useDinosaurs } from "@/composables/useDinosaurs"

  const { dinosaurs, loading, error, fetchDinosaurs } = useDinosaurs()

  onMounted(async () => {
    await fetchDinosaurs()
  })
</script>

<template>
  <div class="dino-page">
    <h1>🦖 Encyclopédie des dinosaures</h1>

    <p v-if="loading">Chargement...</p>
    <p v-if="error" class="error">{{ error }}</p>

    <div v-if="!loading" class="dino-grid">
      <article
        v-for="dino in dinosaurs"
        :key="dino.id"
        class="dino-card"
      >
        <h2>{{ dino.name }}</h2>

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
            </li>
          </ul>
        <router-link :to="`/dinos/${dino.id}`" class="dino-link">
          <button>Voir détails</button>
        </router-link>
        </div>
      </article>
    </div>
  </div>
</template>

<style scoped>
  .dino-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.8rem;
    margin-top: 2rem;
  }

  .dino-card {
    background: radial-gradient(circle at top, #2e3f34, #1b2620);
    border: 1px solid #3e5a4b;
    border-radius: 18px;
    padding: 1.6rem;
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

  .dino-card h2 {
    margin: 0 0 1rem;
    font-size: 1.6rem;
    color: #cddc39;
    border-bottom: 1px solid rgba(205, 220, 57, 0.4);
    padding-bottom: 0.4rem;
  }

  .dino-info p {
    margin: 0.4rem 0;
    font-size: 0.95rem;
    color: #d0d0d0;
  }

  .dino-info strong {
    color: #aed581;
  }

  .dino-locations {
    margin-top: 1rem;
  }

  .dino-locations .label {
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
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.4);
  }
</style>
