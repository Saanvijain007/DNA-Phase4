USE pandora_chronicles_db;

-- =========================
-- 1) SOUL
-- =========================
INSERT INTO Soul (Soul_ID, State) VALUES
 (1, 'Alive'),
 (2, 'Alive'),
 (3, 'Deceased'),
 (4, 'Linked_to_Eywa'),
 (5, 'Alive'),
 (6, 'Deceased'),
 (7, 'Alive'),
 (8, 'Alive'),
 (9, 'Deceased'),
 (10, 'Alive'),
 (11, 'Alive'),
 (12, 'Deceased'),
 (13, 'Alive'),
 (14, 'Alive'),
 (15, 'Deceased'),
 (16, 'Alive'),
 (17, 'Alive'),
 (18, 'Alive'),
 (19, 'Deceased'),
 (20, 'Alive');

-- =========================
-- 2) ALLIANCE
-- =========================
INSERT INTO Alliance (Alliance_ID, Name, Objective) VALUES
 (1, 'Skywalkers Pact', 'Defend sacred Aetherium sites and aerial territories'),
 (2, 'Reefguard Accord', 'Protect oceanic Aetherium fields and reef life'),
 (3, 'Greenheart Coalition', 'Preserve forest ecosystems and spiritual sites'),
 (4, 'Stormrider Covenant', 'Secure high-altitude Aetherium and weather nodes'),
 (5, 'Deepstone Union', 'Mine subterranean aetherium with controlled methods'),
 (6, 'Skyrender Division', 'Neutralize rogue aerial threats on Pandora'),
 (7, 'Tidefall Pact', 'Protect underwater relic sites and shipping lanes');

-- =========================
-- 3) CLAN
-- =========================
INSERT INTO Clan (Clan_ID, Clan_Name, Alliance_ID) VALUES
 (1, 'Omaticaya', 1),
 (2, 'Metkayina', 2),
 (3, 'Tawkami', 3),
 (4, 'Tipani', 4),
 (5, 'Anurai', 5),
 (6, 'Hulanta', 6),
 (7, 'Li_ona', NULL),        -- currently neutral
 (8, 'Kelutral Rangers', 3);

-- =========================
-- 4) ECOSYSTEM
-- =========================
INSERT INTO Ecosystem (Eco_ID, Name, Biome_Type, Dominant_Species) VALUES
 (1, 'Bioluminescent Grove', 'Forest', 'Direhorse'),
 (2, 'Coral Reefs of Eywa', 'Ocean', 'Tsurak'),
 (3, 'Ancient Tree Plains', 'Grassland', 'Prolemuris'),
 (4, 'Aetherium Peaks', 'Mountain', 'Sky Serpents'),
 (5, 'Crystal Caves', 'Cave', 'Luminescent Bats'),
 (6, 'Stormrider Plains', 'Grassland', 'Thunderhoof Elk'),
 (7, 'Tidefall Reefs', 'Coral Reef', 'Wavefin Sharks');

-- =========================
-- 5) COMPANY
-- =========================
INSERT INTO Company (Company_ID, Name, Ethics_Rating, Latitude, Longitude) VALUES
 (1, 'RDA Recon', 4.20, -12.550000, 44.210000),
 (2, 'Helios Corp', 8.10, -16.770000, 48.990000),
 (3, 'Xenotech Extraction', 6.00, -10.210000, 41.120000),
 (4, 'Pandora BioGen', 9.10, -11.540000, 39.210000),
 (5, 'Frontier Terraform Ltd', 5.50, -14.440000, 46.550000),
 (6, 'Nova Mining Solutions', 3.20, -18.220000, 49.770000),
 (7, 'Stellar Axis Corp', 7.60, -9.770000, 43.880000);

-- =========================
-- 6) HUMAN
-- (Human_ID, F_Name, L_Name, Rank, Weapon_Type, Soul_ID, Company_ID)
-- =========================
INSERT INTO Human (Human_ID, F_Name, L_Name, `Rank`, Weapon_Type, Soul_ID, Company_ID) VALUES
 (1, 'Miles', 'Quaritch', 'Colonel', 'Gun', 1, 1),
 (2, 'Elena', 'Rojas', 'Scientist', 'Airship', 2, 2),
 (3, 'Tom', 'Sullivan', 'Pilot', 'Helicopter', 3, 3),
 (4, 'Aria', 'Stone', 'Engineer', 'Drone', 7, 4),
 (5, 'Darius', 'Cole', 'Lieutenant', 'Assault Rifle', 8, 5),
 (6, 'Nia', 'Hartley', 'Medic', 'Pulse Staff', 9, 4),
 (7, 'Viktor', 'Reiss', 'Captain', 'Mech Suit', 10, 6),
 (8, 'Juno', 'Park', 'Strategist', 'Shock Baton', 11, 7),
 (9, 'Kade', 'Morrison', 'Sniper', 'Longbow Railgun', 12, 5),
 (10, 'Selene', 'Cross', 'Pilot', 'Aerial Drone', 13, 4),
 (11, 'Rey', 'Solano', 'Recon', 'Thermal Blade', 14, 6),
 (12, 'Mira', 'Donovan', 'Technician', 'EMP Launcher', 15, 7),
 (13, 'Harlan', 'Keene', 'Scout', 'Grappler', 16, 2),
 (14, 'Zara', 'Ivers', 'Biologist', 'Sonic Net', 17, 4),
 (15, 'Omar', 'Khan', 'Field Commander', 'Rail Pistol', 18, 1),
 (16, 'Priya', 'Desai', 'Analyst', 'Surveillance Drone', 19, 5),
 (17, 'Luca', 'Ferre', 'Engineer', 'Repair Kit', 20, 3);

-- =========================
-- 7) NAVI
-- (Navi_ID, Name, Age, Soul_ID, Clan_ID)
-- =========================
INSERT INTO Navi (Navi_ID, Name, Age, Soul_ID, Clan_ID) VALUES
 (1, 'Neytiri', 25, 4, 1),
 (2, 'Ronal', 30, 5, 2),
 (3, 'Fhara', 22, 6, 3),
 (4, 'Ziyara', 19, 7, 4),
 (5, 'Talon', 28, 8, 5),
 (6, 'Sahela', 32, 9, 6),
 (7, 'Erotan', 41, 10, 7),
 (8, 'Limari', 23, 11, 8),
 (9, 'Tsyal', 20, 12, 1),
 (10, 'Raha', 37, 13, 2),
 (11, 'Wetu', 26, 14, 3),
 (12, 'Namira', 30, 15, 5),
 (13, 'Koru', 45, 16, 1),
 (14, 'Sela', 29, 17, 2),
 (15, 'Maru', 21, 18, 4);

-- =========================
-- 8) BONDED_ANIMAL
-- (Navi_ID PRIMARY KEY, Name)
-- =========================
INSERT INTO Bonded_Animal (Navi_ID, Name) VALUES
 (1, 'Ikran'),
 (2, 'Tsurak'),
 (3, 'Sturmbeest'),
 (4, 'Pa_li'),
 (5, 'Great_Leonopteryx'),
 (6, 'Palulukan'),
 (7, 'Tulkun'),
 (8, 'Fan_Lizard'),
 (9, 'Direhorse'),
 (10, 'Kelku'),
 (11, 'Woven_Beetle'),
 (12, 'Skyherd');

-- =========================
-- 9) AVATAR
-- (Human_ID, Navi_ID, Link_Status, Total_Linked_Hours)
-- =========================
INSERT INTO Avatar (Human_ID, Navi_ID, Link_Status, Total_Linked_Hours) VALUES
 (1, 1, 'Active', 150),
 (2, 2, 'Active', 300),
 (3, 3, 'Inactive', 20),
 (4, 4, 'Active', 95),
 (5, 5, 'Active', 120),
 (6, 6, 'Inactive', 40),
 (7, 7, 'Active', 188),
 (8, 8, 'Inactive', 15),
 (9, 9, 'Active', 60),
 (10, 10, 'Active', 240),
 (11, 11, 'Inactive', 10),
 (12, 12, 'Active', 77),
 (13, 13, 'Active', 210),
 (14, 14, 'Active', 55),
 (15, 15, 'Inactive', 5);

-- =========================
-- 10) PARTNERSHIP
-- (Company_ID, Clan_ID, Alliance_ID)
-- =========================
INSERT INTO Partnership (Company_ID, Clan_ID, Alliance_ID) VALUES
 (2, 1, 1),
 (3, 2, 2),
 (1, 3, 3),
 (4, 4, 4),
 (5, 5, 5),
 (6, 6, 6),
 (7, 8, 3),   -- Stellar Axis with Kelutral Rangers under Greenheart
 (4, 1, 1);   -- Pandora BioGen also partners with Omaticaya (multi-company alliances)

-- =========================
-- 11) WAR
-- (War_ID, Casualties, Outcome, Attack_Alliance_ID, Defense_Alliance_ID)
-- =========================
INSERT INTO War (War_ID, Casualties, Outcome, Attack_Alliance_ID, Defense_Alliance_ID) VALUES
 (1, 250, 'Alliance Victory', 1, 5),
 (2, 400, 'Defeat', 6, 4),
 (3, 150, 'Stalemate', 2, 7),
 (4, 160, 'Victory', 4, 2),
 (5, 95, 'Alliance Loss', 5, 1),
 (6, 300, 'Heavy Loss', 3, 6),
 (7, 40, 'Skirmish', 2, 3);

-- =========================
-- 12) FIGHTS_IN
-- (Clan_ID, War_ID, Strength)
-- =========================
INSERT INTO Fights_In (Clan_ID, War_ID, Strength) VALUES
 (1, 1, '95'),
 (3, 1, '80'),
 (6, 2, '70'),
 (4, 2, '88'),
 (5, 3, '90'),
 (8, 3, '60'),
 (4, 4, '78'),
 (5, 4, '83'),
 (6, 5, '69'),
 (7, 6, '92'),
 (8, 6, '57'),
 (2, 7, '74'),
 (1, 7, '66');

-- =========================
-- 13) AETHERIUM_SITE
-- (Site_ID, Resource_Quantity, Status, Alliance_ID, Eco_ID)
-- =========================
INSERT INTO Aetherium_Site (Site_ID, Resource_Quantity, Status, Alliance_ID, Eco_ID) VALUES
 (1, 1500, 'Unclaimed', NULL, 1),
 (2, 900, 'Claimed', 1, 1),
 (3, 1200, 'Unclaimed', NULL, 2),
 (4, 450, 'Claimed', 2, 3),
 (5, 1800, 'Unclaimed', NULL, 4),
 (6, 600, 'Claimed', 4, 4),
 (7, 2200, 'Unclaimed', NULL, 5),
 (8, 1300, 'Claimed', 5, 5),
 (9, 750, 'Unclaimed', NULL, 6),
 (10, 1900, 'Claimed', 6, 7),
 (11, 420, 'Claimed', 2, 6),
 (12, 50, 'Depleted', NULL, 3);

-- =========================
-- 14) STAFFS
-- (Company_ID, Site_ID)
-- =========================
INSERT INTO Staffs (Company_ID, Site_ID) VALUES
 (1, 1),
 (1, 2),
 (2, 3),
 (3, 4),
 (4, 5),
 (4, 6),
 (5, 7),
 (6, 8),
 (7, 9),
 (5, 10),
 (6, 11);

-- =========================
-- 15) ECOSYSTEM_FLORA
-- (Flora_Name, Eco_ID)
-- =========================
INSERT INTO Ecosystem_Flora (Flora_Name, Eco_ID) VALUES
 ('Glowvine', 1),
 ('Healing Moss', 1),
 ('Reef Moss', 2),
 ('Water Fern', 2),
 ('Tallgrain', 3),
 ('Crystal Bloom', 4),
 ('Skyroot', 4),
 ('Cave Lantern', 5),
 ('Deep Moss', 5),
 ('Mistweed', 6),
 ('Bog Lily', 6),
 ('Azure Kelp', 7),
 ('Pearl Vine', 7);

-- =========================
-- 16) REPORT_META
-- (Report_ID, Timestamp)
-- =========================
INSERT INTO Report_Meta (Report_ID, Timestamp) VALUES
 (1, '2179-05-14 10:00:00'),
 (2, '2179-05-14 14:00:00'),
 (3, '2179-05-15 09:00:00'),
 (4, '2179-05-15 18:30:00'),
 (5, '2179-05-16 11:20:00'),
 (6, '2179-05-17 09:45:00');

-- =========================
-- 17) REPORT_OBSERVATION
-- (Report_ID, Threat_Description, Resource_Estimate_Change, Danger_Level_Observed, Alliance_ID)
-- =========================
INSERT INTO Report_Observation (Report_ID, Threat_Description, Resource_Estimate_Change, Danger_Level_Observed, Alliance_ID) VALUES
 (1, 'Increased predator activity near site 1', -100, '6', 1),
 (2, 'Storm damage reduced access to site 3', -200, '5', 2),
 (3, 'Human mining detected near cave site', -300, '8', 3),
 (4, 'Floating island instability detected', -150, '7', 4),
 (5, 'Tidal disturbance near relic site', -90, '5', 7),
 (6, 'Cave-in risk increasing due to seismic activity', -60, '6', 5);

-- =========================
-- 18) REPORT_SITE (Site_ID, Report_ID)
-- =========================
INSERT INTO Report_Site (Site_ID, Report_ID) VALUES
 (1, 1),
 (3, 2),
 (4, 3),
 (5, 4),
 (7, 5),
 (9, 6);

-- =========================
-- END: All data populated
-- =========================
