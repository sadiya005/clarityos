from utils.llm import ask_llm


def extract_tasks(text):

    prompt = f"""
Extract action items from this meeting.

Meeting:
{text}

IMPORTANT RULES:

1. Extract ONLY explicit tasks.

2. A task must contain:
- Action
- Owner or assignee

3. Do NOT invent tasks.

4. Do NOT create tasks from:
- Concerns
- Risks
- Discussions
- Problems

5. If owner is missing, write:

Owner: Unassigned
Confidence: Low

6. If deadline is missing, write:

Deadline: Not Specified

7. If no explicit tasks exist, return:

No explicit tasks found.

Format:

Task:
Owner:
Deadline:
Priority:
Confidence:

Return only tasks.
"""

    return ask_llm(prompt)