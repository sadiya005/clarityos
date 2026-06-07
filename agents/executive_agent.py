from utils.llm import ask_llm

def executive_summary(
        summary,
        tasks,
        correlation,
        confidence,
        risks):

    prompt = f"""
Meeting Summary:
{summary}

Tasks:
{tasks}

Correlation:
{correlation}

Confidence:
{confidence}

Risks:
{risks}

Create an executive briefing.

IMPORTANT:

1. Do NOT present unverified claims as facts.

2. If a claim is not supported by the dataset, write:

"The meeting raised concerns about ..."

instead of:

"... is occurring."

3. Distinguish between:
- Verified findings
- Meeting concerns
- Not verifiable items

4. Use information from Correlation, Confidence, and Risks sections.

Include:

1. Situation Overview
2. Verified Findings
3. Key Risks
4. Immediate Actions
5. Recommendations

Keep under 200 words.

Use concise executive language.
"""

    return ask_llm(prompt)