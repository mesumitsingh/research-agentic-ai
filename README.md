# Agentic AI Research Assistant

A small LangChain-based research assistant that uses OpenRouter, DuckDuckGo search, and Wikipedia to produce structured research reports. The app can also append research notes to a text file for later review.

## Features

- Structured research output with `topic`, `summary`, `sources`, and `tools_used`
- Web search through DuckDuckGo
- Wikipedia lookup for reference material
- Save research notes to `research_output.txt`
- Local Python execution or Docker-based execution

## Project Files

- `main.py` - configures the model, prompt, response schema, and agent execution
- `tools.py` - defines the search, Wikipedia, and file-saving tools
- `requirements.txt` - Python dependencies
- `docker-compose.yml` - container setup for running the app in Docker
- `run.bat` - convenience command for running `main.py` inside the container

## Requirements

- Python 3.11 or newer
- An OpenRouter API key
- Optional: Docker Desktop if you want to run the app in a container

## Local Setup

1. Create and activate a virtual environment.

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies.

   ```powershell
   pip install -r requirements.txt
   ```

3. Set your OpenRouter API key.

   ```powershell
   $env:OPENROUTER_API_KEY="your_api_key_here"
   ```

4. Run the app.

   ```powershell
   python main.py
   ```

## Docker Setup

1. Build and start the container.

   ```powershell
   docker compose up --build -d
   ```

2. Run the script inside the container.

   ```powershell
   docker exec agentic-ai-container python main.py
   ```

   On Windows, you can also use `run.bat` after the container is running.

## How It Works

The agent is configured with a Pydantic response schema so the final output is structured. It uses search tools when extra context is needed, and it can call the save tool when the prompt asks to write results to a file.

By default, `main.py` uses a sample research query. If you want interactive input, uncomment the `input(...)` line in `main.py` and remove or replace the sample query.

## Output

If the save tool is used, the result is appended to `research_output.txt` in the project root.
