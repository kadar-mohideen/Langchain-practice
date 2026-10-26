from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate


load_dotenv()
llm =ChatGroq(api_key=os.environ.get("GROQ_API_KEY"),
              model = "openai/gpt-oss-20b",
              temperature=0.7,
              max_tokens=512)

template = PromptTemplate.from_template("Explain {topic} in {line}.")

prompt = template.invoke(
    {"topic":"Langchain","line":3}
)

response = llm.invoke(prompt)
print(response.content)