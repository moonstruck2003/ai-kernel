from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes 
from dotenv import load_dotenv

load_dotenv() 
groq_api_key = os.getenv("GROQ_API_KEY") 

model = ChatGroq(model="openai/gpt-oss-120b", groq_api_key=groq_api_key)

#1.Create the Prompt Template

system_template = "Translate the following into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user",'{text}')
])

parser=StrOutputParser() 

#2. Create the chain
chain=prompt_template|model|parser

##app definition
app=FastAPI(title="Langchain Server",version="1.0.0",description="A simple langchain server using Runnable API")


##add chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app,host="localhost",port=8000)