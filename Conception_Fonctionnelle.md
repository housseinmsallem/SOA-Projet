# Conception Fonctionnelle - Gestion de Ferme Laitière

Ce document présente la conception fonctionnelle de l'application de gestion d'une ferme de production laitière, basée sur les modèles de données actuels et les spécifications fournies.

## 1. Acteurs

| Acteur | Rôle et Responsabilités |
| :--- | :--- |
| **Administrateur** | Gestion globale du système, configuration, gestion des utilisateurs et des droits, supervision des ressources humaines et matérielles. |
| **Employé / Ouvrier** | Exécution des tâches quotidiennes, saisie des données opérationnelles (alimentation, production, mouvements de stock), réception des notifications. |
| **Vétérinaire** | Suivi de la santé du troupeau, saisie des interventions médicales, consultation et saisie des analyses biologiques. |
| **Responsable de Production** | Analyse des performances de production, contrôle de la qualité (lait, alimentation), prise de décision stratégique. |
| **Système (Automatique)** | Surveillance des seuils (stocks, maintenance), génération d'alertes et notifications. |

## 2. Architecture Fonctionnelle

L'application est structurée en modules interconnectés couvrant l'ensemble des activités de la ferme.

```mermaid
graph TD
    subgraph System ["Gestion de Ferme Laitière"]
        
        M1["Module Ressources Générales"]
        M2["Module Ressources d'Exploitation"]
        M3["Module Gestion Troupeau"]
        M4["Module Alimentation & Production"]
        M5["Module Reporting & Tableaux de Bord"]

        %% Détails M1
        M1 --> M1_1["Gestion Étables"]
        M1 --> M1_2["Gestion Machines & Maintenance"]
        M1 --> M1_3["Gestion Personnel & RH"]

        %% Détails M2
        M2 --> M2_1["Gestion Stocks Aliments/Pièces"]
        M2 --> M2_2["Approvisionnement & Fournisseurs"]
        M2 --> M2_3["Alertes & Notifications"]

        %% Détails M3
        M3 --> M3_1["Identification & Traçabilité"]
        M3 --> M3_2["Cycle de Vie & Phases"]
        M3 --> M3_3["Suivi Santé & Soins"]

        %% Détails M4
        M4 --> M4_1["Planification Rations"]
        M4 --> M4_2["Suivi Production Laitière"]
        M4 --> M4_3["Analyses Qualité (Lait/Aliment)"]

        %% Détails M5
        M5 --> M5_1["KPI Production"]
        M5 --> M5_2["État des Stocks"]
        M5 --> M5_3["Suivi Santé Global"]
        M5 --> M5_4["Analyse des Coûts"]
    end
```

## 3. Diagramme des Cas d'Utilisation (Use Cases)

Ce diagramme illustre les interactions des différents acteurs avec les fonctionnalités principales du système.

```mermaid
graph LR
    subgraph Actors [Acteurs]
        direction TB
        Admin[Administrateur]
        Emp[Employé]
        Vet[Vétérinaire]
        ProdMgr[Resp. Production]
    end

    subgraph Ressources [Gestion des Ressources]
        direction TB
        UC1([Gérer le Personnel])
        UC2([Gérer les Machines])
        UC3([Planifier Maintenance])
        UC4([Gérer les Étables])
    end

    subgraph Operations [Opérations & Stock]
        direction TB
        UC5([Gérer les Stocks])
        UC6([Gérer Approvisionnement])
        UC7([Saisir Tâches Quotidiennes])
    end

    subgraph Troupeau [Gestion Troupeau]
        direction TB
        UC8([Identifier/Ajouter Vache])
        UC9([Mettre à jour Cycle de Vie])
        UC10([Enregistrer Alimentation])
        UC11([Consulter Dossier Vache])
    end

    subgraph SanteProd [Santé & Production]
        direction TB
        UC12([Saisir Interventions Santé])
        UC13([Enregistrer Production Lait])
        UC14([Saisir Analyses Bio/Lait])
        UC15([Analyser Performances])
    end

    %% Relations Administrateur
    Admin --> UC1
    Admin --> UC2
    Admin --> UC4
    Admin --> UC3
    
    %% Relations Employé
    Emp --> UC7
    Emp --> UC10
    Emp --> UC13
    Emp --> UC5

    %% Relations Vétérinaire
    Vet --> UC12
    Vet --> UC14
    Vet --> UC11

    %% Relations Resp. Production
    ProdMgr --> UC6
    ProdMgr --> UC15
    ProdMgr --> UC9
    ProdMgr --> UC14
```

## 4. Diagramme de Classes (Modèle de Données)

Ce diagramme reflète la structure actuelle de la base de données (basé sur `models.py`), montrant les entités et leurs relations.

```mermaid
classDiagram
    %% Core Users & Personnel
    class UserAuth {
        +String username
        +String role
    }
    class Employees {
        +int employee_id
        +String first_name
        +String last_name
        +String role
        +Decimal base_salary
        +Decimal hourly_rate
        +Date hire_date
    }
    class EmployeeTasks {
        +int task_id
        +String task_description
        +Decimal hours_worked
        +Date task_date
    }

    %% Resources & Infrastructure
    class Barns {
        +int barn_id
        +String name
        +int capacity
        +String location
    }
    class Machines {
        +int machine_id
        +String name
        +String type
        +Date last_maintenance
        +Date next_maintenance
    }

    %% Stock & Supply
    class Resources {
        +int resource_id
        +String name
        +String type
        +Decimal quantity
    }
    class Suppliers {
        +int supplier_id
        +String name
        +String contact_info
    }
    class PurchaseOrders {
        +int order_id
        +Date order_date
        +String status
    }
    class PurchaseOrderItems {
        +Decimal ordered_quantity
    }
    class GoodsReceiptNotes {
        +int grn_id
        +Date receipt_date
        +String status
    }
    
    %% Herd Management
    class Cows {
        +int cow_id
        +String tag_number
        +Date birth_date
        +String current_phase
    }
    class CowHealth {
        +int health_id
        +Date date
        +String type
        +String description
        +String vet_name
    }
    class AnalysisParameters {
        +int parameter_id
        +String name
        +String unit
        +Decimal min_value
        +Decimal max_value
    }
    class CowBiologicalAnalysis {
        +int analysis_id
        +Date date
        +Decimal value
        +String result
    }

    %% Feeding & Production
    class Food {
        +int food_id
        +String name
        +String type
        +Decimal quantity
        +Decimal reorder_level
    }
    class CowFeeding {
        +int feeding_id
        +Date date
        +Decimal quantity
    }
    class FoodAnalysis {
        +int analysis_id
        +Date analysis_date
        +Decimal value
    }
    class MilkProduction {
        +int production_id
        +Date production_date
        +Decimal quantity
        +String quality
    }
    class MilkAnalysis {
        +int analysis_id
        +Date analysis_date
        +Decimal value
    }

    %% Relationships
    Employees "1" -- "*" EmployeeTasks : performs
    Barns "1" -- "*" Cows : houses
    Cows "1" -- "*" CowHealth : has history
    Cows "1" -- "*" CowBiologicalAnalysis : has analysis
    Cows "1" -- "*" CowFeeding : fed with
    Cows "1" -- "*" MilkProduction : produces
    
    Food "1" -- "*" CowFeeding : is fed
    Food "1" -- "*" FoodAnalysis : analyzed
    
    MilkProduction "1" -- "*" MilkAnalysis : analyzed
    
    AnalysisParameters "1" -- "*" CowBiologicalAnalysis : defines
    AnalysisParameters "1" -- "*" FoodAnalysis : defines
    AnalysisParameters "1" -- "*" MilkAnalysis : defines

    Suppliers "1" -- "*" PurchaseOrders : supplies
    PurchaseOrders "1" -- "*" PurchaseOrderItems : contains
    Resources "1" -- "*" PurchaseOrderItems : ordered
    PurchaseOrders "1" -- "*" GoodsReceiptNotes : fulfills
    
    %% Note: UserAuth helps manage access but isn't strictly FK linked to Employees in current model explicitly, though conceptually related.
```

## 5. Scénarios d'Utilisation (Détails)

### Gestion du Stock d'Aliments
1.  **Acteur** : Employé.
2.  **Action** : Enregistre une sortie de stock (ex: 500kg de Maïs) pour l'alimentation.
3.  **Système** :
    *   Met à jour la quantité dans `Food`.
    *   Vérifie si `Quantity` < `ReorderLevel`.
    *   Si Oui : Crée une **Notification** (ou Alerte) pour le Responsable.

### Suivi de Cycle de Vie d'une Vache
1.  **Acteur** : Vétérinaire ou Responsable.
2.  **Action** : Déclare le vêlage d'une vache.
3.  **Système** :
    *   Met à jour `Cows.current_phase` de "Gestation" à "Lactation".
    *   Crée une nouvelle entrée `Cows` pour le veau (lien mère-enfant possible si modèle étendu).
    *   Active le suivi de `MilkProduction` pour la mère.

### Planification Maintenance
1.  **Acteur** : Administrateur.
2.  **Action** : Consulte la liste des `Machines`.
3.  **Système** : Affiche les machines dont `NextMaintenance` est proche.
4.  **Action** : Planifie une intervention.
5.  **Système** : Met à jour `NextMaintenance`.

### Production Laitière et Qualité
1.  **Acteur** : Employé (Traite) / Resp. Production (Analyse).
2.  **Action** : Enregistre la traite du jour (`MilkProduction`).
3.  **Action** : Enregistre les résultats d'analyse (`MilkAnalysis`) pour cet échantillon.
4.  **Système** : Associe les données. Si qualité insuffisante (ex: taux protéique bas), alerte le nutritionniste pour ajuster la ration (`CowFeeding`).
