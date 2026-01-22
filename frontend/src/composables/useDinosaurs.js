import { ref } from 'vue'
import api from '@/services/api'

/**
 * Composable pour gérer les données des dinosaures
 * @returns {Object} - État et méthodes pour interagir avec l'API dinosaures
 */
export function useDinosaurs() {
  const dinosaurs = ref([])
  const loading = ref(false)
  const error = ref(null)

  /**
   * Récupère la liste de tous les dinosaures
   */
  const fetchDinosaurs = async () => {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.get('dinosaure/')
      dinosaurs.value = response.data.results || response.data
      return dinosaurs.value
    } catch (err) {
      error.value = `Erreur lors du chargement: ${err.message}`
      console.error('Error fetching dinosaurs:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  /**
   * Récupère un dinosaure par son ID
   * @param {number} id - L'ID du dinosaure
   */
  const fetchDinosaurById = async (id) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.get(`dinosaure/${id}/`)
      dinosaurs.value = response.data
      return dinosaurs.value
    } catch (err) {
      error.value = `Erreur lors du chargement du dinosaure: ${err.message}`
      console.error('Error fetching dinosaur:', err)
      throw err
    } finally {
      loading.value = false
    }
  }
  
  /**
   * Récupère les dinosaures par nom de catégorie
   * @param {string} categoryName - Le nom de la catégorie
   */
  const fetchDinosaurByCategoryName = async (categoryName) => {
    loading.value = true
    error.value = false

    try {
        const response = api.get(`dinosaure/${categoryName}`)
        return (await response).data
    }catch(err) {
        error.value = `Erreur lors du chargement du dinosaure: ${err.message}`
        console.error('Error fetching dinosaur:', err)
        throw err
    } finally {
        loading.value = false
    }
  }

  /**
   * Crée un nouveau dinosaure
   * @param {Object} dinosaurData - Les données du dinosaure
   */
  const createDinosaur = async (dinosaurData) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.post('dinosaure/', dinosaurData)
      dinosaurs.value.push(response.data)
      return response.data
    } catch (err) {
      error.value = `Erreur lors de la création: ${err.message}`
      console.error('Error creating dinosaur:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  /**
   * Met à jour un dinosaure existant
   * @param {number} id - L'ID du dinosaure
   * @param {Object} dinosaurData - Les nouvelles données
   */
  const updateDinosaur = async (id, dinosaurData) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.put(`dinosaure/${id}/`, dinosaurData)
      const index = dinosaurs.value.findIndex(d => d.id === id)
      if (index !== -1) {
        dinosaurs.value[index] = response.data
      }
      return response.data
    } catch (err) {
      error.value = `Erreur lors de la mise à jour: ${err.message}`
      console.error('Error updating dinosaur:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  /**
   * Supprime un dinosaure
   * @param {number} id - L'ID du dinosaure à supprimer
   */
  const deleteDinosaur = async (id) => {
    loading.value = true
    error.value = null
    
    try {
      await api.delete(`dinosaure/${id}/`)
      dinosaurs.value = dinosaurs.value.filter(d => d.id !== id)
    } catch (err) {
      error.value = `Erreur lors de la suppression: ${err.message}`
      console.error('Error deleting dinosaur:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

    /**
   * Récupère la liste des dinosaures par type d'alimentation
   */
  const fetchDinosaursByAlimentation = async (alimentationType) => {
    loading.value = true
    error.value = null
    
    try {
      const response = await api.get('dinosaure/')
      const dinoList = response.data.results || response.data
      const filteredDinosaurs = dinoList.filter(dino => 
        dino.alimentation?.name.toLowerCase() === alimentationType
      )
      dinosaurs.value = filteredDinosaurs
      return dinosaurs.value
    } catch (err) {
      error.value = `Erreur lors du chargement: ${err.message}`
      console.error('Error fetching dinosaurs:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  return {
    // État
    dinosaurs,
    loading,
    error,
    
    // Méthodes
    fetchDinosaurs,
    fetchDinosaurById,
    fetchDinosaurByCategoryName,
    fetchDinosaursByAlimentation,
    createDinosaur,
    updateDinosaur,
    deleteDinosaur
  }
}
