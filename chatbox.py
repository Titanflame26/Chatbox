from langchain_cohere.llms import Cohere
llm=Cohere(cohere_api_key="3ml84htGhfTvj2TffmAB22xNpj6xN6ZLpCkiXNje")
response = llm.invoke("who is bharadwaj.")
print(response)