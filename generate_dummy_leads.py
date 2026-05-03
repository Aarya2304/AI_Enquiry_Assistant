import random
import sqlite3
from datetime import datetime, timedelta

DB_PATH = "database/leads.db"

courses = [
    "AI Foundations",
    "Machine Learning Bootcamp",
    "Data Science Professional",
    "NLP Specialization",
    "Python for AI",
    "Generative AI Engineering"
]

names = [
    "Aarav Sharma",
    "Priya Mehta",
    "Rohan Verma",
    "Sneha Patil",
    "Arjun Rao",
    "Neha Kapoor",
    "Rahul Singh",
    "Ananya Joshi",
    "Vikram Das",
    "Isha Nair"
]

statuses = [
    "New",
    "Interested",
    "Follow-up"
]

conn = sqlite3.connect(DB_PATH)

cursor = conn.cursor()

for i in range(50):

    name = random.choice(names)

    email = f"user{i}@gmail.com"

    phone = f"98{random.randint(10000000, 99999999)}"

    course = random.choice(courses)

    lead_score = random.randint(20, 95)

    status = random.choice(statuses)

    random_date = datetime.now() - timedelta(
        days=random.randint(0, 15)
    )

    cursor.execute("""

    INSERT INTO leads (
        name,
        email,
        phone,
        interested_course,
        lead_score,
        lead_status,
        created_at
    )

    VALUES (?, ?, ?, ?, ?, ?, ?)

    """, (
        name,
        email,
        phone,
        course,
        lead_score,
        status,
        random_date
    ))

conn.commit()

conn.close()

print("50 dummy leads inserted successfully.")