import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Load Knowledge Base
# -----------------------------

def load_knowledge_base():

    knowledge_chunks = []

    # Load FAQs
    with open("data/faqs.txt", "r", encoding="utf-8") as f:
        faq_text = f.read()

    knowledge_chunks.extend(faq_text.split("\n\n"))

    # Load institute info
    with open("data/institute_info.txt", "r", encoding="utf-8") as f:
        institute_text = f.read()

    knowledge_chunks.extend(institute_text.split("\n"))

    # Load courses
    courses_df = pd.read_csv("data/courses.csv")

    for _, row in courses_df.iterrows():

        course_text = f"""
        Course: {row['course']}
        Duration: {row['duration']}
        Fees: {row['fees']}
        Level: {row['level']}
        Placement Support: {row['placement_support']}
        Description: {row['description']}
        """

        knowledge_chunks.append(course_text)

    return knowledge_chunks


# -----------------------------
# Create Retriever
# -----------------------------

knowledge_base = load_knowledge_base()

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(knowledge_base)


# -----------------------------
# Retrieve Context
# -----------------------------

def retrieve_context(user_query, top_k=3):

    query_vector = vectorizer.transform([user_query])

    similarities = cosine_similarity(
        query_vector,
        tfidf_matrix
    ).flatten()

    top_indices = similarities.argsort()[-top_k:][::-1]

    retrieved_chunks = [
        knowledge_base[i]
        for i in top_indices
    ]

    context = "\n\n".join(retrieved_chunks)

    return context