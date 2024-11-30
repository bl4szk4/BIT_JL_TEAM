from langchain.embeddings import AzureOpenAIEmbeddings
from bit_app.apps.common.consts import AZURE_EMBEDDINGS_DEPLOYMENT_NAME
from bit_app.settings import AzureEmbedding


def generate_embedded_data(text: str) -> list[float]:
    azure_embedding = AzureOpenAIEmbeddings(
        deployment=AZURE_EMBEDDINGS_DEPLOYMENT_NAME,
        openai_api_key=AzureEmbedding.KEY,
        azure_endpoint=AzureEmbedding.ENDPOINT,
        openai_api_version=AzureEmbedding.API_VERSION,
    )

    return azure_embedding.embed_query(text)
