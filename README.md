# LLM Integration Demo

This project is a simple demo for integrating a local Large Language Model (LLM), such as **Gemma 3**, through an OpenAI-compatible API with **FastAPI**.

## 🚀 Features
- Provides a `/chat` endpoint that accepts a prompt and optional parameters (`temperature`, `max_tokens`).
- Returns a model-generated response along with token usage statistics.

## ⚙️ Setup
1. Clone the repository:
   ```bash
   git clone git@github.com:username/03-llm-integration.git
   cd 03-llm-integration
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Start a local LLM server (e.g. [Ollama](https://ollama.ai) or llama.cpp).
4. Create a `.env` file with connection details:
   ```
   OPENAI_API_KEY=dummy
   BASE_URL=http://localhost:11434/v1
   MODEL=gemma3:1b
   ```
5. Run the API:
   ```bash
   fastapi dev main.py
   ```

## 🔍 Usage
Access Swagger UI for testing:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Example request:
```json
{
  "prompt": "Explain closures in JavaScript",
  "temperature": 0.7,
  "max_tokens": 256
}
```
