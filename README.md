# Ollama Search Tool

A simple tool that searches the web using SearchAPI and summarizes results using Ollama's LLM.

## Setup

1. Install dependencies:

```bash
pip install ollama python-dotenv requests
```

2. Create `.env` file:

```
SEARCH_API_KEY=your_api_key_here
```

3. Run:

```bash
python main.py
```

## Requirements

- Python 3.8+
- Ollama installed and running
- SearchAPI key

## Usage

```python
python main.py
What would you like to know? Who is Claude Shannon?
```
