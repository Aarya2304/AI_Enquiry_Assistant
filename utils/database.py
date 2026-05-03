import sqlite3
import pandas as pd

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

# -----------------------------
# Fetch Dashboard Metrics
# -----------------------------

def get_dashboard_metrics():

    conn = get_connection()

    cursor = conn.cursor()

    # Total leads
    cursor.execute("""
    SELECT COUNT(*) FROM leads
    """)
    total_leads = cursor.fetchone()[0]

    # Average lead score
    cursor.execute("""
    SELECT AVG(lead_score) FROM leads
    """)
    avg_score = cursor.fetchone()[0]

    # High intent leads
    cursor.execute("""
    SELECT COUNT(*) FROM leads
    WHERE lead_score >= 50
    """)
    high_intent = cursor.fetchone()[0]

    conn.close()

    return {
        "total_leads": total_leads,
        "avg_score": round(avg_score or 0, 2),
        "high_intent": high_intent
    }

# -----------------------------
# Fetch Leads DataFrame
# -----------------------------

def fetch_leads_dataframe():

    conn = get_connection()

    query = """
    SELECT * FROM leads
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    return df