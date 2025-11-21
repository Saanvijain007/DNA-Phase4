import pymysql
import sys
from getpass import getpass
from datetime import datetime

# ============================================================
# DATABASE CONNECTION
# ============================================================
def get_connection():
    """Establishes connection to the Pandora Chronicles database."""
    print("\n=== DATABASE CONNECTION ===")
    print("Enter MySQL credentials:")
    user = input("Username: ").strip()
    password = getpass("Password: ")

    try:
        conn = pymysql.connect(
            host="localhost",
            user=user,
            password=password,
            database="pandora_chronicles_db",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=False
        )
        print("✓ Connection successful!\n")
        return conn
    except pymysql.Error as e:
        print(f"✗ Connection failed: {e}", file=sys.stderr)
        return None


# ============================================================
# UTILITY FUNCTIONS
# ============================================================
def print_header(title):
    """Prints a formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)


def print_results(results, title="Results"):
    """Prints query results in a formatted table."""
    if not results:
        print("  No data found.")
        return
    
    print(f"\n{title}:")
    print("-" * 60)
    for i, row in enumerate(results, 1):
        print(f"\n[{i}]")
        for key, value in row.items():
            print(f"  {key}: {value}")
    print("-" * 60)
    print(f"Total: {len(results)} record(s)")


def confirm_action(message="Proceed with this action?"):
    """Asks user for confirmation."""
    response = input(f"{message} (yes/no): ").strip().lower()
    return response in ['yes', 'y']


# ============================================================
# READ OPERATIONS (10 QUERIES)
# ============================================================

def view_humans_by_company(conn):
    """
    READ 1: View all humans in a specific company
    SQL: 3-table JOIN (Human-Company-Soul)
    """
    print_header("View Human Operatives by Company")
    
    try:
        # First, show available companies
        with conn.cursor() as cur:
            cur.execute("SELECT Company_ID, Name FROM Company ORDER BY Name")
            companies = cur.fetchall()
            
        if not companies:
            print("No companies found in database.")
            return
            
        print("\nAvailable Companies:")
        for comp in companies:
            print(f"  ID {comp['Company_ID']}: {comp['Name']}")
        
        company_id = input("\nEnter Company ID: ").strip()
        
        sql = """
            SELECT h.Human_ID, h.F_Name, h.L_Name, h.Rank, h.Weapon_Type,
                   c.Name as Company_Name, c.Ethics_Rating,
                   s.Soul_ID, s.State as Soul_State
            FROM Human h
            JOIN Company c ON h.Company_ID = c.Company_ID
            JOIN Soul s ON h.Soul_ID = s.Soul_ID
            WHERE c.Company_ID = %s
            ORDER BY h.Rank, h.L_Name
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (company_id,))
            results = cur.fetchall()
        
        print_results(results, f"Human Operatives in Company {company_id}")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


def view_navi_by_clan(conn):
    """
    READ 2: View Na'vi by clan with alliance information
    SQL: 3-table JOIN with LEFT JOIN (Navi-Clan-Alliance)
    """
    print_header("View Na'vi by Clan")
    
    try:
        # Show available clans
        with conn.cursor() as cur:
            cur.execute("SELECT Clan_ID, Clan_Name FROM Clan ORDER BY Clan_Name")
            clans = cur.fetchall()
        
        if not clans:
            print("No clans found.")
            return
        
        print("\nAvailable Clans:")
        for clan in clans:
            print(f"  ID {clan['Clan_ID']}: {clan['Clan_Name']}")
        
        clan_id = input("\nEnter Clan ID: ").strip()
        
        sql = """
            SELECT n.Navi_ID, n.Name, n.Age,
                   c.Clan_Name,
                   a.Name as Alliance_Name, a.Objective as Alliance_Objective,
                   s.State as Soul_State
            FROM Navi n
            JOIN Clan c ON n.Clan_ID = c.Clan_ID
            LEFT JOIN Alliance a ON c.Alliance_ID = a.Alliance_ID
            JOIN Soul s ON n.Soul_ID = s.Soul_ID
            WHERE c.Clan_ID = %s
            ORDER BY n.Age DESC
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (clan_id,))
            results = cur.fetchall()
        
        print_results(results, f"Na'vi in Clan {clan_id}")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


def view_avatar_links(conn):
    """
    READ 3: View active avatar links
    SQL: 4-table JOIN (Avatar-Human-Navi-Soul)
    """
    print_header("Active Avatar Links")
    
    try:
        sql = """
            SELECT av.Human_ID, av.Navi_ID, av.Link_Status, av.Total_Linked_Hours,
                   CONCAT(h.F_Name, ' ', h.L_Name) as Human_Name, h.Rank,
                   n.Name as Navi_Name, n.Age as Navi_Age,
                   c.Clan_Name,
                   co.Name as Company_Name
            FROM Avatar av
            JOIN Human h ON av.Human_ID = h.Human_ID
            JOIN Navi n ON av.Navi_ID = n.Navi_ID
            JOIN Clan c ON n.Clan_ID = c.Clan_ID
            LEFT JOIN Company co ON h.Company_ID = co.Company_ID
            WHERE av.Link_Status = 'Active'
            ORDER BY av.Total_Linked_Hours DESC
        """
        
        with conn.cursor() as cur:
            cur.execute(sql)
            results = cur.fetchall()
        
        print_results(results, "Active Avatar Links")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)


def view_navi_bonded_animals(conn):
    """
    READ 4: View Na'vi with their bonded animals
    SQL: LEFT JOIN to show Na'vi with and without bonded animals
    """
    print_header("Na'vi Bonded Animals")
    
    try:
        sql = """
            SELECT n.Navi_ID, n.Name as Navi_Name, n.Age,
                   ba.Name as Bonded_Animal,
                   c.Clan_Name,
                   a.Name as Alliance_Name
            FROM Navi n
            LEFT JOIN Bonded_Animal ba ON n.Navi_ID = ba.Navi_ID
            JOIN Clan c ON n.Clan_ID = c.Clan_ID
            LEFT JOIN Alliance a ON c.Alliance_ID = a.Alliance_ID
            ORDER BY c.Clan_Name, n.Name
        """
        
        with conn.cursor() as cur:
            cur.execute(sql)
            results = cur.fetchall()
        
        print_results(results, "Na'vi and Their Bonded Animals")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)


def view_alliance_resources(conn):
    """
    READ 5: View alliance resource control
    SQL: GROUP BY with aggregations (COUNT, SUM)
    """
    print_header("Alliance Resource Control Analysis")
    
    try:
        sql = """
            SELECT a.Alliance_ID, a.Name as Alliance_Name, a.Objective,
                   COUNT(ast.Site_ID) as Sites_Controlled,
                   COALESCE(SUM(ast.Resource_Quantity), 0) as Total_Resources,
                   COALESCE(AVG(ast.Resource_Quantity), 0) as Avg_Resources_Per_Site
            FROM Alliance a
            LEFT JOIN Aetherium_Site ast ON a.Alliance_ID = ast.Alliance_ID 
                AND ast.Status = 'Claimed'
            GROUP BY a.Alliance_ID
            ORDER BY Total_Resources DESC
        """
        
        with conn.cursor() as cur:
            cur.execute(sql)
            results = cur.fetchall()
        
        print_results(results, "Alliance Resource Statistics")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)


def view_company_clan_partnerships(conn):
    """
    READ 6: View company-clan partnerships
    SQL: 3-table JOIN (Partnership-Company-Clan-Alliance)
    """
    print_header("Company-Clan Partnerships")
    
    try:
        sql = """
            SELECT p.Company_ID, p.Clan_ID,
                   co.Name as Company_Name, co.Ethics_Rating,
                   c.Clan_Name,
                   a.Name as Alliance_Name, a.Objective
            FROM Partnership p
            JOIN Company co ON p.Company_ID = co.Company_ID
            JOIN Clan c ON p.Clan_ID = c.Clan_ID
            LEFT JOIN Alliance a ON p.Alliance_ID = a.Alliance_ID
            ORDER BY a.Name, co.Name
        """
        
        with conn.cursor() as cur:
            cur.execute(sql)
            results = cur.fetchall()
        
        print_results(results, "Active Partnerships")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)


def view_war_active_clans(conn):
    """
    READ 7: Most war-active clans
    SQL: GROUP BY with HAVING clause
    """
    print_header("Most War-Active Clans")
    
    try:
        min_wars = input("Minimum wars participated (default 1): ").strip()
        min_wars = int(min_wars) if min_wars else 1
        
        sql = """
            SELECT c.Clan_ID, c.Clan_Name,
                   a.Name as Alliance_Name,
                   COUNT(fi.War_ID) as Wars_Participated,
                   AVG(CAST(fi.Strength as UNSIGNED)) as Avg_Strength
            FROM Clan c
            JOIN Fights_In fi ON c.Clan_ID = fi.Clan_ID
            LEFT JOIN Alliance a ON c.Alliance_ID = a.Alliance_ID
            GROUP BY c.Clan_ID
            HAVING COUNT(fi.War_ID) >= %s
            ORDER BY Wars_Participated DESC, Avg_Strength DESC
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (min_wars,))
            results = cur.fetchall()
        
        print_results(results, f"Clans with {min_wars}+ Wars")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
    except ValueError:
        print("Invalid number entered.")


def view_war_history(conn):
    """
    READ 8: View war history for an alliance
    SQL: 5-table JOIN with aggregation
    """
    print_header("Alliance War History")
    
    try:
        # Show alliances
        with conn.cursor() as cur:
            cur.execute("SELECT Alliance_ID, Name FROM Alliance ORDER BY Name")
            alliances = cur.fetchall()
        
        print("\nAlliances:")
        for alliance in alliances:
            print(f"  ID {alliance['Alliance_ID']}: {alliance['Name']}")
        
        alliance_id = input("\nEnter Alliance ID: ").strip()
        
        sql = """
            SELECT w.War_ID, w.Casualties, w.Outcome,
                   a_attack.Name as Attacking_Alliance,
                   a_defend.Name as Defending_Alliance,
                   COUNT(DISTINCT fi.Clan_ID) as Clans_Involved
            FROM War w
            JOIN Alliance a_attack ON w.Attack_Alliance_ID = a_attack.Alliance_ID
            JOIN Alliance a_defend ON w.Defense_Alliance_ID = a_defend.Alliance_ID
            LEFT JOIN Fights_In fi ON w.War_ID = fi.War_ID
            WHERE w.Attack_Alliance_ID = %s OR w.Defense_Alliance_ID = %s
            GROUP BY w.War_ID
            ORDER BY w.Casualties DESC
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (alliance_id, alliance_id))
            results = cur.fetchall()
        
        print_results(results, f"Wars Involving Alliance {alliance_id}")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


def view_sites_by_ecosystem(conn):
    """
    READ 9: View aetherium sites by ecosystem with flora
    SQL: 3-table JOIN (Ecosystem-Site-Flora)
    """
    print_header("Aetherium Sites by Ecosystem")
    
    try:
        # Show ecosystems
        with conn.cursor() as cur:
            cur.execute("SELECT Eco_ID, Name, Biome_Type FROM Ecosystem ORDER BY Name")
            ecosystems = cur.fetchall()
        
        print("\nEcosystems:")
        for eco in ecosystems:
            print(f"  ID {eco['Eco_ID']}: {eco['Name']} ({eco['Biome_Type']})")
        
        eco_id = input("\nEnter Ecosystem ID: ").strip()
        
        sql = """
            SELECT e.Name as Ecosystem_Name, e.Biome_Type, e.Dominant_Species,
                   ast.Site_ID, ast.Resource_Quantity, ast.Status,
                   a.Name as Controlled_By_Alliance,
                   GROUP_CONCAT(DISTINCT ef.Flora_Name SEPARATOR ', ') as Flora_Species
            FROM Ecosystem e
            LEFT JOIN Aetherium_Site ast ON e.Eco_ID = ast.Eco_ID
            LEFT JOIN Alliance a ON ast.Alliance_ID = a.Alliance_ID
            LEFT JOIN Ecosystem_Flora ef ON e.Eco_ID = ef.Eco_ID
            WHERE e.Eco_ID = %s
            GROUP BY ast.Site_ID
            ORDER BY ast.Resource_Quantity DESC
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (eco_id,))
            results = cur.fetchall()
        
        print_results(results, f"Sites in Ecosystem {eco_id}")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


def ecosystem_threat_analysis(conn):
    """
    READ 10: Ecosystem threat analysis
    SQL: 4-table JOIN with aggregations (AVG, COUNT)
    """
    print_header("Ecosystem Threat Assessment")
    
    try:
        sql = """
            SELECT e.Eco_ID, e.Name as Ecosystem_Name, e.Biome_Type,
                   COUNT(DISTINCT ro.Report_ID) as Threat_Reports,
                   AVG(CAST(ro.Danger_Level_Observed as UNSIGNED)) as Avg_Danger_Level,
                   SUM(ro.Resource_Estimate_Change) as Total_Resource_Loss
            FROM Ecosystem e
            JOIN Aetherium_Site ast ON e.Eco_ID = ast.Eco_ID
            JOIN Report_Site rs ON ast.Site_ID = rs.Site_ID
            JOIN Report_Observation ro ON rs.Report_ID = ro.Report_ID
            GROUP BY e.Eco_ID
            HAVING COUNT(ro.Report_ID) > 0
            ORDER BY Avg_Danger_Level DESC, Threat_Reports DESC
        """
        
        with conn.cursor() as cur:
            cur.execute(sql)
            results = cur.fetchall()
        
        print_results(results, "Ecosystem Threat Analysis")
        
        if results:
            print("\n⚠ Danger Level Scale: 1 (Low) - 10 (Critical)")
        
    except pymysql.Error as e:
        print(f"Database error: {e}", file=sys.stderr)


# ============================================================
# WRITE OPERATIONS (5 UPDATES)
# ============================================================

def create_human(conn):
    """
    WRITE 1: Create a new human character
    SQL: INSERT into Human
    """
    print_header("Create New Human Operative")
    
    try:
        # Show companies
        with conn.cursor() as cur:
            cur.execute("SELECT Company_ID, Name FROM Company ORDER BY Name")
            companies = cur.fetchall()
            
            # Show available souls (not assigned to humans)
            cur.execute("""
                SELECT s.Soul_ID, s.State 
                FROM Soul s 
                WHERE s.Soul_ID NOT IN (SELECT Soul_ID FROM Human WHERE Soul_ID IS NOT NULL)
                ORDER BY s.Soul_ID
            """)
            available_souls = cur.fetchall()
        
        print("\nAvailable Companies:")
        for comp in companies:
            print(f"  {comp['Company_ID']}: {comp['Name']}")
        
        print("\nAvailable Souls:")
        for soul in available_souls[:10]:  # Show first 10
            print(f"  Soul {soul['Soul_ID']}: {soul['State']}")
        
        print("\n--- Enter Human Details ---")
        f_name = input("First Name: ").strip()
        l_name = input("Last Name: ").strip()
        rank = input("Rank (e.g., Colonel, Pilot, Engineer): ").strip()
        weapon = input("Weapon Type: ").strip()
        soul_id = input("Soul ID: ").strip()
        company_id = input("Company ID: ").strip()
        
        if not all([f_name, l_name, soul_id]):
            print("First name, last name, and soul ID are required.")
            return
        
        sql = """
            INSERT INTO Human (F_Name, L_Name, `Rank`, Weapon_Type, Soul_ID, Company_ID)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (f_name, l_name, rank, weapon, soul_id, company_id or None))
        
        conn.commit()
        print(f"\n✓ Human operative '{f_name} {l_name}' created successfully!")
        
    except pymysql.IntegrityError as e:
        conn.rollback()
        print(f"✗ Data integrity error: {e}", file=sys.stderr)
        print("  (Soul ID may already be assigned or Company ID invalid)")
    except pymysql.Error as e:
        conn.rollback()
        print(f"✗ Database error: {e}", file=sys.stderr)
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}", file=sys.stderr)


def create_navi(conn):
    """
    WRITE 2: Create a new Na'vi character
    SQL: INSERT into Navi
    """
    print_header("Create New Na'vi Character")
    
    try:
        # Show clans
        with conn.cursor() as cur:
            cur.execute("SELECT Clan_ID, Clan_Name FROM Clan ORDER BY Clan_Name")
            clans = cur.fetchall()
            
            # Show available souls
            cur.execute("""
                SELECT s.Soul_ID, s.State 
                FROM Soul s 
                WHERE s.Soul_ID NOT IN (SELECT Soul_ID FROM Navi WHERE Soul_ID IS NOT NULL)
                ORDER BY s.Soul_ID
            """)
            available_souls = cur.fetchall()
        
        print("\nAvailable Clans:")
        for clan in clans:
            print(f"  {clan['Clan_ID']}: {clan['Clan_Name']}")
        
        print("\nAvailable Souls:")
        for soul in available_souls[:10]:
            print(f"  Soul {soul['Soul_ID']}: {soul['State']}")
        
        print("\n--- Enter Na'vi Details ---")
        name = input("Name: ").strip()
        age = input("Age: ").strip()
        soul_id = input("Soul ID: ").strip()
        clan_id = input("Clan ID: ").strip()
        
        if not all([name, soul_id]):
            print("Name and Soul ID are required.")
            return
        
        sql = """
            INSERT INTO Navi (Name, Age, Soul_ID, Clan_ID)
            VALUES (%s, %s, %s, %s)
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (name, age or None, soul_id, clan_id or None))
        
        conn.commit()
        print(f"\n✓ Na'vi '{name}' created successfully!")
        
    except pymysql.IntegrityError as e:
        conn.rollback()
        print(f"✗ Data integrity error: {e}", file=sys.stderr)
        print("  (Soul ID may already be assigned or Clan ID invalid)")
    except pymysql.Error as e:
        conn.rollback()
        print(f"✗ Database error: {e}", file=sys.stderr)
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}", file=sys.stderr)


def create_avatar_link(conn):
    """
    WRITE 3: Form an avatar link between human and Na'vi
    SQL: INSERT into Avatar
    """
    print_header("Form Avatar Link")
    
    try:
        # Show available humans and na'vi
        with conn.cursor() as cur:
            cur.execute("""
                SELECT h.Human_ID, CONCAT(h.F_Name, ' ', h.L_Name) as Name, c.Name as Company
                FROM Human h
                LEFT JOIN Company c ON h.Company_ID = c.Company_ID
                ORDER BY h.Human_ID
            """)
            humans = cur.fetchall()
            
            cur.execute("""
                SELECT n.Navi_ID, n.Name, cl.Clan_Name
                FROM Navi n
                LEFT JOIN Clan cl ON n.Clan_ID = cl.Clan_ID
                ORDER BY n.Navi_ID
            """)
            navis = cur.fetchall()
        
        print("\nAvailable Humans:")
        for h in humans[:10]:
            print(f"  ID {h['Human_ID']}: {h['Name']} ({h['Company']})")
        
        print("\nAvailable Na'vi:")
        for n in navis[:10]:
            print(f"  ID {n['Navi_ID']}: {n['Name']} ({n['Clan_Name']})")
        
        human_id = input("\nEnter Human ID: ").strip()
        navi_id = input("Enter Na'vi ID: ").strip()
        link_status = input("Link Status (default: Active): ").strip() or "Active"
        
        if not all([human_id, navi_id]):
            print("Both Human ID and Na'vi ID are required.")
            return
        
        sql = """
            INSERT INTO Avatar (Human_ID, Navi_ID, Link_Status, Total_Linked_Hours)
            VALUES (%s, %s, %s, 0)
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (human_id, navi_id, link_status))
        
        conn.commit()
        print(f"\n✓ Avatar link created successfully! (Human {human_id} ↔ Na'vi {navi_id})")
        
    except pymysql.IntegrityError as e:
        conn.rollback()
        print(f"✗ Data integrity error: {e}", file=sys.stderr)
        print("  (Link may already exist or invalid IDs)")
    except pymysql.Error as e:
        conn.rollback()
        print(f"✗ Database error: {e}", file=sys.stderr)
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}", file=sys.stderr)


def update_site_status(conn):
    """
    WRITE 4: Update aetherium site status and ownership
    SQL: UPDATE Aetherium_Site
    """
    print_header("Update Aetherium Site Status")
    
    try:
        # Show sites
        with conn.cursor() as cur:
            cur.execute("""
                SELECT ast.Site_ID, ast.Status, ast.Resource_Quantity,
                       e.Name as Ecosystem, a.Name as Controlled_By
                FROM Aetherium_Site ast
                JOIN Ecosystem e ON ast.Eco_ID = e.Eco_ID
                LEFT JOIN Alliance a ON ast.Alliance_ID = a.Alliance_ID
                ORDER BY ast.Site_ID
            """)
            sites = cur.fetchall()
            
            cur.execute("SELECT Alliance_ID, Name FROM Alliance ORDER BY Name")
            alliances = cur.fetchall()
        
        print("\nCurrent Sites:")
        for site in sites:
            print(f"  Site {site['Site_ID']}: {site['Status']} | {site['Resource_Quantity']} units | "
                  f"Ecosystem: {site['Ecosystem']} | Owner: {site['Controlled_By'] or 'None'}")
        
        site_id = input("\nEnter Site ID to update: ").strip()
        
        print("\nStatus Options: Unclaimed, Claimed, Depleted")
        new_status = input("New Status: ").strip()
        
        if new_status not in ['Unclaimed', 'Claimed', 'Depleted']:
            print("Invalid status. Must be: Unclaimed, Claimed, or Depleted")
            return
        
        if new_status == 'Claimed':
            print("\nAlliances:")
            for alliance in alliances:
                print(f"  {alliance['Alliance_ID']}: {alliance['Name']}")
            alliance_id = input("New Owner Alliance ID: ").strip()
        else:
            alliance_id = None
        
        if not confirm_action("Update this site?"):
            print("Action cancelled.")
            return
        
        sql = """
            UPDATE Aetherium_Site
            SET Status = %s, Alliance_ID = %s
            WHERE Site_ID = %s
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (new_status, alliance_id, site_id))
        
        conn.commit()
        print(f"\n✓ Site {site_id} updated to '{new_status}'!")
        
    except pymysql.Error as e:
        conn.rollback()
        print(f"✗ Database error: {e}", file=sys.stderr)
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}", file=sys.stderr)


def update_company_ethics(conn):
    """
    WRITE 5: Update company ethics rating
    SQL: UPDATE Company
    """
    print_header("Update Company Ethics Rating")
    
    try:
        # Show companies
        with conn.cursor() as cur:
            cur.execute("SELECT Company_ID, Name, Ethics_Rating FROM Company ORDER BY Name")
            companies = cur.fetchall()
        
        print("\nCompanies:")
        for comp in companies:
            print(f"  ID {comp['Company_ID']}: {comp['Name']} | "
                  f"Current Ethics: {comp['Ethics_Rating']}/10.00")
        
        company_id = input("\nEnter Company ID: ").strip()
        new_rating = input("New Ethics Rating (0.00 - 10.00): ").strip()
        
        try:
            rating_val = float(new_rating)
            if not (0.0 <= rating_val <= 10.0):
                print("Rating must be between 0.00 and 10.00")
                return
        except ValueError:
            print("Invalid rating format.")
            return
        
        if not confirm_action(f"Update ethics rating to {new_rating}?"):
            print("Action cancelled.")
            return
        
        sql = """
            UPDATE Company
            SET Ethics_Rating = %s
            WHERE Company_ID = %s
        """
        
        with conn.cursor() as cur:
            cur.execute(sql, (new_rating, company_id))
        
        conn.commit()
        print(f"\n✓ Company {company_id} ethics rating updated to {new_rating}!")
        
    except pymysql.Error as e:
        conn.rollback()
        print(f"✗ Database error: {e}", file=sys.stderr)
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}", file=sys.stderr)


def delete_alliance(conn):
    """
    WRITE 6 (DELETE): Delete an alliance (cascades to related data)
    SQL: DELETE from Alliance
    """
    print_header("Delete Alliance (ADMIN)")
    
    try:
        # Show alliances with stats
        with conn.cursor() as cur:
            cur.execute("""
                SELECT a.Alliance_ID, a.Name, a.Objective,
                       COUNT(DISTINCT c.Clan_ID) as Clans,
                       COUNT(DISTINCT ast.Site_ID) as Sites
                FROM Alliance a
                LEFT JOIN Clan c ON a.Alliance_ID = c.Alliance_ID
                LEFT JOIN Aetherium_Site ast ON a.Alliance_ID = ast.Alliance_ID
                GROUP BY a.Alliance_ID
                ORDER BY a.Name
            """)
            alliances = cur.fetchall()
        
        print("\nAlliances:")
        for alliance in alliances:
            print(f"  ID {alliance['Alliance_ID']}: {alliance['Name']}")
            print(f"    Clans: {alliance['Clans']} | Sites: {alliance['Sites']}")
            print(f"    Objective: {alliance['Objective']}")
        
        alliance_id = input("\nEnter Alliance ID to DELETE: ").strip()
        
        print("\n⚠ WARNING: This will:")
        print("  - Remove alliance from clans (set to NULL)")
        print("  - Remove alliance from sites (set to NULL)")
        print("  - Remove alliance from partnerships (set to NULL)")
        print("  - Remove related war records (set to NULL)")
        
        if not confirm_action("PERMANENTLY DELETE this alliance?"):
            print("Action cancelled.")
            return
        
        sql = "DELETE FROM Alliance WHERE Alliance_ID = %s"
        
        with conn.cursor() as cur:
            cur.execute(sql, (alliance_id,))
            rows_affected = cur.rowcount
        
        if rows_affected > 0:
            conn.commit()
            print(f"\n✓ Alliance {alliance_id} deleted successfully!")
        else:
            print(f"\n✗ Alliance {alliance_id} not found.")
        
    except pymysql.Error as e:
        conn.rollback()
        print(f"✗ Database error: {e}", file=sys.stderr)
    except Exception as e:
        conn.rollback()
        print(f"✗ Error: {e}", file=sys.stderr)


# ============================================================
# MENU SYSTEM
# ============================================================

def character_operations_menu(conn):
    """Submenu for character operations."""
    while True:
        print_header("CHARACTER OPERATIONS")
        print("""
1. Create Human Operative          [INSERT]
2. Create Na'vi Character          [INSERT]
3. Form Avatar Link                [INSERT]
4. View Humans by Company          [JOIN: 3 tables]
5. View Na'vi by Clan              [JOIN: 3 tables]
6. View Active Avatar Links        [JOIN: 4 tables]
7. View Na'vi Bonded Animals       [LEFT JOIN]

0. Back to Main Menu
        """)
        
        choice = input("Select operation: ").strip()
        
        if choice == '1':
            create_human(conn)
        elif choice == '2':
            create_navi(conn)
        elif choice == '3':
            create_avatar_link(conn)
        elif choice == '4':
            view_humans_by_company(conn)
        elif choice == '5':
            view_navi_by_clan(conn)
        elif choice == '6':
            view_avatar_links(conn)
        elif choice == '7':
            view_navi_bonded_animals(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


def alliance_politics_menu(conn):
    """Submenu for alliance and politics."""
    while True:
        print_header("ALLIANCE & POLITICS")
        print("""
1. View Alliance Resource Control  [GROUP BY + SUM]
2. View Company-Clan Partnerships  [JOIN: 3 tables]
3. Most War-Active Clans           [GROUP BY + HAVING]

0. Back to Main Menu
        """)
        
        choice = input("Select operation: ").strip()
        
        if choice == '1':
            view_alliance_resources(conn)
        elif choice == '2':
            view_company_clan_partnerships(conn)
        elif choice == '3':
            view_war_active_clans(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


def war_operations_menu(conn):
    """Submenu for war operations."""
    while True:
        print_header("WAR OPERATIONS")
        print("""
1. View Alliance War History       [JOIN: 5 tables + GROUP BY]

0. Back to Main Menu
        """)
        
        choice = input("Select operation: ").strip()
        
        if choice == '1':
            view_war_history(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


def aetherium_management_menu(conn):
    """Submenu for aetherium site management."""
    while True:
        print_header("AETHERIUM MANAGEMENT")
        print("""
1. View Sites by Ecosystem         [JOIN: 3 tables]
2. Update Site Status/Owner        [UPDATE]
3. Update Company Ethics Rating    [UPDATE]

0. Back to Main Menu
        """)
        
        choice = input("Select operation: ").strip()
        
        if choice == '1':
            view_sites_by_ecosystem(conn)
        elif choice == '2':
            update_site_status(conn)
        elif choice == '3':
            update_company_ethics(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


def intelligence_menu(conn):
    """Submenu for intelligence and analytics."""
    while True:
        print_header("INTELLIGENCE & ANALYTICS")
        print("""
1. Ecosystem Threat Analysis       [JOIN: 4 tables + AVG]

0. Back to Main Menu
        """)
        
        choice = input("Select operation: ").strip()
        
        if choice == '1':
            ecosystem_threat_analysis(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


def admin_operations_menu(conn):
    """Submenu for admin operations."""
    while True:
        print_header("ADMIN OPERATIONS")
        print("""
1. Delete Alliance (Cascade)       [DELETE]

0. Back to Main Menu
        """)
        
        choice = input("Select operation: ").strip()
        
        if choice == '1':
            delete_alliance(conn)
        elif choice == '0':
            break
        else:
            print("Invalid choice.")


def main_menu(conn):
    """Main menu loop."""
    while True:
        print("\n" + "="*60)
        print("     PANDORA CHRONICLES DATABASE SYSTEM")
        print("="*60)
        print("""
Mission Control: Select Operation Category

1. CHARACTER OPERATIONS
2. ALLIANCE & POLITICS
3. WAR OPERATIONS
4. AETHERIUM MANAGEMENT
5. INTELLIGENCE & ANALYTICS
6. ADMIN OPERATIONS

Q. Exit System
        """)
        print("="*60)
        
        choice = input("Enter choice: ").strip().lower()
        
        if choice == '1':
            character_operations_menu(conn)
        elif choice == '2':
            alliance_politics_menu(conn)
        elif choice == '3':
            war_operations_menu(conn)
        elif choice == '4':
            aetherium_management_menu(conn)
        elif choice == '5':
            intelligence_menu(conn)
        elif choice == '6':
            admin_operations_menu(conn)
        elif choice == 'q':
            print("\n" + "="*60)
            print("  Exiting Pandora Chronicles Database System...")
            print("  Connection terminated. Stay safe on Pandora.")
            print("="*60 + "\n")
            break
        else:
            print("Invalid choice. Please try again.")


# ============================================================
# MAIN ENTRY POINT
# ============================================================
def main():
    """Main application entry point."""
    print("\n" + "="*60)
    print("  PANDORA CHRONICLES - DATABASE INTERFACE")
    print("  Phase 4: Data & Applications Project")
    print("="*60)
    
    conn = get_connection()
    
    if not conn:
        print("Failed to establish database connection. Exiting.")
        sys.exit(1)
    
    try:
        main_menu(conn)
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
    except Exception as e:
        print(f"\nUnexpected error: {e}", file=sys.stderr)
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")


if __name__ == "__main__":
    main()
