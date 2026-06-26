from pydantic import BaseModel
from langchain_ollama import ChatOllama
import json

# Initialize local LLM
llm = ChatOllama(
    model="qwen3",
    temperature=0
)


class MitreAnalysis(BaseModel):
    technique_id: str
    technique_name: str
    tactic: str
    description: str
    detection: str
    mitigation: str


def map_to_mitre(vulnerability: str) -> dict:
    """
    Maps a vulnerability or attack description to MITRE ATT&CK.
    """

    prompt = f"""
You are an expert Cybersecurity Analyst.

Map the following vulnerability or attack to the MITRE ATT&CK Framework.

Input:
{vulnerability}

Return ONLY valid JSON.

Format:

{{
    "technique_id":"",
    "technique_name":"",
    "tactic":"",
    "description":"",
    "detection":"",
    "mitigation":""
}}

Do not include explanations.
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except Exception:
        return {
            "error": "Unable to parse model output",
            "raw_output": response.content
        }


if __name__ == "__main__":

    attack = input("Enter Vulnerability or Attack: ")

    result = map_to_mitre(attack)

    print("\nMITRE Mapping\n")

    print(json.dumps(result, indent=4))