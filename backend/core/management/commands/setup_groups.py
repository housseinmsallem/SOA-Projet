from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from core.models import (
    AnalysisParameters,
    Barns,
    Cows,
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


class Command(BaseCommand):
    help = "Setup Django groups and permissions based on user roles"

    def handle(self, *args, **options):
        roles = {
            "Administrateur": {
                "models": [
                    AnalysisParameters,
                    Barns,
                    Cows,
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
                ],
                "permissions": ["view", "add", "change", "delete"],
            },
            "Employe": {
                "models": [EmployeeTasks, CowFeeding, GoodsReceiptNotes, Cows, Barns],
                "permissions": ["view", "add"],
            },
            "Veterinaire": {
                "models": [CowBiologicalAnalysis, CowHealth, Cows],
                "permissions": ["view", "add"],
            },
            "Responsable_Production": {
                "models": [MilkProduction, MilkAnalysis, Cows, Barns],
                "permissions": ["view", "add"],
            },
        }

        for role_name, config in roles.items():
            group, created = Group.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created group: {role_name}"))

            permissions_to_add = []
            for model in config["models"]:
                content_type = ContentType.objects.get_for_model(model)
                for perm_code in config["permissions"]:
                    codename = f"{perm_code}_{model._meta.model_name}"
                    try:
                        permission = Permission.objects.get(
                            content_type=content_type, codename=codename
                        )
                        permissions_to_add.append(permission)
                    except Permission.DoesNotExist:
                        self.stdout.write(
                            self.style.WARNING(
                                f"Permission {codename} not found for {model.__name__}"
                            )
                        )

            group.permissions.set(permissions_to_add)
            self.stdout.write(
                self.style.SUCCESS(f"Updated permissions for group: {role_name}")
            )

        self.stdout.write(
            self.style.SUCCESS("Successfully setup groups and permissions")
        )
