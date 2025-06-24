# main.py (FastAPI Backend)

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

# Import the assessment_data from the new file
from questions_data import assessment_data as questions_data

app = FastAPI()

# Allow CORS for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Pydantic Models ---
class Answer(BaseModel):
    question_id: str
    value: int

class AssessmentSubmission(BaseModel):
    answers: list[Answer]
    email: str

# --- API Endpoints ---

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse("static/index.html")

@app.get("/api/assessment-data")
async def get_assessment_data():
    """Returns all questions, categories, and maturity levels."""
    return questions_data

@app.post("/api/submit-assessment")
async def submit_assessment(submission: AssessmentSubmission):
    """Calculates maturity score and returns report data."""
    total_score = 0
    answered_questions_count = 0
    
    # Initialize category scores
    category_scores = {category['name']: 0 for category in questions_data['categories'] if category['id'] != 0}
    category_question_counts = {category['name']: 0 for category in questions_data['categories'] if category['id'] != 0}

    for answer in submission.answers:
        question_key = answer.question_id
        if question_key in questions_data["questions"]:
            total_score += answer.value
            answered_questions_count += 1
            
            # Update category scores
            for category in questions_data['categories']:
                if category['id'] != 0 and category['question_range'] and \
                   int(question_key.replace('q', '')) >= category['question_range'][0] and \
                   int(question_key.replace('q', '')) <= category['question_range'][1]:
                    category_scores[category['name']] += answer.value
                    category_question_counts[category['name']] += 1
                    break

    if answered_questions_count == 0:
        raise HTTPException(status_code=400, detail="No questions answered.")

    average_score = total_score / answered_questions_count
    maturity_level_int = round(average_score)

    # Calculate average for each category
    final_category_scores = {}
    for category_name, score_sum in category_scores.items():
        count = category_question_counts[category_name]
        final_category_scores[category_name] = round(score_sum / count, 2) if count > 0 else 0

    level_info = questions_data["maturity_levels"].get(maturity_level_int, questions_data["maturity_levels"][1]) # Default to level 1 if something goes wrong

    report_data = {
        "overall_maturity_level": maturity_level_int,
        "maturity_title": level_info["title"],
        "maturity_description": level_info["description"],
        "total_score": total_score,
        "average_score": round(average_score, 2),
        "category_scores": final_category_scores,
        "email": submission.email
    }

    # In a real application, you would save this report data to a database
    # and/or send the detailed report via email here.
    print(f"Generated report for {submission.email}: {report_data}")

    return {"message": "Report generated successfully", "report_data": report_data}