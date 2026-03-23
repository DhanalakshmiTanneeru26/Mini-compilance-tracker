import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    country TEXT,
    entity_type TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    title TEXT,
    category TEXT,
    due_date TEXT,
    status TEXT
)
""")

# Reset data
conn.execute("DELETE FROM clients")
conn.execute("DELETE FROM tasks")

# New clients
conn.execute("INSERT INTO clients VALUES (NULL,'TechNova Solutions Pvt Ltd','India','Private')")
conn.execute("INSERT INTO clients VALUES (NULL,'GreenField Enterprises LLP','India','LLP')")
conn.execute("INSERT INTO clients VALUES (NULL,'SkyBridge Consulting Pvt Ltd','India','Private')")

conn.commit()
conn.close()