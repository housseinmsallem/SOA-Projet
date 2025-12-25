from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("cows/", views.CowsView.as_view()),
    path("barns/", views.BarnsView.as_view()),
    path("analysis-parameters/", views.AnalysisParametersView.as_view()),
    path("cow-biological-analysis/", views.CowBiologicalAnalysisView.as_view()),
    path("food/", views.FoodView.as_view()),
    path("cow-feeding/", views.CowFeedingView.as_view()),
    path("cow-health/", views.CowHealthView.as_view()),
    path("employees/", views.EmployeesView.as_view()),
    path("employee-tasks/", views.EmployeeTasksView.as_view()),
    path("food-analysis/", views.FoodAnalysisView.as_view()),
    path("resources/", views.ResourcesView.as_view()),
    path("suppliers/", views.SuppliersView.as_view()),
    path("purchase-orders/", views.PurchaseOrdersView.as_view()),
    path("goods-receipt-notes/", views.GoodsReceiptNotesView.as_view()),
    path("goods-receipt-details/", views.GoodsReceiptDetailsView.as_view()),
    path("machines/", views.MachinesView.as_view()),
    path("milk-production/", views.MilkProductionView.as_view()),
    path("milk-analysis/", views.MilkAnalysisView.as_view()),
    path("purchase-order-items/", views.PurchaseOrderItemsView.as_view()),
    path("spare-parts/", views.SparePartsView.as_view()),
    path("users/", views.UserAuthView.as_view()),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
