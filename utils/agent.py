from utils.scraper import scrape_table
from utils.analyzer import analyze_data
from utils.visualizer import make_plot

async def process_question(question: str) -> dict:
    # You may be calling some LLM here like OpenAI, or parsing the question.
    print("Received question:", question)  # Debug print

    # Dummy response (replace with actual LLM logic or data scraping logic)
    return {"message": f"Question processed: {question}"}


