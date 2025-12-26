from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import (
    Cows,
    Barns,
    AnalysisParameters,
    CowBiologicalAnalysis,
    Food,
    CowFeeding,
    CowHealth,
    Employees,
    EmployeeTasks,
    FoodAnalysis,
    Resources,
    Suppliers,
    PurchaseOrders,
    GoodsReceiptNotes,
    GoodsReceiptDetails,
    Machines,
    MilkProduction,
    MilkAnalysis,
    PurchaseOrderItems,
    SpareParts,
    UserAuth,
)
from .serializers import (
    CowsSerializer,
    BarnsSerializer,
    AnalysisParametersSerializer,
    CowBiologicalAnalysisSerializer,
    FoodSerializer,
    CowFeedingSerializer,
    CowHealthSerializer,
    EmployeesSerializer,
    EmployeeTasksSerializer,
    FoodAnalysisSerializer,
    ResourcesSerializer,
    SuppliersSerializer,
    PurchaseOrdersSerializer,
    GoodsReceiptNotesSerializer,
    GoodsReceiptDetailsSerializer,
    MachinesSerializer,
    MilkProductionSerializer,
    MilkAnalysisSerializer,
    PurchaseOrderItemsSerializer,
    SparePartsSerializer,
    UserAuthSerializer,
)
from .permissions import IsAdministrateur


class BaseCoreView(APIView):
    model = None
    serializer_class = None

    def get_permissions(self):
        return [IsAuthenticated()]

    def get_queryset(self):
        # DjangoModelPermissions requires this method
        return self.model.objects.all()

    def get(self, request, pk=None):
        if pk:
            try:
                item = self.model.objects.get(pk=pk)
                serializer = self.serializer_class(item)
                return Response(serializer.data)
            except self.model.DoesNotExist:
                return Response(
                    {"error": "Not found"}, status=status.HTTP_404_NOT_FOUND
                )

        items = self.get_queryset()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        # As per user request: if patch and put are the same, partial=True is used
        return self.patch(request, *args, **kwargs)

    def delete(self, request, pk):
        try:
            item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CowsView(BaseCoreView):
    model = Cows
    serializer_class = CowsSerializer


class BarnsView(BaseCoreView):
    model = Barns
    serializer_class = BarnsSerializer


class AnalysisParametersView(BaseCoreView):
    model = AnalysisParameters
    serializer_class = AnalysisParametersSerializer


class CowBiologicalAnalysisView(BaseCoreView):
    model = CowBiologicalAnalysis
    serializer_class = CowBiologicalAnalysisSerializer


class FoodView(BaseCoreView):
    model = Food
    serializer_class = FoodSerializer


class CowFeedingView(BaseCoreView):
    model = CowFeeding
    serializer_class = CowFeedingSerializer


class CowHealthView(BaseCoreView):
    model = CowHealth
    serializer_class = CowHealthSerializer


class EmployeesView(BaseCoreView):
    model = Employees
    serializer_class = EmployeesSerializer

    def get_permissions(self):
        permissions = super().get_permissions()
        if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
            permissions.append(IsAdministrateur())
        return permissions


class EmployeeTasksView(BaseCoreView):
    model = EmployeeTasks
    serializer_class = EmployeeTasksSerializer


class FoodAnalysisView(BaseCoreView):
    model = FoodAnalysis
    serializer_class = FoodAnalysisSerializer


class ResourcesView(BaseCoreView):
    model = Resources
    serializer_class = ResourcesSerializer


class SuppliersView(BaseCoreView):
    model = Suppliers
    serializer_class = SuppliersSerializer


class PurchaseOrdersView(BaseCoreView):
    model = PurchaseOrders
    serializer_class = PurchaseOrdersSerializer


class GoodsReceiptNotesView(BaseCoreView):
    model = GoodsReceiptNotes
    serializer_class = GoodsReceiptNotesSerializer


class GoodsReceiptDetailsView(BaseCoreView):
    model = GoodsReceiptDetails
    serializer_class = GoodsReceiptDetailsSerializer


class MachinesView(BaseCoreView):
    model = Machines
    serializer_class = MachinesSerializer


class MilkProductionView(BaseCoreView):
    model = MilkProduction
    serializer_class = MilkProductionSerializer


class MilkAnalysisView(BaseCoreView):
    model = MilkAnalysis
    serializer_class = MilkAnalysisSerializer


class PurchaseOrderItemsView(BaseCoreView):
    model = PurchaseOrderItems
    serializer_class = PurchaseOrderItemsSerializer


class SparePartsView(BaseCoreView):
    model = SpareParts
    serializer_class = SparePartsSerializer


class UserAuthView(BaseCoreView):
    model = UserAuth
    serializer_class = UserAuthSerializer
