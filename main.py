import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_agent
from langchain_core.output_parsers import PydanticOutputParser
from tools import search_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-4o-mini"
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a research assistant."
            "Answer the query and return ONLY in this format:\n{format_instructions}"
        ),
        ("human", "{query}")
    ]
).partial(format_instructions=parser.get_format_instructions())

tools=[search_tool]
agent = create_agent( 
    model = llm, 
    tools=tools, 
    system_prompt="You are a research assistant"
)


query = input("What can I help you research?")
raw_response = agent.invoke(
    { 
        "messages" : [ 
            { 
                "role" : "user",
                "content" : prompt.format(query)
            }
        ]
    }
)

print(raw_response)

content = raw_response["messages"][-1].content
print(content)