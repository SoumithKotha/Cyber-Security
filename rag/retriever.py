from langchain_chroma import Chroma

# pyrefly: ignore [missing-import]
from embeddings import embeddings

db = Chroma(
    persist_directory="./vector_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(
    search_kwargs={
        "k": 3
    }
)

query = input("Ask Security Question: ")

docs = retriever.invoke(query)

print()

for doc in docs:

    print("=" * 40)

    print(doc.page_content)

    print("=" * 40)