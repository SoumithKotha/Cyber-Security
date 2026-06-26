from agents.cve_agent import llm
def threat_score(cve):

    prompt=f"""
Is {cve} actively exploited?

Return

Threat Level

Known Exploitation

Recommendation
"""

    return llm.invoke(prompt)