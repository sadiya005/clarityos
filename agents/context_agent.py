from utils.llm import ask_llm


def summarize_meeting(text):

    prompt = f"""
    Summarize the following meeting.

    Meeting:
    {text}

    Give:
    1. Key discussion points
    2. Concerns
    3. Decisions
    """

    return ask_llm(prompt)