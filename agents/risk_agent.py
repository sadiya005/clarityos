from utils.llm import ask_llm

def identify_risks(
        meeting_summary,
        data_insights):

    prompt = f"""
You are a business risk analyst.

Meeting Summary:
{meeting_summary}

Data Insights:
{data_insights}

IMPORTANT RULES:

1. Only identify risks explicitly mentioned in:

* Meeting discussion
  OR
* Uploaded dataset

2. Do not invent new risks.

3. Assign:

* High
* Medium
* Low

ONLY when supporting evidence exists in the uploaded dataset.

4. If the dataset cannot verify a risk, use:

Severity: Not Verifiable

Reason: <why evidence is missing>

5. Do NOT assign High, Medium, or Low to risks that are only mentioned in the meeting.

6. Examples:

Risk: Inventory shortages
Severity: Not Verifiable
Reason: Inventory data not provided.

Risk: Customer complaint trend
Severity: Not Verifiable
Reason: Complaint data not provided.

Risk: Regional revenue decline
Severity: Not Verifiable
Reason: Region-specific revenue trend data not provided.

7. Recommendations must be practical and based only on available evidence.

8. Be factual and avoid assumptions.

Identify:

1. Business Risks
2. Operational Risks
3. Recommended Actions

Format:

Business Risks

Risk:
Severity:
Reason:
Recommendation:

Operational Risks

Risk:
Severity:
Reason:
Recommendation:

Recommended Actions

* Action 1
* Action 2

Keep concise.
"""


    return ask_llm(prompt)