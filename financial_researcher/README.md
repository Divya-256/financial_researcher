# 🤖 AI Financial Researcher

A multi-agent AI system using CrewAI that generates comprehensive research reports on any company using real-time web search.

## Features

- **Multi-Agent System**: Researcher and Analyst agents working together
- **Real-time Data**: Uses Serper API for current web search results
- **Web Interface**: Gradio-based UI for easy interaction
- **Comprehensive Reports**: Detailed analysis with executive summary, challenges, opportunities, and future outlook

## Setup

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Set up environment variables** in `.env`:
   ```
   GROQ_API_KEY=your_groq_api_key
   SERPER_API_KEY=your_serper_api_key
   ```

## Usage

### Command Line
```bash
crewai run
```

### Web Interface
```bash
python app.py
```

## Tech Stack

- **CrewAI**: Multi-agent orchestration
- **Groq**: LLM provider (Llama 3.1 8B)
- **Serper**: Web search API
- **Gradio**: Web interface
- **Python**: Core language