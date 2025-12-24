from .models import (
    AnalysisParameters,
    Barns,
    Cows,
    CowFeeding,
    CowBiologicalAnalysis,
    Food,
    CowHealth,
    Employees,
    EmployeeTasks,
    FoodAnalysis,
    Resources,
    Suppliers,
    PurchaseOrderItems,
    PurchaseOrders,
    GoodsReceiptDetails,
    GoodsReceiptNotes,
    Machines,
    MilkProduction,
    MilkAnalysis,
    SpareParts,
    UserAuth,
)
from rest_framework import serializers


class AnalysisParametersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisParameters
        fields = "__all__"


class BarnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barns
        fields = ["name", "capacity", "location"]


class CowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cows
        fields = "__all__"


class CowBiologicalAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CowBiologicalAnalysis
        fields = "__all__"


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class CowFeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CowFeeding
        fields = "__all__"


class CowHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = CowHealth
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class EmployeeTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeTasks
        fields = "__all__"


class FoodAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodAnalysis
        fields = "__all__"


class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = "__all__"


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = "__all__"


class PurchaseOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrders
        fields = "__all__"


class GoodsReceiptNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsReceiptNotes
        fields = "__all__"


class GoodsReceiptDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsReceiptDetails
        fields = "__all__"


class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machines
        fields = "__all__"


class MilkProductionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkProduction
        fields = "__all__"


class MilkAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = MilkAnalysis
        fields = "__all__"


class PurchaseOrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderItems
        fields = "__all__"


class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = "__all__"


class UserAuthSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserAuth
        exclude = ("user_permissions", "groups")

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = UserAuth(**validated_data)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
