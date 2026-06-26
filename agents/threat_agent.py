# pyrefly: ignore [missing-import]
from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3")

def analyze_threat(cve_data):

    prompt = f"""
    You are a threat intelligence analyst.

    Analyze:

    {cve_data}

    Return:
    - Threat level
    - Active exploitation status
    - Recommended actions
    """

    response = llm.invoke(prompt)

    return response.content