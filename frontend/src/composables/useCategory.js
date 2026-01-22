import { ref } from 'vue'
import api from '@/services/api'


export function useCategory() {
    const category = ref([])
    const loading = ref(false)
    const error = ref(null)

    const fetchAllCategory = async () => {
        loading.value = true
        error.value = null

        try {
            const response = await api.get('categorie/')
            category.value = response.data.results || response.data
            return category.value 
        }catch (err) {
            error.value = `Erreur lors du chargement: ${err.message}`
            console.error('Error fetching categories:', err)
            throw err
        }finally {
            loading.value = false
        }
    }
    
    const fetchCategoryById = async (id) => {
        loading.value = true
        error.value = null

        try {
            const response = await api.get(`categorie/${id}/`)
            category.value = response.data.results || response.data
            return category.value
        }catch (err) {
            error.value = `Erreur lors du chargement: ${err.message}`
            console.error('Error fetching category:', err)
            throw err
        } finally {
            loading.value = false
        }        
    }

    return {
        category,
        loading,
        error,

        fetchAllCategory,
        fetchCategoryById
    }
}