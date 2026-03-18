from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='xyz')

text = "Delhi is the capital of India"

vector = embeddings.embed_query(text)

print(str(vector))