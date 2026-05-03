import sqlite3

DB_PATH = "database/leads.db"


# -----------------------------
# Database Connection
# -----------------------------

def get_connection():

    conn = sqlite3.connect(DB_PATH)

    return conn


# -----------------------------
# Initialize Database
# -----------------------------

def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    # Leads table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        email TEXT,
        phone TEXT,

        interested_course TEXT,

        lead_score INTEGER DEFAULT 0,

        lead_status TEXT DEFAULT 'New',

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()

    conn.close()


# -----------------------------
# Insert Lead
# -----------------------------

def insert_lead(
    name,
    email,
    phone,
    interested_course,
    lead_score
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO leads (
        name,
        email,
        phone,
        interested_course,
        lead_score
    )

    VALUES (?, ?, ?, ?, ?)

    """, (
        name,
        email,
        phone,
        interested_course,
        lead_score
    ))

    conn.commit()

    conn.close()


# -----------------------------
# Fetch Leads
# -----------------------------

def fetch_all_leads():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM leads
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


# -----------------------------
# Main
# -----------------------------

if __name__ == "__main__":

    initialize_database()

    print("Database initialized successfully.")