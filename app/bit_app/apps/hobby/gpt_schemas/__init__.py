from bit_app.apps.common.classes import PromptOpenAI


SYSTEM_PROMPT = """
You are a hobby summarizer. For given list of hobby properties write a summary of that hobby, including all aspects.
"""


USER_PROMPT = """
You are given a name of hobby and a list of that hobby properties. Each property is ranked in scale 0-4. Write a
summary of that hobby, including all aspects.
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "summary": "Summary of the offer",
        }
    },
    "required": ["summary"]
}

def prompt_preparing_function():
    pass

HOBBY_SUMMARY = PromptOpenAI(
    system_prompt=SYSTEM_PROMPT,
    user_prompt=USER_PROMPT,
    schema=SCHEMA,
)