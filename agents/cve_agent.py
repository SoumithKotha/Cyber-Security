# pyrefly: ignore [missing-import]
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3",
    temperature=0
)

def analyze_cve(cve_id: str):

    prompt = f"""
    You are a cybersecurity analyst.

    Analyze the vulnerability {cve_id}.

    Return:

    1. Vulnerability Name
    2. Severity
    3. CVSS Score
    4. Description
    5. Remediation

    Format clearly.
    """

    response = llm.invoke(prompt)

    return response.content