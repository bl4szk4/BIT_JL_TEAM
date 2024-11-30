from bit_app.apps.common.classes import PromptOpenAI


SYSTEM_PROMPT = """
You are a person summarizer. For given list of questions with answers write a summary of that person, including all aspects.
"""


USER_PROMPT = """
You are given a list of questions that were asked to the user with their answers. Provide me a characteristic of that 
user. Characteristic should be short and based on those questions with answers.
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


def prompt_preparing_function(quiz_data: dict):
    pass


HOBBY_SUMMARY = PromptOpenAI(
    system_prompt=SYSTEM_PROMPT,
    user_prompt=USER_PROMPT,
    schema=SCHEMA,
    prompt_preparing_function=prompt_preparing_function
)