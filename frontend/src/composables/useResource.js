import { ref } from 'vue';

export default function useResource(resourceApi) {
  const data = ref([]);
  const item = ref(null);
  const loading = ref(false);
  const error = ref(null);

  const fetchAll = async () => {
    loading.value = true;
    error.value = null;
    try {
      const response = await resourceApi.list();
      data.value = response.data;
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const fetchOne = async (id) => {
    loading.value = true;
    error.value = null;
    try {
      const response = await resourceApi.get(id);
      item.value = response.data;
      return response.data;
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const create = async (payload) => {
    loading.value = true;
    error.value = null;
    try {
      const response = await resourceApi.create(payload);
      data.value.push(response.data);
      return response.data;
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const update = async (id, payload) => {
    loading.value = true;
    error.value = null;
    try {
      const response = await resourceApi.update(id, payload);
      const index = data.value.findIndex((i) => i.id === id);
      if (index !== -1) {
        data.value[index] = response.data;
      }
      item.value = response.data;
      return response.data;
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  const remove = async (id) => {
    loading.value = true;
    error.value = null;
    try {
      await resourceApi.delete(id);
      data.value = data.value.filter((i) => i.id !== id);
    } catch (err) {
      error.value = err;
      throw err;
    } finally {
      loading.value = false;
    }
  };

  return {
    data,
    item,
    loading,
    error,
    fetchAll,
    fetchOne,
    create,
    update,
    remove,
  };
}
