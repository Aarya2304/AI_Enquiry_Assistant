def detect_lead_intent(user_query):

    lead_keywords = [
        "interested",
        "enroll",
        "join",
        "admission",
        "fees",
        "contact",
        "register",
        "apply",
        "placement"
    ]

    user_query = user_query.lower()

    for keyword in lead_keywords:

        if keyword in user_query:
            return True

    return False