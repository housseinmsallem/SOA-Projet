from django.db import models
from django.contrib.auth.models import AbstractUser

class AnalysisParameters(models.Model):
    parameter_id = models.AutoField(db_column='ParameterID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    unit = models.CharField(db_column='Unit', max_length=20, null=True, blank=True)
    min_value = models.DecimalField(db_column='MinValue', max_digits=10, decimal_places=2, null=True, blank=True)
    max_value = models.DecimalField(db_column='MaxValue', max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.CharField(db_column='Description', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'AnalysisParameters'

    def __str__(self):
        return self.name

class Barns(models.Model):
    barn_id = models.AutoField(db_column='BarnID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    capacity = models.IntegerField(db_column='Capacity')
    location = models.CharField(db_column='Location', max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'Barns'

    def __str__(self):
        return self.name

class Cows(models.Model):
    cow_id = models.AutoField(db_column='CowID', primary_key=True)
    barn = models.ForeignKey(Barns, models.DO_NOTHING, db_column='BarnID')
    ear_tag_number = models.CharField(db_column='EarTagNumber', max_length=50, unique=True)
    breed = models.CharField(db_column='Breed', max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(db_column='DateOfBirth')
    gender = models.CharField(db_column='Gender', max_length=10)
    weight = models.DecimalField(db_column='Weight', max_digits=10, decimal_places=2, null=True, blank=True)
    health_status = models.CharField(db_column='HealthStatus', max_length=50, null=True, blank=True)
    last_milking_date = models.DateField(db_column='LastMilkingDate', null=True, blank=True)

    class Meta:
        db_table = 'Cows'

    def __str__(self):
        return self.ear_tag_number

class CowBiologicalAnalysis(models.Model):
    analysis_id = models.AutoField(db_column='AnalysisID', primary_key=True)
    cow = models.ForeignKey(Cows, models.DO_NOTHING, db_column='CowID')
    parameter = models.ForeignKey(AnalysisParameters, models.DO_NOTHING, db_column='ParameterID')
    date = models.DateField(db_column='Date')
    value = models.DecimalField(db_column='Value', max_digits=10, decimal_places=2, null=True, blank=True)
    result = models.CharField(db_column='Result', max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'CowBiologicalAnalysis'

class Food(models.Model):
    food_id = models.AutoField(db_column='FoodID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    type = models.CharField(db_column='Type', max_length=50)
    category = models.CharField(db_column='Category', max_length=50, null=True, blank=True)
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2)
    unit = models.CharField(db_column='Unit', max_length=20, null=True, blank=True)
    reorder_level = models.DecimalField(db_column='ReorderLevel', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'Food'

    def __str__(self):
        return self.name

class CowFeeding(models.Model):
    feeding_id = models.AutoField(db_column='FeedingID', primary_key=True)
    cow = models.ForeignKey(Cows, models.DO_NOTHING, db_column='CowID')
    food = models.ForeignKey(Food, models.DO_NOTHING, db_column='FoodID')
    date = models.DateField(db_column='Date')
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'CowFeeding'

class CowHealth(models.Model):
    health_id = models.AutoField(db_column='HealthID', primary_key=True)
    cow = models.ForeignKey(Cows, models.DO_NOTHING, db_column='CowID')
    date = models.DateField(db_column='Date')
    type = models.CharField(db_column='Type', max_length=50)
    description = models.CharField(db_column='Description', max_length=255, null=True, blank=True)
    vet_name = models.CharField(db_column='VetName', max_length=100, null=True, blank=True)
    next_checkup_date = models.DateField(db_column='NextCheckupDate', null=True, blank=True)

    class Meta:
        db_table = 'CowHealth'

class Employees(models.Model):
    employee_id = models.AutoField(db_column='EmployeeID', primary_key=True)
    first_name = models.CharField(db_column='FirstName', max_length=100)
    last_name = models.CharField(db_column='LastName', max_length=100)
    role = models.CharField(db_column='Role_', max_length=50)
    base_salary = models.DecimalField(db_column='BaseSalary', max_digits=10, decimal_places=2)
    hourly_rate = models.DecimalField(db_column='HourlyRate', max_digits=10, decimal_places=2)
    hire_date = models.DateField(db_column='HireDate')

    class Meta:
        db_table = 'Employees'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployeeTasks(models.Model):
    task_id = models.AutoField(db_column='TaskID', primary_key=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EmployeeID')
    task_description = models.CharField(db_column='TaskDescription', max_length=255, null=True, blank=True)
    hours_worked = models.DecimalField(db_column='HoursWorked', max_digits=5, decimal_places=2, null=True, blank=True)
    task_date = models.DateField(db_column='TaskDate')

    class Meta:
        db_table = 'EmployeeTasks'

class FoodAnalysis(models.Model):
    analysis_id = models.AutoField(db_column='AnalysisID', primary_key=True)
    food = models.ForeignKey(Food, models.DO_NOTHING, db_column='FoodID')
    analysis_date = models.DateField(db_column='AnalysisDate')
    parameter = models.ForeignKey(AnalysisParameters, models.DO_NOTHING, db_column='ParameterID')
    value = models.DecimalField(db_column='Value', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'FoodAnalysis'

class Resources(models.Model):
    resource_id = models.AutoField(db_column='ResourceID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    type = models.CharField(db_column='Type', max_length=50, null=True, blank=True)
    category = models.CharField(db_column='Category', max_length=50, null=True, blank=True)
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2)
    unit = models.CharField(db_column='Unit', max_length=20, null=True, blank=True)
    reorder_level = models.DecimalField(db_column='ReorderLevel', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'Resources'
    
    def __str__(self):
        return self.name

class Suppliers(models.Model):
    supplier_id = models.AutoField(db_column='SupplierID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    contact_info = models.CharField(db_column='ContactInfo', max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Suppliers'

    def __str__(self):
        return self.name

class PurchaseOrders(models.Model):
    order_id = models.AutoField(db_column='OrderID', primary_key=True)
    supplier = models.ForeignKey(Suppliers, models.DO_NOTHING, db_column='SupplierID')
    order_date = models.DateField(db_column='OrderDate')
    status = models.CharField(db_column='Status', max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'PurchaseOrders'

class GoodsReceiptNotes(models.Model):
    grn_id = models.AutoField(db_column='GRNID', primary_key=True)
    order = models.ForeignKey(PurchaseOrders, models.DO_NOTHING, db_column='OrderID')
    receipt_date = models.DateField(db_column='ReceiptDate')
    status = models.CharField(db_column='Status', max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'GoodsReceiptNotes'

class GoodsReceiptDetails(models.Model):
    grn_detail_id = models.AutoField(db_column='GRNDetailID', primary_key=True)
    grn = models.ForeignKey(GoodsReceiptNotes, models.DO_NOTHING, db_column='GRNID')
    resource = models.ForeignKey(Resources, models.DO_NOTHING, db_column='ResourceID')
    received_quantity = models.DecimalField(db_column='ReceivedQuantity', max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'GoodsReceiptDetails'

class Machines(models.Model):
    machine_id = models.AutoField(db_column='MachineID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    type = models.CharField(db_column='Type', max_length=50, null=True, blank=True)
    last_maintenance = models.DateField(db_column='LastMaintenance', null=True, blank=True)
    next_maintenance = models.DateField(db_column='NextMaintenance', null=True, blank=True)

    class Meta:
        db_table = 'Machines'

    def __str__(self):
        return self.name

class MilkProduction(models.Model):
    production_id = models.AutoField(db_column='ProductionID', primary_key=True)
    cow = models.ForeignKey(Cows, models.DO_NOTHING, db_column='CowID')
    production_date = models.DateField(db_column='ProductionDate')
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2)
    quality = models.CharField(db_column='Quality', max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'MilkProduction'

class MilkAnalysis(models.Model):
    analysis_id = models.AutoField(db_column='AnalysisID', primary_key=True)
    milk_production = models.ForeignKey(MilkProduction, models.DO_NOTHING, db_column='MilkProductionID')
    analysis_date = models.DateField(db_column='AnalysisDate')
    parameter = models.ForeignKey(AnalysisParameters, models.DO_NOTHING, db_column='ParameterID')
    value = models.DecimalField(db_column='Value', max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'MilkAnalysis'

class PurchaseOrderItems(models.Model):
    resource = models.ForeignKey(Resources, models.DO_NOTHING, db_column='ResourceID')
    order = models.ForeignKey(PurchaseOrders, models.DO_NOTHING, db_column='OrderID')
    ordered_quantity = models.DecimalField(db_column='OrderedQuantity', max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'PurchaseOrderItems'
        unique_together = (('resource', 'order'),)

class SpareParts(models.Model):
    part_id = models.AutoField(db_column='PartID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=100)
    quantity = models.IntegerField(db_column='Quantity')
    reorder_level = models.IntegerField(db_column='ReorderLevel')

    class Meta:
        db_table = 'SpareParts'

class UserAuth(AbstractUser):
    role = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'User_Auth'
