from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-3-xyz', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Jaipur is the capital of Rajasthan",
    "Paris is the capital of France"
]

result = embedding.embed_documents(documents)

print(str(result))