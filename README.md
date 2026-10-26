# LangChain Practice with Groq

A hands-on Python project exploring LangChain fundamentals, prompt engineering, and structured LLM outputs using Python, LangChain, Pydantic, and Groq.

## 🚀 Project Overview

This project demonstrates how to create prompts, process JSON responses, validate structured data, and build chat-based prompts using LangChain and Groq's hosted language models.

## 🛠️ Tech Stack

- **Python 3.12** — Programming language
- **LangChain Core** — Prompt templates and output parsers
- **LangChain Groq** — Integration with Groq models
- **Groq API** — Language model inference
- **Pydantic** — Structured data validation
- **python-dotenv** — Environment variable management
- **Git and GitHub** — Version control

**Model used:** `openai/gpt-oss-20b`

## 📁 Project Structure

```text
Langchain practice/
│
├── venv/                       # Local virtual environment
├── .env                        # Groq API key (not uploaded)
├── .gitignore                  # Files excluded from Git
├── README.md                   # Project documentation
│
├── prompt_template.py          # PromptTemplate
├── json_output_parser.py       # JsonOutputParser
├── pydantic_output_parser.py   # PydanticOutputParser
└── chat_template.py            # Combined chat prompt and Pydantic parser
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/langchain-practice.git
cd langchain-practice
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create and activate a virtual environment

For Windows PowerShell:

```powershell
py -3.12 -m venv venv
.\venv\Scripts\Activate.ps1
```

If you already have a compatible virtual environment, activate the existing one instead.

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
python -m pip install langchain-core langchain-groq python-dotenv pydantic
```

### 4. Configure the Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

Replace the placeholder with your actual key from the [Groq Console](https://console.groq.com/).

**Security:** Never commit your `.env` file or expose your API key in a public repository.

## 📚 Concepts Explored

### 1. PromptTemplate

File: `prompt_template.py`

Creates reusable text prompts with variables that can be populated dynamically.

**What I learned:**
- Creating reusable prompts
- Defining input variables
- Formatting prompts before sending them to an LLM

### 2. JsonOutputParser

File: `json_output_parser.py`

Parses JSON-formatted LLM responses into Python data structures.

**What I learned:**
- Requesting structured JSON output
- Parsing responses into Python dictionaries
- Accessing values using dictionary keys

### 3. PydanticOutputParser

File: `pydantic_output_parser.py`

Uses a Pydantic model to define the expected output structure and validate parsed responses.

**What I learned:**
- Defining structured data models with `BaseModel`
- Describing fields with `Field`
- Parsing responses into Pydantic objects
- Accessing structured data through model attributes

### 4. ChatPromptTemplate + PydanticOutputParser

File: `chat_template.py`

Combines `ChatPromptTemplate` and `PydanticOutputParser` into one workflow.

The chat prompt provides system instructions and a human message. Formatting instructions from the Pydantic parser guide the model toward the expected output structure.

**Workflow:**

1. Define the output schema using Pydantic.
2. Create a `PydanticOutputParser`.
3. Build a chat prompt using `ChatPromptTemplate`.
4. Insert the parser's formatting instructions into the prompt.
5. Send the messages to the Groq model using `ChatGroq`.
6. Parse and validate the model response.
7. Access the resulting fields as object attributes.

**What I learned:** How to combine chat-based prompting and structured output parsing in a single LangChain application.

## ▶️ Running the Examples

Activate your existing virtual environment and run each script from the project directory:

```powershell
python prompt_template.py
```

```powershell
python json_output_parser.py
```

```powershell
python pydantic_output_parser.py
```

```powershell
python chat_template.py
```

Each script demonstrates a separate learning example, with the final script combining chat prompts and Pydantic parsing.

## 🔄 Combined Application Workflow

```text
ChatPromptTemplate
        |
        v
Formatted Chat Messages
        |
        v
ChatGroq (Groq API)
        |
        v
LLM Response
        |
        v
PydanticOutputParser
        |
        v
Validated TopicInfo Object
```

The Pydantic model defines the expected fields, such as the topic name, description, and difficulty level.

## 🔐 Git and Security

The root `.gitignore` should exclude sensitive and generated files:

```gitignore
venv/
.venv/
.env
.env.*
!.env.example
__pycache__/
*.py[cod]
.vscode/
```

Keep your virtual environment and API credentials local. If an API key has already been exposed publicly, revoke it and generate a replacement.

## 🎯 Future Learning Goals

- LangChain chains and the pipe operator (`|`)
- Runnable sequences
- Prompt chaining
- Conversation history and memory
- Embeddings and vector databases
- Retrieval-Augmented Generation (RAG)
- Building interactive LLM applications

## 👨‍💻 About This Project

This repository documents my hands-on learning journey with LangChain and large language models. It focuses on understanding prompts, output parsers, Pydantic validation, and integrating these components with the Groq API.

---

**Built with Python, LangChain, Pydantic, and Groq.**
