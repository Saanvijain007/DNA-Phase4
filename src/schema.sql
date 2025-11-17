

DROP DATABASE IF EXISTS pandora_chronicles_db;
CREATE DATABASE pandora_chronicles_db;
USE pandora_chronicles_db;

CREATE TABLE Soul (
    Soul_ID INT PRIMARY KEY,
    State VARCHAR(50) NOT NULL
);

CREATE TABLE Clan (
    Clan_ID INT PRIMARY KEY,
    Clan_Name VARCHAR(100) NOT NULL
);


CREATE TABLE Alliance (
    Alliance_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Objective TEXT
);

CREATE TABLE Ecosystem (
    Eco_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Biome_Type VARCHAR(100),
    Dominant_Species VARCHAR(100)
);

-- =========================================================
-- 5. COMPANY
-- =========================================================
CREATE TABLE Company (
    Company_ID INT PRIMARY KEY,
    Name VARCHAR(150) NOT NULL,
    Ethics_Rating DECIMAL(3,2),
    Latitude DECIMAL(9,6),
    Longitude DECIMAL(9,6)
);

-- =========================================================
-- 6. HUMAN
-- =========================================================
CREATE TABLE Human (
    Human_ID INT PRIMARY KEY,
    F_Name VARCHAR(100),
    L_Name VARCHAR(100),
    Rank VARCHAR(50),
    Weapon_Type VARCHAR(100),
    Soul_ID INT UNIQUE,
    Company_ID INT,
    FOREIGN KEY (Soul_ID) REFERENCES Soul(Soul_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- =========================================================
-- 7. NA'VI
-- =========================================================
CREATE TABLE Navi (
    Navi_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Age INT,
    Soul_ID INT UNIQUE,
    Clan_ID INT,
    FOREIGN KEY (Soul_ID) REFERENCES Soul(Soul_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (Clan_ID) REFERENCES Clan(Clan_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- =========================================================
-- 8. BONDED ANIMAL
-- =========================================================
CREATE TABLE Bonded_Animal (
    Navi_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    FOREIGN KEY (Navi_ID) REFERENCES Navi(Navi_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- 9. AVATAR (Composite PK)
-- =========================================================
CREATE TABLE Avatar (
    Human_ID INT,
    Navi_ID INT,
    Link_Status VARCHAR(50),
    Total_Linked_Hours INT CHECK (Total_Linked_Hours >= 0),
    PRIMARY KEY (Human_ID, Navi_ID),
    FOREIGN KEY (Human_ID) REFERENCES Human(Human_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Navi_ID) REFERENCES Navi(Navi_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- 10. PARTNERSHIP (Composite PK)
-- =========================================================
CREATE TABLE Partnership (
    Company_ID INT,
    Clan_ID INT,
    Alliance_ID INT,
    PRIMARY KEY (Company_ID, Clan_ID, Alliance_ID),
    FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Clan_ID) REFERENCES Clan(Clan_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Alliance_ID) REFERENCES Alliance(Alliance_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- =========================================================
-- 11. WAR
-- =========================================================
CREATE TABLE War (
    War_ID INT PRIMARY KEY,
    Casualties INT,
    Outcome VARCHAR(100),
    Attack_Alliance_ID INT,
    Defense_Alliance_ID INT,
    FOREIGN KEY (Attack_Alliance_ID) REFERENCES Alliance(Alliance_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (Defense_Alliance_ID) REFERENCES Alliance(Alliance_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- =========================================================
-- 12. FIGHTS_IN (Composite PK)
-- =========================================================
CREATE TABLE Fights_In (
    Clan_ID INT,
    War_ID INT,
    Strength VARCHAR(50),
    PRIMARY KEY (Clan_ID, War_ID),
    FOREIGN KEY (Clan_ID) REFERENCES Clan(Clan_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (War_ID) REFERENCES War(War_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- 13. AETHERIUM SITE
-- =========================================================
CREATE TABLE Aetherium_Site (
    Site_ID INT PRIMARY KEY,
    Resource_Quantity INT,
    Status VARCHAR(50),
    Alliance_ID INT,
    Eco_ID INT,
    FOREIGN KEY (Alliance_ID) REFERENCES Alliance(Alliance_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
    FOREIGN KEY (Eco_ID) REFERENCES Ecosystem(Eco_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- =========================================================
-- 14. STAFFS (Composite PK)
-- =========================================================
CREATE TABLE Staffs (
    Company_ID INT,
    Site_ID INT,
    PRIMARY KEY (Company_ID, Site_ID),
    FOREIGN KEY (Company_ID) REFERENCES Company(Company_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Site_ID) REFERENCES Aetherium_Site(Site_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- 15. ECOSYSTEM FLORA (Composite PK)
-- =========================================================
CREATE TABLE Ecosystem_Flora (
    Flora_Name VARCHAR(100),
    Eco_ID INT,
    PRIMARY KEY (Flora_Name, Eco_ID),
    FOREIGN KEY (Eco_ID) REFERENCES Ecosystem(Eco_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =========================================================
-- 16. REPORT META
-- =========================================================
CREATE TABLE Report_Meta (
    Report_ID INT PRIMARY KEY,
    Timestamp DATETIME NOT NULL
);

-- =========================================================
-- 17. REPORT OBSERVATION
-- =========================================================
CREATE TABLE Report_Observation (
    Report_ID INT PRIMARY KEY,
    Threat_Description TEXT,
    Resource_Estimate_Change INT,
    Danger_Level_Observed VARCHAR(50),
    Alliance_ID INT,
    FOREIGN KEY (Report_ID) REFERENCES Report_Meta(Report_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Alliance_ID) REFERENCES Alliance(Alliance_ID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- =========================================================
-- 18. REPORT SITE (Composite PK)
-- =========================================================
CREATE TABLE Report_Site (
    Site_ID INT,
    Report_ID INT,
    PRIMARY KEY (Site_ID, Report_ID),
    FOREIGN KEY (Site_ID) REFERENCES Aetherium_Site(Site_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (Report_ID) REFERENCES Report_Meta(Report_ID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
