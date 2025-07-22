import pandas as pd
import io
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from utils.agent import process_question

app = FastAPI()

@app.post("/api/")
async def analyze_file(file: UploadFile = File(...)):
    # Read the uploaded file
    content = await file.read()

    # Try to decode the content as UTF-8 first, fallback to UTF-16 if needed
    try:
        question = content.decode("utf-8").strip()
    except UnicodeDecodeError:
        question = content.decode("utf-16").strip()

    # Pass the question string to your custom agent
    response = await process_question(question)

    return JSONResponse(content={"result": response})
