from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

# pyrefly: ignore [missing-import]
from embeddings import embeddings

DATA_FOLDER = Path("../data")

documents = []

for file in DATA_FOLDER.glob("*.txt"):

    text = file.read_text()

    documents.append(
        Document(
            page_content=text,
            metadata={
                "source": file.name
            }
        )
    )

db = Chroma.from_documents(
    documents,
    embedding=embeddings,
    persist_directory="./vector_db"
)

print("Knowledge Base Created Successfully")