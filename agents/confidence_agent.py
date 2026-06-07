from utils.llm import ask_llm

def confidence_score(
        meeting_summary,
        data_insights,
        correlation_report):

    prompt = f"""
Meeting Summary:
{meeting_summary}

Data Insights:
{data_insights}

Correlation Report:
{correlation_report}

Generate confidence scores.

Rules:

100% = Fully supported by uploaded data

70-90% = Strong evidence available

40-60% = Mentioned in meeting but only partially supported

10-30% = Very weak evidence

0% = No supporting evidence available

IMPORTANT:

If evidence is missing:

Confidence = 0%

Examples:

Customer complaints | 0% | No complaint data available

Inventory shortage | 0% | No inventory data available

Regional revenue decline | 0% | No trend data available

Format:

Claim | Confidence % | Evidence

Example:

Revenue decline | 50% | Mentioned in meeting but not proven by data

Customer complaints | 0% | No complaint data available

Inventory shortage | 0% | No inventory data available

South region underperformance | 100% | Supported by regional sales data

Only output confidence table.
"""

    return ask_llm(prompt)