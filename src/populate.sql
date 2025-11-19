USE pandora_chronicles;

-- ======================================
-- 1. POPULATE SOUL
-- ======================================
INSERT INTO Soul (Soul_ID, State)
VALUES
  (1, 'Active'),
  (2, 'Active'),
  (3, 'Inactive'),
  (4, 'Active'),
  (5, 'Active'),
  (6, 'Inactive');

-- ======================================
-- 2. POPULATE COMPANY
-- ======================================
INSERT INTO Company (Company_ID, Name, Ethics_Rating, Latitude, Longitude)
VALUES
  (1, 'RDA Recon', 4, -12.55, 44.21),
  (2, 'Helios Corp', 8, -16.77, 48.99),
  (3, 'Xenotech Extraction', 6, -10.21, 41.12);

-- ======================================
-- 3. POPULATE CLAN
-- ======================================
INSERT INTO Clan (Clan_ID, Clan_Name)
VALUES
  (1, 'Omaticaya'),
  (2, 'Metkayina'),
  (3, 'Tawkami');

-- ======================================
-- 4. POPULATE ECOSYSTEM
-- ======================================
INSERT INTO Ecosystem (Eco_ID, Name, Biome_Type, Dominant_Species)
VALUES
  (1, 'Bioluminescent Grove', 'Forest', 'Direhorse'),
  (2, 'Coral Reefs of Eywa', 'Ocean', 'Tsurak'),
  (3, 'Ancient Tree Plains', 'Grassland', 'Prolemuris');

-- ======================================
-- 5. POPULATE ECOSYSTEM FLORA
-- ======================================
INSERT INTO Ecosystem_Flora (Flora_Name, Eco_ID)
VALUES
  ('Glowvine', 1),
  ('Healing Moss', 1),
  ('Reef Moss', 2),
  ('Water Fern', 2),
  ('Tallgrain', 3);

-- ======================================
-- 6. POPULATE AETHERIUM_SITE
-- ======================================
INSERT INTO Aetherium_Site (Site_ID, Resource_Quantity, Status, Alliance_ID, Eco_ID)
VALUES
  (1, 1500, 'Unclaimed', NULL, 1),
  (2, 900, 'Claimed', NULL, 1),
  (3, 1200, 'Unclaimed', NULL, 2),
  (4, 450, 'Claimed', NULL, 3);

-- ======================================
-- 7. POPULATE HUMAN
-- ======================================
INSERT INTO Human (Human_ID, F_Name, L_Name, Rank, Weapon_Type, Soul_ID, Company_ID)
VALUES
  (1, 'Miles', 'Quaritch', 'Colonel', 'Gun', 1, 1),
  (2, 'Elena', 'Rojas', 'Scientist', 'Airship', 2, 2),
  (3, 'Tom', 'Sullivan', 'Pilot', 'Helicopter', 3, 3);

-- ======================================
-- 8. POPULATE NA'VI
-- ======================================
INSERT INTO "Na'vi" (Navi_ID, Name, Age, Soul_ID, Clan_ID)
VALUES
  (1, 'Neytiri', 25, 4, 1),
  (2, 'Ronal', 30, 5, 2),
  (3, 'Fhara', 22, 6, 3);

-- ======================================
-- 9. POPULATE BONDED ANIMAL
-- ======================================
INSERT INTO Bonded_Animal (Navi_ID, Name)
VALUES
  (1, 'Ikran'),
  (2, 'Tsurak'),
  (3, 'Sturmbeest');

-- ======================================
-- 10. POPULATE AVATAR
-- ======================================
INSERT INTO Avatar (Human_ID, Navi_ID, Link_Status, Total_Linked_Hours)
VALUES
  (1, 1, 'Active', 120),
  (2, 2, 'Active', 300),
  (3, 3, 'Inactive', 20);

-- ======================================
-- 11. POPULATE ALLIANCE
-- ======================================
INSERT INTO Alliance (Alliance_ID, Name, Objective)
VALUES
  (1, 'Skywalkers Pact', 'Defend Sacred Aetherium'),
  (2, 'Reefguard Accord', 'Protect Oceanic Territories'),
  (3, 'Greenheart Coalition', 'Preserve Tree Plains');

-- ======================================
-- 12. POPULATE PARTNERSHIP  (Company–Clan–Alliance)
-- ======================================
INSERT INTO Partnership (Company_ID, Clan_ID, Alliance_ID)
VALUES
  (2, 1, 1),  -- Helios + Omaticaya = Skywalkers Pact
  (3, 2, 2),  -- Xenotech + Metkayina = Reefguard Accord
  (1, 3, 3);  -- RDA + Tawkami = Greenheart Coalition

-- ======================================
-- 13. POPULATE STAFFS (Company–Site)
-- ======================================
INSERT INTO Staffs (Company_ID, Site_ID)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 4);

-- ======================================
-- 14. POPULATE WAR
-- ======================================
INSERT INTO War (War_ID, Casualties, Outcome, Attack_Alliance_ID, Defense_Alliance_ID)
VALUES
  (1, 120, 'Alliance Victory', 1, 3),
  (2, 80, 'Stalemate', 2, 1),
  (3, 200, 'Defeat', 3, 2);

-- ======================================
-- 15. POPULATE FIGHTS_IN
-- ======================================
INSERT INTO Fights_In (Clan_ID, War_ID, Strength)
VALUES
  (1, 1, 95),
  (3, 1, 80),
  (2, 2, 90),
  (1, 2, 88),
  (3, 3, 70);

-- ======================================
-- 16. REPORT META
-- ======================================
INSERT INTO Report_Meta (Report_ID, Timestamp)
VALUES
  (1, '2179-05-14 10:00:00'),
  (2, '2179-05-14 14:00:00'),
  (3, '2179-05-15 09:00:00');

-- ======================================
-- 17. REPORT OBSERVATION
-- ======================================
INSERT INTO Report_Observation (Report_ID, Threat_Description, Resource_Estimate_Change, Danger_Level_Observed, Alliance_ID)
VALUES
  (1, 'Increased predator activity', -100, 6, 1),
  (2, 'Storm damage reduced access', -200, 5, 2),
  (3, 'Human mining detected', -300, 8, 3);

-- ======================================
-- 18. REPORT SITE
-- ======================================
INSERT INTO Report_Site (Site_ID, Report_ID)
VALUES
  (1, 1),
  (2, 2),
  (3, 3);
