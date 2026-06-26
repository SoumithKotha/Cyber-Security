from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

# pyrefly: ignore [missing-import]
from embeddings import embeddings

llm = ChatOllama(
    model="qwen3",
    temperature=0
)

db = Chroma(
    persist_directory="./vector_db",
    embedding_function=embeddings
)

retriever = db.as_retriever()

def ask_security(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are a cybersecurity analyst.

Use ONLY the information below.

Context:

{context}

Question:

{question}
"""

    response = llm.invoke(prompt)

    return response.content


if __name__ == "__main__":

    while True:

        question = input("Question: ")

        if question.lower() == "exit":
            break

        print()

        print(ask_security(question))

        print()