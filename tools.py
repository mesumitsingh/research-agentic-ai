import json
from datetime import datetime
from langchain_core.tools import StructuredTool
from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper


def save_to_txt(data: str, filename: str = "research_output.txt") -> str:
    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


save_tool = StructuredTool.from_function(
    func=save_to_txt,
    name="save_text_to_file",
    description="Saves structured research data to a text file.",
)


search = DuckDuckGoSearchRun()


def search_web(query: str) -> str:
    try:
        result =  search.run(query)
        
        if not result: 
            return "No result found"
        
        return result 

    except Exception as e:
        return f"Search error: {str(e)}"


search_tool = StructuredTool.from_function(
    func=search_web,
    name="search",
    description="Search the web for current information.",
)


api_wrapper = WikipediaAPIWrapper(top_k_results=5, doc_content_chars_max=1000)

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)