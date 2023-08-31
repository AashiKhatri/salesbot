# pip install -q langchain openai chromadb
# pip install tiktoken

from langchain.document_loaders import CSVLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os
import joblib

os.environ["OPENAI_API_KEY"] = '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'
# Load the documents
loader = CSVLoader(file_path='salesbot.csv')

# Create an index using the loaded documents
index_creator = VectorstoreIndexCreator()
docsearch = index_creator.from_loaders([loader])

chain = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=docsearch.vectorstore.as_retriever(), input_key="question")

query = "Yes, tell me about your services."
response = chain({"question": query})
print(response['result'])
