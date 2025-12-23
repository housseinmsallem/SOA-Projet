-- Seeding AnalysisParameters
INSERT INTO AnalysisParameters (Name, Unit, MinValue, MaxValue, Description) VALUES 
('Weight', 'kg', 100.00, 1500.00, 'Weight of the cow'),
('Milk Yield', 'L', 0.00, 50.00, 'Daily milk production'),
('Temperature', '°C', 38.00, 39.50, 'Body temperature');

-- Seeding Barns
INSERT INTO Barns (Name, Capacity, Location) VALUES 
('Main Barn', 50, 'North Sector'),
('Isolation Barn', 10, 'East Sector');

-- Seeding Cows (assuming BarnIDs 1 and 2)
INSERT INTO Cows (BarnID, EarTagNumber, Breed, DateOfBirth, Gender, Weight, HealthStatus, LastMilkingDate) VALUES 
(1, 'COW-001', 'Holstein', '2022-01-15', 'Female', 650.50, 'Healthy', '2023-12-20'),
(1, 'COW-002', 'Jersey', '2021-05-20', 'Female', 520.00, 'Healthy', '2023-12-21'),
(2, 'COW-003', 'Holstein', '2023-03-10', 'Female', 480.00, 'Under Observation', NULL);

-- Seeding Food
INSERT INTO Food (Name, Type, Category, Quantity, Unit, ReorderLevel) VALUES 
('Organic Hay', 'Dry', 'Forage', 1000.00, 'kg', 200.00),
('Corn Silage', 'Fermented', 'Forage', 5000.00, 'kg', 1000.00),
('Protein Mix', 'Grain', 'Supplement', 500.00, 'kg', 100.00);

-- Seeding Employees
INSERT INTO Employees (FirstName, LastName, Role_, BaseSalary, HourlyRate, HireDate) VALUES 
('John', 'Doe', 'Manager', 4000.00, 25.00, '2020-01-01'),
('Alice', 'Smith', 'Veterinarian', 4500.00, 30.00, '2021-06-15'),
('Bob', 'Wilson', 'Farm Hand', 2500.00, 15.00, '2022-03-01');

-- Seeding Suppliers
INSERT INTO Suppliers (Name, ContactInfo) VALUES 
('AgroCorp', 'contact@agrocorp.com'),
('FarmSupply Ltd', 'sales@farmsupply.com');

-- Seeding Resources
INSERT INTO Resources (Name, Type, Category, Quantity, Unit, ReorderLevel) VALUES 
('Vaccine Set A', 'Medical', 'Medicine', 100.00, 'pcs', 20.00),
('Cleaning Detergent', 'Chemical', 'Cleaning', 50.00, 'L', 10.00);

-- Seeding Machines
INSERT INTO Machines (Name, Type, LastMaintenance, NextMaintenance) VALUES 
('AutoMilker 3000', 'Milking', '2023-11-01', '2024-05-01'),
('John Deere Tractor', 'Heavy Machinery', '2023-10-15', '2024-04-15');

-- Seeding MilkProduction
-- Assuming CowID 1 (COW-001)
INSERT INTO MilkProduction (CowID, ProductionDate, Quantity, Quality) VALUES 
(1, '2023-12-22', 25.5, 'Premium'),
(1, '2023-12-23', 24.8, 'Standard');

-- Seeding CowFeeding
-- Assuming CowID 1 and FoodID 1 (Organic Hay)
INSERT INTO CowFeeding (CowID, FoodID, Date, Quantity) VALUES 
(1, 1, '2023-12-23', 15.0),
(2, 1, '2023-12-23', 12.0);
