
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    api_key=os.environ.get("GROQ_API_KEY"),
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_tokens=512
)

parser = JsonOutputParser()

prompt = PromptTemplate(
    template=(
        "Give a brief explanation of LangChain. Return exactly one JSON object "
        "with a string field named \"key\" and a string field named "
        "\"description\".\n{format_instructions}"
    ),
    input_variables=[],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

formatted_prompt = prompt.format()
response = llm.invoke(formatted_prompt)
result = parser.invoke(response)
print(result)
print(type(result))
