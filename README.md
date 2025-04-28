# Function Calling with Ollama and Web Search

![Function Calling](images/function_calling.jpg)

A smart search assistant that combines Ollama's LLM capabilities with web search functionality using function calling. The assistant can decide when to search the web for additional information to answer questions accurately.

**Read the article for more details**: [Tool use and function calling in LLMs](https://www.apideck.com/blog/llm-tool-use-and-function-calling)

## Watch it in Action

![Ollama Search Assistant](./images/Ollama_Search.gif)

## Features

- Function calling with Ollama
- Web search integration via SearchAPI
- Smart decision-making on when to use web search
- Automatic summarization of search results

## Setup

1. Install dependencies:

```bash
pip install ollama python-dotenv requests
```

2. Create `.env` file in project root:

```
SEARCH_API_KEY=your_api_key_here
```

3. Ensure Ollama is running locally

## Project Structure

```
.
├── .env
├── search_tool.py  # Search functionality and utilities
└── main.py        # Main application logic
```

## Usage

Run the assistant:

```bash
python main.py
```

Example interaction:

```
What would you like to know? What's the latest research on quantum computing?
Processing your question...
Searching the web...
Answer: [Ollama's response with current information]
```

## Requirements

- Python 3.12+
- Ollama installed and running
- SearchAPI key (get from searchapi.io)
