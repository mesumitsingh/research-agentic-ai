# Agentic AI Research Assistant

A LangChain-based research assistant that leverages OpenRouter, DuckDuckGo search, and Wikipedia to generate structured research reports. It can also save research notes to a text file for later reference.

## Features

- **Structured Research Output**: Produces reports with `topic`, `summary`, `sources`, and `tools_used`.
- **Web Search**: Integrates DuckDuckGo for current information retrieval.
- **Wikipedia Integration**: Fetches reference material from Wikipedia.
- **Note Saving**: Appends research notes to `research_output.txt`.
- **Flexible Execution**: Supports local Python execution or Docker-based containerization.

## Project Structure

- `main.py`: Configures the LangChain agent, prompt, response schema, and execution.
- `tools.py`: Defines tools for searching, Wikipedia queries, and file saving.
- `requirements.txt`: Lists Python dependencies.
- `docker-compose.yml`: Docker Compose configuration for container setup.
- `Dockerfile`: Docker image build instructions.
- `run.bat`: Convenience script for running the app inside the Docker container (Windows).

## Requirements

- Python 3.11 or newer
- An OpenRouter API key (set as environment variable)
- Optional: Docker Desktop for containerized execution

## Installation and Setup

### Local Setup

1. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set your OpenRouter API key**:

   ```bash
   export OPENROUTER_API_KEY="your_api_key_here"  # On Windows: set OPENROUTER_API_KEY=your_api_key_here
   ```

4. **Run the application**:

   ```bash
   python main.py
   ```

   Enter your research query when prompted.

### Docker Setup

1. **Build and start the container**:

   ```bash
   docker compose up --build -d
   ```

2. **Run the script inside the container**:

   ```bash
   docker exec agentic-ai-container python main.py
   ```

   Alternatively, on Windows, use `run.bat` after the container is running.

## How It Works

The agent uses a Pydantic response schema to ensure structured output. It employs tools for web search and Wikipedia lookups when additional context is required. If the user requests to save data, it uses the save tool to append notes to `research_output.txt`.

The prompt instructs the agent to provide accurate facts, detailed explanations, trends, comparisons, and caveats, while always filling all schema fields.

## Usage

Run the app and enter a research query. The output will be a JSON object with the structured research report. If saving is requested, the results are appended to `research_output.txt`.

Example query: "Research the latest trends in AI agent development."

## Output

The structured response includes:
- `topic`: The research topic.
- `summary`: A detailed report with facts, trends, context, comparisons, and caveats.
- `sources`: List of sources used (websites, Wikipedia pages, etc.).
- `tools_used`: List of exact tool names used (e.g., "search", "wikipedia", "save_text_to_file").

If the save tool is invoked, the output is also saved to `research_output.txt` in the project root, prefixed with a timestamp.

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is open-source. Please check for any specific license in the repository.