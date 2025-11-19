import pymysql
from getpass import getpass

# ============================================================
# DATABASE CONNECTION
# ============================================================
def get_connection():
    print("Enter MySQL credentials:")
    user = input("Username: ")
    password = getpass("Password: ")

    try:
        conn = pymysql.connect(
            host="localhost",
            user=user,
            password=password,
            database="pandora_chronicles_db",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("\nConnected successfully!\n")
        return conn
    except Exception as e:
        print("Connection failed:", e)
        exit()



# ============================================================
# INSERT OPERATIONS
# ============================================================
def insert_human(conn):
    print("\n--- Insert New Human Operative ---")
    try:
        f = input("First Name: ")
        l = input("Last Name: ")
        rank = input("Rank: ")
        weapon = input("Weapon Type: ")
        soul = input("Soul_ID: ")
        company = input("Company_ID: ")

        sql = """
            INSERT INTO Human (Human_ID, F_Name, L_Name, Rank, Weapon_Type, Soul_ID, Company_ID)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        new_id = int(input("Enter new Human_ID: "))

        with conn.cursor() as cur:
            cur.execute(sql, (new_id, f, l, rank, weapon, soul, company))
        conn.commit()
        print("Human added successfully!")

    except Exception as e:
        print("Error:", e)



def insert_navi(conn):
    print("\n--- Insert New Na'vi ---")
    try:
        name = input("Name: ")
        age = input("Age: ")
        soul = input("Soul_ID: ")
        clan = input("Clan_ID: ")
        new_id = int(input("Enter new Navi_ID: "))

        sql = """
            INSERT INTO Navi (Navi_ID, Name, Age, Soul_ID, Clan_ID)
            VALUES (%s, %s, %s, %s, %s)
        """

        with conn.cursor() as cur:
            cur.execute(sql, (new_id, name, age, soul, clan))
        conn.commit()
        print("Na'vi added successfully!")

    except Exception as e:
        print("Error:", e)



# ============================================================
# UPDATE OPERATIONS
# ============================================================
def update_site_status(conn):
    print("\n--- Update Aetherium Site Status ---")
    site = input("Enter Site_ID: ")
    new_status = input("Enter new status (Unclaimed/Claimed/Depleted): ")

    sql = """
        UPDATE Aetherium_Site
        SET Status = %s
        WHERE Site_ID = %s
    """

    try:
        with conn.cursor() as cur:
            cur.execute(sql, (new_status, site))
        conn.commit()
        print("Status updated successfully!")
    except Exception as e:
        print("Error:", e)



def update_company_ethics(conn):
    print("\n--- Update Company Ethics Rating ---")
    cid = input("Enter Company_ID: ")
    new_rating = input("New Ethics Rating: ")

    sql = """UPDATE Company SET Ethics_Rating = %s WHERE Company_ID = %s"""

    try:
        with conn.cursor() as cur:
            cur.execute(sql, (new_rating, cid))
        conn.commit()
        print("Company ethics updated!")
    except Exception as e:
        print("Error:", e)



def update_war_outcome(conn):
    print("\n--- Update War Outcome ---")
    wid = input("Enter War_ID: ")
    new_outcome = input("New Outcome: ")

    sql = """UPDATE War SET Outcome = %s WHERE War_ID = %s"""

    try:
        with conn.cursor() as cur:
            cur.execute(sql, (new_outcome, wid))
        conn.commit()
        print("War outcome updated!")
    except Exception as e:
        print("Error:", e)



# ============================================================
# DELETE OPERATIONS
# ============================================================
def delete_alliance(conn):
    print("\n--- Delete Alliance ---")
    aid = input("Enter Alliance_ID: ")

    sql = """DELETE FROM Alliance WHERE Alliance_ID = %s"""

    try:
        with conn.cursor() as cur:
            cur.execute(sql, (aid,))
        conn.commit()
        print("Alliance deleted (and cascaded).")
    except Exception as e:
        print("Error:", e)



# ============================================================
# READ / SELECT OPERATIONS
# ============================================================
def show_all_humans(conn):
    print("\n--- All Humans ---")
    sql = "SELECT * FROM Human"
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        for r in rows:
            print(r)



def list_unclaimed_sites(conn):
    print("\n--- Unclaimed Aetherium Sites ---")
    sql = """SELECT Site_ID, Resource_Quantity FROM Aetherium_Site WHERE Status = 'Unclaimed'"""
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        for r in rows:
            print(r)



def navi_by_clan(conn):
    print("\n--- Na'vi by Clan ---")
    clan = input("Enter Clan_ID: ")
    sql = "SELECT * FROM Navi WHERE Clan_ID = %s"
    with conn.cursor() as cur:
        cur.execute(sql, (clan,))
        rows = cur.fetchall()
        for r in rows:
            print(r)



def war_details(conn):
    print("\n--- All War Records ---")
    sql = "SELECT * FROM War"
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        for r in rows:
            print(r)



def show_ecosystems(conn):
    print("\n--- Ecosystems ---")
    sql = "SELECT * FROM Ecosystem"
    with conn.cursor() as cur:
        cur.execute(sql)
        rows = cur.fetchall()
        for r in rows:
            print(r)



# ============================================================
# MENU
# ============================================================
def menu():
    print("""
================= PANDORA CHRONICLES DB =================
1. Insert Human
2. Insert Na'vi

3. Update Site Status
4. Update Company Ethics
5. Update War Outcome

6. Delete Alliance

7. Show All Humans
8. List Unclaimed Aetherium Sites
9. Show Na'vi in a Clan
10. Show War Details
11. Show Ecosystems

0. Exit
==========================================================
""")


# ============================================================
# MAIN PROGRAM LOOP
# ============================================================
def main():
    conn = get_connection()

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            insert_human(conn)
        elif choice == "2":
            insert_navi(conn)
        elif choice == "3":
            update_site_status(conn)
        elif choice == "4":
            update_company_ethics(conn)
        elif choice == "5":
            update_war_outcome(conn)
        elif choice == "6":
            delete_alliance(conn)
        elif choice == "7":
            show_all_humans(conn)
        elif choice == "8":
            list_unclaimed_sites(conn)
        elif choice == "9":
            navi_by_clan(conn)
        elif choice == "10":
            war_details(conn)
        elif choice == "11":
            show_ecosystems(conn)
        elif choice == "0":
            print("Exiting...")
            conn.close()
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
