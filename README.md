# Pandora Chronicles Database System - Phase 4

## Team Information
**Project:** DNA Phase 4 - Database Application  
**Theme:** Avatar/Na'vi Universe (Pandora Chronicles)  
**Database:** MySQL-based relational database system  
**Interface:** Python CLI Application

---

## Project Overview
The Pandora Chronicles Database System manages a complex ecosystem of characters, alliances, resources, and conflicts on the fictional planet Pandora. This application demonstrates advanced SQL operations through an interactive command-line interface.

---

## Features Implemented

### 📊 **Database Operations Summary**
- **Total Operations:** 15
- **READ Operations:** 10 (JOINs, aggregations, GROUP BY, HAVING)
- **WRITE Operations:** 5 (INSERT × 3, UPDATE × 2, DELETE × 1)
- **Tables:** 18 interconnected tables
- **Relationships:** Complex foreign keys with CASCADE and SET NULL actions

---

## Complete Feature List

### **1. CHARACTER OPERATIONS**

#### 1.1 Create Human Operative [INSERT]
- **Description:** Add a new human character to the database
- **SQL:** `INSERT INTO Human`
- **Features:** 
  - Soul assignment validation
  - Company assignment
  - Rank and weapon type specification
  - Prevents duplicate soul assignments

#### 1.2 Create Na'vi Character [INSERT]
- **Description:** Add a new Na'vi character to the database
- **SQL:** `INSERT INTO Navi`
- **Features:**
  - Soul assignment validation
  - Clan membership
  - Age tracking
  - Prevents duplicate soul assignments

#### 1.3 Form Avatar Link [INSERT]
- **Description:** Create an avatar link between a human and Na'vi body
- **SQL:** `INSERT INTO Avatar`
- **Features:**
  - Links human consciousness to Na'vi body
  - Tracks link status (Active/Inactive)
  - Records total linked hours
  - Validates both entities exist

#### 1.4 View Humans by Company [READ - 3-table JOIN]
- **Description:** Display all human operatives in a specific company
- **SQL:** `JOIN Human-Company-Soul`
- **Shows:** Name, rank, weapon, company details, soul state
- **Sorting:** By rank and last name

#### 1.5 View Na'vi by Clan [READ - 3-table JOIN]
- **Description:** Display all Na'vi members of a specific clan
- **SQL:** `JOIN Navi-Clan-Alliance`
- **Shows:** Name, age, clan, alliance affiliation, soul state
- **Sorting:** By age (descending)

#### 1.6 View Active Avatar Links [READ - 4-table JOIN]
- **Description:** Display all active human-Na'vi avatar connections
- **SQL:** `JOIN Avatar-Human-Navi-Clan-Company`
- **Shows:** Both human and Na'vi details, linked hours, clan, company
- **Sorting:** By total linked hours (descending)

#### 1.7 View Na'vi Bonded Animals [READ - LEFT JOIN]
- **Description:** Display Na'vi with their bonded animals (or without)
- **SQL:** `LEFT JOIN Navi-Bonded_Animal-Clan-Alliance`
- **Shows:** Na'vi name, bonded animal type, clan, alliance
- **Special:** Shows Na'vi even if they have no bonded animal

---

### **2. ALLIANCE & POLITICS**

#### 2.1 View Alliance Resource Control [READ - GROUP BY + Aggregations]
- **Description:** Analyze resource control across all alliances
- **SQL:** `GROUP BY with SUM, COUNT, AVG`
- **Shows:** Sites controlled, total resources, average resources per site
- **Sorting:** By total resources (descending)
- **Aggregates:** COUNT(sites), SUM(resources), AVG(resources)

#### 2.2 View Company-Clan Partnerships [READ - 3-table JOIN]
- **Description:** Display all active company-clan partnership agreements
- **SQL:** `JOIN Partnership-Company-Clan-Alliance`
- **Shows:** Company name, ethics rating, clan name, alliance objective
- **Sorting:** By alliance name, then company name

#### 2.3 Most War-Active Clans [READ - GROUP BY + HAVING]
- **Description:** Identify clans most frequently involved in wars
- **SQL:** `GROUP BY with HAVING clause`
- **Features:**
  - User-specified minimum war threshold
  - Average strength calculation
  - Filters clans by war participation
- **Shows:** Clan name, wars participated, average strength
- **Sorting:** By wars participated (descending)

---

### **3. WAR OPERATIONS**

#### 3.1 View Alliance War History [READ - 5-table JOIN + GROUP BY]
- **Description:** Comprehensive war history for a specific alliance
- **SQL:** `JOIN War-Alliance(×2)-Fights_In`
- **Shows:** 
  - War ID, casualties, outcome
  - Attacking and defending alliances
  - Number of clans involved
- **Sorting:** By casualties (descending)
- **Complex:** Handles alliance appearing as attacker OR defender

---

### **4. AETHERIUM MANAGEMENT**

#### 4.1 View Sites by Ecosystem [READ - 3-table JOIN + GROUP_CONCAT]
- **Description:** View all aetherium sites in a specific ecosystem
- **SQL:** `JOIN Ecosystem-Aetherium_Site-Alliance-Ecosystem_Flora`
- **Shows:** 
  - Ecosystem details (biome, dominant species)
  - Site resources and status
  - Controlling alliance
  - Comma-separated list of flora species
- **Sorting:** By resource quantity (descending)

#### 4.2 Update Site Status/Owner [UPDATE]
- **Description:** Change site status and/or owning alliance
- **SQL:** `UPDATE Aetherium_Site`
- **Features:**
  - Status validation (Unclaimed/Claimed/Depleted)
  - Alliance ownership transfer
  - Displays before/after states
  - Confirmation prompt
- **Demo Note:** Perfect for before/after demonstration in video

#### 4.3 Update Company Ethics Rating [UPDATE]
- **Description:** Modify a company's ethics rating
- **SQL:** `UPDATE Company`
- **Features:**
  - Rating validation (0.00 - 10.00)
  - Shows current rating before update
  - Confirmation prompt
- **Demo Note:** Good for demonstrating UPDATE with CHECK constraint

---

### **5. INTELLIGENCE & ANALYTICS**

#### 5.1 Ecosystem Threat Analysis [READ - 4-table JOIN + Aggregations]
- **Description:** Analyze threat levels across ecosystems
- **SQL:** `JOIN Ecosystem-Aetherium_Site-Report_Site-Report_Observation`
- **Aggregates:**
  - `COUNT(reports)` - Number of threat reports
  - `AVG(danger_level)` - Average danger level
  - `SUM(resource_loss)` - Total estimated resource loss
- **Shows:** Ecosystems sorted by danger level
- **Filter:** Only ecosystems with at least one report

---

### **6. ADMIN OPERATIONS**

#### 6.1 Delete Alliance [DELETE with CASCADE]
- **Description:** Permanently delete an alliance
- **SQL:** `DELETE FROM Alliance`
- **Cascade Effects:**
  - Clans lose alliance (set to NULL)
  - Sites become unclaimed (alliance set to NULL)
  - Partnerships dissolved (alliance set to NULL)
  - War records updated (alliance set to NULL)
- **Safety:** 
  - Shows affected clans and sites count
  - Requires explicit confirmation
  - Warning messages
- **Demo Note:** Excellent for showing CASCADE and SET NULL behavior

---

## Technical Details

### **SQL Techniques Demonstrated**
- ✅ **INNER JOIN** - Multiple 3, 4, and 5-table joins
- ✅ **LEFT JOIN** - Handling optional relationships
- ✅ **GROUP BY** - With multiple aggregations
- ✅ **HAVING** - Filtering aggregated results
- ✅ **Aggregate Functions** - COUNT, SUM, AVG, GROUP_CONCAT
- ✅ **Subqueries** - In WHERE clauses for availability checks
- ✅ **ORDER BY** - Complex sorting
- ✅ **CHECK Constraints** - Data validation
- ✅ **Foreign Keys** - CASCADE and SET NULL
- ✅ **Parameterized Queries** - SQL injection protection
- ✅ **Transactions** - COMMIT and ROLLBACK

### **Data Integrity Features**
- NOT NULL constraints on critical fields
- UNIQUE constraints on souls
- CHECK constraints on status fields and ratings
- Referential integrity via foreign keys
- Parameterized queries prevent SQL injection

---

## Setup Instructions

### **Prerequisites**
```bash
# Install MySQL
# Install Python 3.x
# Install PyMySQL
pip install pymysql
```

### **Database Setup**
```bash
# 1. Connect to MySQL
mysql -u root -p

# 2. Run schema creation
mysql -u root -p < src/schema.sql

# 3. Populate database
mysql -u root -p < src/populate.sql
```

### **Run Application**
```bash
cd src
python main_app.py
```

---

## Demo Guide (For Video Submission)

### **Recommended Demo Order (5 minutes)**

**1. Character Operations (90 seconds)**
- Show "View Humans by Company" [READ - 3-table JOIN]
- Demo "Create Human Operative" [INSERT]
  - Before: `SELECT * FROM Human ORDER BY Human_ID DESC LIMIT 5;`
  - After: Re-run same query to show new human

**2. Alliances & Resources (60 seconds)**
- Show "View Alliance Resource Control" [GROUP BY]
- Demonstrates aggregation and GROUP BY

**3. Updates & Cascades (90 seconds)**
- Demo "Update Site Status" [UPDATE]
  - Before: `SELECT * FROM Aetherium_Site WHERE Site_ID = X;`
  - Update in app
  - After: Re-run same query
- Demo "Delete Alliance" [DELETE]
  - Before: `SELECT * FROM Clan WHERE Alliance_ID = X;`
  - Delete in app
  - After: Show alliance_ID is now NULL

**4. Advanced Queries (60 seconds)**
- Show "War History" [5-table JOIN]
- Show "Ecosystem Threat Analysis" [4-table JOIN + aggregates]

**5. Avatar Links (30 seconds)**
- Show "View Active Avatar Links" [4-table JOIN]
- Demonstrates the soul transfer concept

---

## Files Included

```
DNA-Phase4/
├── README.md                    (this file)
├── phase3.pdf                   (previous submission)
├── src/
│   ├── schema.sql              (database structure)
│   ├── populate.sql            (sample data)
│   └── main_app.py             (Python application)
└── <team_number>.mp4           (video demonstration)
```

---

## Database Schema Statistics

- **Total Tables:** 18
- **Strong Entities:** 6 (Soul, Alliance, Clan, Ecosystem, Company, Report_Meta)
- **Weak Entities:** 1 (Bonded_Animal)
- **Relationship Tables:** 11
- **Total Foreign Keys:** 27
- **CHECK Constraints:** 5
- **AUTO_INCREMENT Primary Keys:** 10

---

## Known Limitations & Design Decisions

1. **Soul Sharing:** Souls can be linked to both Human and Na'vi (representing Avatar transfer)
2. **Bonded Animals:** Each Na'vi limited to one bonded animal (1:1 relationship)
3. **War Constraint:** Same alliance cannot attack and defend in same war (CHECK constraint)
4. **Alliance Deletion:** Uses SET NULL instead of CASCADE for safety
5. **Ethics Rating:** Constrained to 0.00-10.00 range

---

## Contact & Support

For questions about this project, please refer to phase3.pdf for full design documentation.

---

**End of README**
