import openai
from bit_app.settings import AzureOpenAI

openai_client = openai.AzureOpenAI(
    azure_endpoint=AzureOpenAI.ENDPOINT,
    api_key=AzureOpenAI.KEY,
    api_version=AzureOpenAI.API_VERSION,
)
