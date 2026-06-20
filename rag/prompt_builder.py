def build_prompt(
    village_name,
    ndvi,
    risk_score,
    water_distance,
    retrieved_docs
):

    retrieved_context = "\n\n".join(
        [
            f"[{d['source']}]\n{d['text']}"
            for d in retrieved_docs
        ]
    )

    prompt = f"""
You are an Earth Intelligence analyst.

Village Information
-------------------

Village: {village_name}

NDVI Mean: {ndvi:.3f}

Risk Score: {risk_score:.3f}

Distance To Water (m):
{water_distance:.2f}

Retrieved Knowledge
-------------------

{retrieved_context}

Tasks
-----

1. Explain the risk score.
2. Identify supporting evidence.
3. Identify contradicting evidence.
4. Discuss competing hypotheses.
5. Assign confidence:
   Low / Medium / High
6. Mention limitations.

Important:
Do not claim causality unless supported.
Discuss uncertainty explicitly.
"""

    return prompt