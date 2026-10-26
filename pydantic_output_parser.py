from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-20b",
    temperature=0.2,
    max_tokens=512
)

class TopicInfo(BaseModel):
    key: str = Field(description="The name of the topic")
    description: str = Field(description="A brief explanation")
    difficulty: str = Field(description="Difficulty level")


parser = PydanticOutputParser(
    pydantic_object=TopicInfo
)

prompt = PromptTemplate(
    template=(
        "Explain {topic} briefly.\n"
        "Return the result according to these instructions:\n"
        "{format_instructions}"
    ),
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

formatted_prompt = prompt.format(topic="LangChain")


response = llm.invoke(formatted_prompt)

result = parser.invoke(response)

print(result)
print(type(result))
print(result.key)
print(result.description)

