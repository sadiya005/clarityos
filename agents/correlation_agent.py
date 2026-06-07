from utils.llm import ask_llm

def correlate_insights(meeting_summary, data_insights):

    prompt = f"""
You are an enterprise analyst.

Meeting Summary:
{meeting_summary}

Data Insights:
{data_insights}

Compare the meeting discussion with the uploaded data.

IMPORTANT RULES:

1. Only use evidence that exists in the uploaded dataset.

2. If the uploaded data does not contain evidence for a claim, mark it as:

Not Verifiable
Reason: Data not available.

3. Do NOT assume:
- Inventory shortages
- Customer complaints
- Regional revenue decline
- Future performance impact

unless explicit evidence exists in the uploaded data.

4. Be conservative and factual. Do not speculate.

Return:

## Supported Claims

## Unsupported Claims

## Not Verifiable Claims

## Additional Data Findings

Keep concise.
"""

    return ask_llm(prompt)