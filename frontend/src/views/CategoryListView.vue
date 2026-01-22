<script setup>
import { onMounted } from "vue"
import { useCategory } from "@/composables/useCategory"

const { category, loading, error, fetchAllCategory } = useCategory()

onMounted(async () => {
  await fetchAllCategory()
})
</script>

<template>
  <div class="category-page">
    <h1>🦖 Catégories de Dinosaures</h1>

    <p v-if="loading">Chargement...</p>
    <p v-if="error" class="error">{{ error }}</p>

    <div v-if="!loading" class="category-grid">
      <router-link
        v-for="cate in category"
        :key="cate.id"
        :to="`/categorie/${cate.id}`"
        class="category-card"
      >
        <h2>{{ cate.name }}</h2>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.category-page {
  max-width: 1200px;
  margin: 2rem auto;
  padding: 1rem;
}

.category-page h1 {
  text-align: center;
  font-size: 2.4rem;
  color: #cddc39;
}

/* GRID */
.category-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1.8rem;
  margin-top: 2.5rem;
}

/* CARD */
.category-card {
  background: radial-gradient(circle at top, #2e3f34, #1b2620);
  border: 1px solid #3e5a4b;
  border-radius: 18px;
  padding: 2.2rem 1.5rem;
  text-decoration: none;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow:
    0 10px 24px rgba(0, 0, 0, 0.7),
    inset 0 0 15px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* HOVER */
.category-card:hover {
  transform: translateY(-8px) scale(1.05);
  box-shadow:
    0 16px 36px rgba(0, 0, 0, 0.9),
    inset 0 0 20px rgba(0, 0, 0, 0.5);
}

/* TITLE */
.category-card h2 {
  font-size: 1.6rem;
  color: #aed581;
  margin: 0;
  text-align: center;
  letter-spacing: 1px;
}

/* ERROR */
.error {
  color: #e57373;
  text-align: center;
  margin-top: 1rem;
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .category-page h1 {
    font-size: 2rem;
  }
}
</style>
