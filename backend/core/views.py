from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
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


class BaseCoreView(APIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        # DjangoModelPermissions requires this method
        return self.model.objects.all()


class CowsView(BaseCoreView):
    model = Cows

    def get(self, request):
        items = Cows.objects.all()
        serializer = CowsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CowsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BarnsView(BaseCoreView):
    model = Barns

    def get(self, request):
        items = Barns.objects.all()
        serializer = BarnsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BarnsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnalysisParametersView(BaseCoreView):
    model = AnalysisParameters

    def get(self, request):
        items = AnalysisParameters.objects.all()
        serializer = AnalysisParametersSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnalysisParametersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CowBiologicalAnalysisView(BaseCoreView):
    model = CowBiologicalAnalysis

    def get(self, request):
        items = CowBiologicalAnalysis.objects.all()
        serializer = CowBiologicalAnalysisSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CowBiologicalAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodView(BaseCoreView):
    model = Food

    def get(self, request):
        items = Food.objects.all()
        serializer = FoodSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CowFeedingView(BaseCoreView):
    model = CowFeeding

    def get(self, request):
        items = CowFeeding.objects.all()
        serializer = CowFeedingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CowFeedingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CowHealthView(BaseCoreView):
    model = CowHealth

    def get(self, request):
        items = CowHealth.objects.all()
        serializer = CowHealthSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CowHealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeesView(BaseCoreView):
    model = Employees

    def get(self, request):
        items = Employees.objects.all()
        serializer = EmployeesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeTasksView(BaseCoreView):
    model = EmployeeTasks

    def get(self, request):
        items = EmployeeTasks.objects.all()
        serializer = EmployeeTasksSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeTasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodAnalysisView(BaseCoreView):
    model = FoodAnalysis

    def get(self, request):
        items = FoodAnalysis.objects.all()
        serializer = FoodAnalysisSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourcesView(BaseCoreView):
    model = Resources

    def get(self, request):
        items = Resources.objects.all()
        serializer = ResourcesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ResourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SuppliersView(BaseCoreView):
    model = Suppliers

    def get(self, request):
        items = Suppliers.objects.all()
        serializer = SuppliersSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrdersView(BaseCoreView):
    model = PurchaseOrders

    def get(self, request):
        items = PurchaseOrders.objects.all()
        serializer = PurchaseOrdersSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsReceiptNotesView(BaseCoreView):
    model = GoodsReceiptNotes

    def get(self, request):
        items = GoodsReceiptNotes.objects.all()
        serializer = GoodsReceiptNotesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GoodsReceiptNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsReceiptDetailsView(BaseCoreView):
    model = GoodsReceiptDetails

    def get(self, request):
        items = GoodsReceiptDetails.objects.all()
        serializer = GoodsReceiptDetailsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GoodsReceiptDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MachinesView(BaseCoreView):
    model = Machines

    def get(self, request):
        items = Machines.objects.all()
        serializer = MachinesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MachinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilkProductionView(BaseCoreView):
    model = MilkProduction

    def get(self, request):
        items = MilkProduction.objects.all()
        serializer = MilkProductionSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MilkProductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilkAnalysisView(BaseCoreView):
    model = MilkAnalysis

    def get(self, request):
        items = MilkAnalysis.objects.all()
        serializer = MilkAnalysisSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MilkAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderItemsView(BaseCoreView):
    model = PurchaseOrderItems

    def get(self, request):
        items = PurchaseOrderItems.objects.all()
        serializer = PurchaseOrderItemsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PurchaseOrderItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SparePartsView(BaseCoreView):
    model = SpareParts

    def get(self, request):
        items = SpareParts.objects.all()
        serializer = SparePartsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SparePartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuthView(BaseCoreView):
    model = UserAuth

    def get(self, request):
        items = UserAuth.objects.all()
        serializer = UserAuthSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
