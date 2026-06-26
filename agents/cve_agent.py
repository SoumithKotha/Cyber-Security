from pydantic import BaseModel
from langchain_ollama import ChatOllama

class CVEReport(BaseModel):
    cve: str
    severity: str
    cvss: float
    description: str
    remediation: str

llm = ChatOllama(
    model="qwen3",
    temperature=0
)

def analyze(cve):

    prompt=f"""
Return JSON.

Analyze {cve}

Fields:
cve
severity
cvss
description
remediation
"""

    return llm.invoke(prompt)