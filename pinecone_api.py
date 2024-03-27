
import config
from pinecone import Pinecone
from langchain.memory import VectorStoreRetrieverMemory
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as lang_pinecone



# Initialize Pinecone
pc = Pinecone(api_key=config.PINECONE_KEY)



def memory(input_key, memory_key):
    text_field = "text"
    model_name = "text-embedding-ada-002"
    embed = OpenAIEmbeddings(model=model_name, openai_api_key=config.OPENAI_KEY)

    # switch back to normal index for langchain
    index_name = 'chathistory'
    index = pc.Index(index_name)

    # Connect to vectorstore
    vectorstore = lang_pinecone(index, embed.embed_query, text_field)
    retriever = vectorstore.as_retriever(search_kwargs=dict(k=5))
    return VectorStoreRetrieverMemory(retriever=retriever, input_key=input_key, memory_key=memory_key)