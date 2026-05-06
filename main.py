import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from tools import search_tool, wiki_tool,save_tool


load_dotenv()


class ResearchResponse(BaseModel):

    topic: str = Field(description="The research topic being addressed.")

    summary: str = Field(description=( "A detailed research report with facts, trends, context, comparisons, and caveats."))

    sources: list[str] = Field(description="Sources used during research.")
    tools_used: list[str] = Field(description="Exact tool names used.")



llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-4o-mini"
)

prompt = """
        You are a research assistant that produces thorough, well-sourced research reports.

        Use available tools whenever needed.

        Always provide:
        - accurate facts
        - detailed explanations
        - trends
        - comparisons
        - caveats

        You MUST fill all schema fields.

        For sources:
        - include websites, Wikipedia pages, or search references used
        - never leave sources empty

        For tools_used:
        - include exact tool names used

        If user asks to save data:
        - use save_text_to_file tool
        """


tools = [search_tool, wiki_tool, save_tool]


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt,
    response_format=ResearchResponse,
)



# query = input("What can I help you research? ")
query = "south east asia population, save to a file"


raw_response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": query
            }
        ]
    }
)


try:

    structured_response = raw_response["structured_response"]

    print(structured_response.model_dump_json(indent=2))

except Exception as e:
    print("Error:", e, "\n\nRaw Response:\n", raw_response)