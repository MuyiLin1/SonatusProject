from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings


# from langchain_voyageai import VoyageAIEmbeddings
# #https://python.langchain.com/v0.1/docs/integrations/text_embedding/voyageai/

def get_embedding_function():
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="bedrock-admin", region_name="us-east-1"
    # )
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings





