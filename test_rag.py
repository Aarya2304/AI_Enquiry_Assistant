from utils.rag_pipeline import retrieve_context

query = "Do you provide placement support?"

context = retrieve_context(query)

print(context)