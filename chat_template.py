
from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()


class TopicInfo(BaseModel):
    key: str = Field(description="Topic name")
    description: str = Field(description="Brief explanation")
    difficulty: str = Field(
        description="Difficulty level: Beginner, Intermediate, or Advanced"
    )


llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-20b",
    temperature=0.2,
    max_tokens=512
)


parser = PydanticOutputParser(
    pydantic_object=TopicInfo
)


chat_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You explain AI concepts clearly. Follow the required output format."
    ),
    (
        "human",
        "Explain {topic} to a beginner.\n{format_instructions}"
    )
])


messages = chat_template.invoke({
    "topic": "Pydantic",
    "format_instructions": parser.get_format_instructions()
})


response = llm.invoke(messages)


result = parser.invoke(response)


print("STRUCTURED OUTPUT:")
print(result)

print("\nTOPIC:", result.key)
print("DESCRIPTION:", result.description)
print("DIFFICULTY:", result.difficulty)

print("\nRESULT TYPE:", type(result))
