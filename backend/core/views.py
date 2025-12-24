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


class CowsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Cows.objects.all()
        serializer = CowsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = CowsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BarnsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Barns.objects.all()
        serializer = BarnsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = BarnsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnalysisParametersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = AnalysisParameters.objects.all()
        serializer = AnalysisParametersSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = AnalysisParametersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CowBiologicalAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = CowBiologicalAnalysis.objects.all()
        serializer = CowBiologicalAnalysisSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = CowBiologicalAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Food.objects.all()
        serializer = FoodSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CowFeedingView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = CowFeeding.objects.all()
        serializer = CowFeedingSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = CowFeedingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CowHealthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = CowHealth.objects.all()
        serializer = CowHealthSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = CowHealthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Employees.objects.all()
        serializer = EmployeesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = EmployeesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = EmployeeTasks.objects.all()
        serializer = EmployeeTasksSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = EmployeeTasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = FoodAnalysis.objects.all()
        serializer = FoodAnalysisSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = FoodAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourcesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Resources.objects.all()
        serializer = ResourcesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = ResourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SuppliersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Suppliers.objects.all()
        serializer = SuppliersSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = SuppliersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = PurchaseOrders.objects.all()
        serializer = PurchaseOrdersSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PurchaseOrdersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsReceiptNotesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = GoodsReceiptNotes.objects.all()
        serializer = GoodsReceiptNotesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = GoodsReceiptNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsReceiptDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = GoodsReceiptDetails.objects.all()
        serializer = GoodsReceiptDetailsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = GoodsReceiptDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MachinesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = Machines.objects.all()
        serializer = MachinesSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = MachinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilkProductionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = MilkProduction.objects.all()
        serializer = MilkProductionSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = MilkProductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MilkAnalysisView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = MilkAnalysis.objects.all()
        serializer = MilkAnalysisSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = MilkAnalysisSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = PurchaseOrderItems.objects.all()
        serializer = PurchaseOrderItemsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = PurchaseOrderItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SparePartsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = SpareParts.objects.all()
        serializer = SparePartsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = SparePartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAuthView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        items = UserAuth.objects.all()
        serializer = UserAuthSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != UserAuth.Roles.ADMIN:
            return Response({"detail": "Admin only"}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
