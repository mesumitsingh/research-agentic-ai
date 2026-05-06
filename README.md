# Agentic AI Research Assistant
*Your personal digital demon that actually does research instead of hallucinating bullshit at 3 AM.*

Tired of asking ChatGPT about "latest AI trends" and getting 2023 garbage wrapped in corporate cheerleading? This LangChain-powered savage doesn't just search it **hunts**, cross-references, and spits out structured reports like a cynical grad student who’s seen too much.

Built with OpenRouter (because free models lie), DuckDuckGo (Google can suck it), and Wikipedia (the last somewhat honest corner of the internet). Also saves your research notes so you don’t lose them like every other half-finished side project.

### Features (The Ones That Actually Work)
- **Structured output** or die trying: Always delivers `topic`, `summary`, `sources`, and `tools_used`. No half-assed Markdown soup.
- **Web search** that doesn’t track you (DuckDuckGo supremacy).
- **Wikipedia integration** for when you want facts instead of vibes.
- **Auto-save** to `research_output.txt` — because your brain is a sieve and future-you will thank present-you (or curse them, whatever).
- Runs locally or in Docker, because Docker makes you feel like a real engineer.

### Project Structure (Behold the Glory)
- `main.py` — Where the cursed LangChain agent is summoned
- `tools.py` — The weapons (search, wiki, and the sacred note saver)
- `requirements.txt` — Dependencies that will definitely break in six months
- `docker-compose.yml` + `Dockerfile` — For when you want to feel production-ready while crying inside
- `run.bat` — Windows users, I got you (you’re welcome)

### Requirements
- Python 3.11+
- OpenRouter API key (yes, you actually need money)
- Optional: Docker Desktop (highly recommended if you value your sanity)

### Installation (Local — For Masochists)

```bash
python -m venv venv
source venv/bin/activate    # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

export OPENROUTER_API_KEY="sk-or-..."   # Windows: set OPENROUTER_API_KEY=sk-or-...
```

Now witness true power:

```bash
python main.py
```

Type your query and watch it cook.

### Docker Setup (For People With Standards)

```bash
docker compose up --build -d
docker exec agentic-ai-container python main.py
```

Or just run `run.bat` like a civilized Windows user.

### How It Works (The Dark Magic)

The agent is given a strict Pydantic schema and a prompt that basically says: *"Don’t hallucinate, idiot. Use tools. Cite sources. Be useful for once."*

It will search, read Wikipedia, think, and then deliver a proper research report instead of the usual AI slop. If you mention saving, it appends everything to `research_output.txt` with a timestamp (so you can track how your obsessions evolve).

### Usage Example

Try this masterpiece of a query:
> "Research the latest trends in AI agent development and roast the current hype"

You’ll get a proper report. Not blogspam. Not marketing fluff. Actual signal.

### Output Format

```json
{
  "topic": "AI Agent Development in 2026",
  "summary": "Everyone’s building agents. Most are over-engineered todo list apps with extra steps...",
  "sources": ["https://...", "Wikipedia: Artificial Intelligence"],
  "tools_used": ["search", "wikipedia", "save_text_to_file"]
}
```

### Contributing

Found a bug? Open an issue.  
Have a better idea? PR it.  
Just here to complain? Make it funny at least.

### License

Open source. Do whatever. I’m not your dad.

---

**Now stop reading READMEs and go build something terrifying.**
