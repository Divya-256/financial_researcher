import gradio as gr
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fix sys.path for financial researcher package
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FINANCIAL_RESEARCHER_SRC = os.path.join(BASE_DIR, "financial_researcher", "src")
if FINANCIAL_RESEARCHER_SRC not in sys.path:
    sys.path.insert(0, FINANCIAL_RESEARCHER_SRC)

from financial_researcher.crew import ResearchCrew
def run_research(company):
    if not company.strip():
        return "Please enter a company name."
    
    try:
        inputs = {"company": company}
        result = ResearchCrew().crew().kickoff(inputs=inputs)
        return result.raw
    except Exception as e:
        return f"Error: {str(e)}"

# Create interface
with gr.Blocks(title="AI Financial Researcher") as demo:
    gr.Markdown("""
    # 🤖 AI Financial Researcher
    
    **Multi-agent AI system using CrewAI that generates comprehensive research reports on any company.**
    
    Enter a company name and watch AI agents generate a detailed research report!
    """)
    
    company_input = gr.Textbox(
        label="Company Name",
        placeholder="Enter the name of the company you want to research...",
        value="Apple Inc.",
        lines=2
    )
    
    submit_btn = gr.Button("🎯 Start Research", variant="primary")
    
    output = gr.Textbox(
        label="Research Results",
        lines=12,
        placeholder="Research results will appear here..."
    )
    
    submit_btn.click(
        fn=run_research,
        inputs=company_input,
        outputs=output
    )
    
    gr.Examples(
        examples=[
            ["Tesla, Inc."],
            ["Amazon.com, Inc."],
            ["Microsoft Corporation"],
            ["Meta Platforms, Inc."]
        ],
        inputs=company_input,
        outputs=output,
        fn=run_research
    )
    
    gr.Markdown("""
    ---
    ### 🔧 Tech Stack: Python • CrewAI • Gradio • LLMs • Multi-Agent Systems
    
    [View Source Code](https://github.com/Divya-256/financial_researcher)
    """)

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Soft())
