import api from './api';

// Auth
export const login = async (data) => await api.post('api/token/', data);
export const refresh = async (data) => await api.post('api/token/refresh/', data);

// Generic CRUD helper
const createResource = (endpoint) => ({
  list: async () => await api.get(`${endpoint}/`),
  get: async (id) => await api.get(`${endpoint}/${id}/`),
  create: async (data) => await api.post(`${endpoint}/`, data),
  update: async (id, data) => await api.put(`${endpoint}/${id}/`, data),
  patch: async (id, data) => await api.patch(`${endpoint}/${id}/`, data),
  delete: async (id) => await api.delete(`${endpoint}/${id}/`),
});

export const CowsApi = createResource('cows');
export const BarnsApi = createResource('barns');
export const AnalysisParametersApi = createResource('analysis-parameters');
export const CowBiologicalAnalysisApi = createResource('cow-biological-analysis');
export const FoodApi = createResource('food');
export const CowFeedingApi = createResource('cow-feeding');
export const CowHealthApi = createResource('cow-health');
export const EmployeesApi = createResource('employees');
export const EmployeeTasksApi = createResource('employee-tasks');
export const FoodAnalysisApi = createResource('food-analysis');
export const ResourcesApi = createResource('resources');
export const SuppliersApi = createResource('suppliers');
export const PurchaseOrdersApi = createResource('purchase-orders');
export const GoodsReceiptNotesApi = createResource('goods-receipt-notes');
export const GoodsReceiptDetailsApi = createResource('goods-receipt-details');
export const MachinesApi = createResource('machines');
export const MilkProductionApi = createResource('milk-production');
export const MilkAnalysisApi = createResource('milk-analysis');
export const PurchaseOrderItemsApi = createResource('purchase-order-items');
export const SparePartsApi = createResource('spare-parts');
export const UsersApi = createResource('users');

// Backward compatibility or convenience exports if needed (optional)
// export const getCows = CowsApi.list;
