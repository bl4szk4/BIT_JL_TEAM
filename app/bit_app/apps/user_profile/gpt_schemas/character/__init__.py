from bit_app.apps.common.classes import PromptOpenAI


SYSTEM_PROMPT = """
You are a person categorizer. For given person summary create their categorization.
"""


USER_PROMPT = """
You are given a summary of a person. Decide how each category describes that person in scale 0-5.
"""

SCHEMA = {
    "type": "object",
    "properties": {
        "traits": {
            "type": "array",
            "description": "List of traits with their integer values",
            "items": {
                "type": "object",
                "properties": {
                    "key": {
                        "type": "string",
                        "enum": [
                            "Adventurousness",
                            "Conscientiousness",
                            "Extraversion",
                            "Neuroticism",
                            "Openness",
                            "Perseverance",
                            "Social Connectedness",
                            "Curiosity",
                            "Risk Tolerance",
                            "Emotional Resonance"
                        ],
                        "description": "The name of the trait",
                    },
                    "value": {
                        "type": "integer",
                        "description": "The value of the trait on a defined scale",
                    },
                },
                "required": ["key", "value"]
            },
        },
    },
    "required": ["traits"]
}


def prompt_changing_function(data: dict):
    result = data.get("traits")
    data_out = {}
    for trait in result:
        data_out[trait["key"]] = trait["value"]

    return data_out


USER_CHARACTER = PromptOpenAI(
    system_prompt=SYSTEM_PROMPT,
    user_prompt=USER_PROMPT,
    schema=SCHEMA,
    prompt_changing_function=prompt_changing_function
)