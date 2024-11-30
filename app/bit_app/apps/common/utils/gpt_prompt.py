import json

from bit_app.apps.common.consts import AZURE_OPENAI_ENGINE_NAME
from bit_app.apps.common.openai import openai_client


def prompt_openai(
    system_prompt: str,
    user_prompt: str,
    schema: dict,
    engine_name: str = AZURE_OPENAI_ENGINE_NAME,
    temperature: float = 0,
    function_name: str = "gpt_prompt",
    context: str = "",
) -> tuple:
    completion = openai_client.chat.completions.create(
        model=engine_name,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt + "\n" + context,
            },
        ],
        temperature=temperature,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": function_name,
                    "parameters": schema,
                },
            }
        ],
        tool_choice={
            "type": "function",
            "function": {"name": function_name},
        },
    )


    response = completion.choices[0].message.tool_calls[0].function.arguments

    return json.loads(response, strict=False)
