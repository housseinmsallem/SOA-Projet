
import { ref } from 'vue';
import { login } from '../api/resources.api';

export default async function useAuth(credentials) {
  const loading = ref(true);
  const error = ref(null);
  
  try {
    const response = await login(credentials);
    const token = response.data.access; // Assuming SimpleJWT returns { access, refresh }
    const refresh = response.data.refresh;
    
    localStorage.setItem('token', token);
    localStorage.setItem('refresh_token', refresh);
    
    return { success: true };
  } catch (err) {
    error.value = err.response?.data?.detail || err.message;
    throw new Error(error.value);
  } finally {
    loading.value = false;
  }
}

