from dataclasses import dataclass


@dataclass
class PromptOpenAI:
    schema: dict
    system_prompt: str
    user_prompt: str
    prompt_preparing_function: callable = None
    prompt_changing_function: callable = None
