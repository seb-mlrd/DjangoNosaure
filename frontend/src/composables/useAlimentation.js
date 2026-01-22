import { ref } from 'vue'
import api from '@/services/api'


export function useAlimentation() {
    const alimentation = ref([])
    const loading = ref(false)
    const error = ref(null)

    const fetchAllAlimentation = async () => {
        loading.value = true
        error.value = null

        try {
            const response = await api.get('alimentation/')
            alimentation.value = response.data.results || response.data
            return alimentation.value 
        }catch (err) {
            error.value = `Erreur lors du chargement: ${err.message}`
            console.error('Error fetching alimentations:', err)
            throw err
        }finally {
            loading.value = false
        }
    }
    
    const fetchAlimentationById = async (id) => {
        loading.value = true
        error.value = null

        try {
            const response = await api.get(`alimentation/${id}/`)
            alimentation.value = response.data.results || response.data
            return alimentation.value
        }catch (err) {
            error.value = `Erreur lors du chargement: ${err.message}`
            console.error('Error fetching alimentation:', err)
            throw err
        } finally {
            loading.value = false
        }        
    }

    return {
        alimentation,
        loading,
        error,

        fetchAllAlimentation,
        fetchAlimentationById
    }
}