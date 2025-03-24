from fastapi import FastAPI
from pydantic import BaseModel
from agents import create_crew
import asyncio

app = FastAPI()

class InquiryRequest(BaseModel):
    customer: str
    person: str
    inquiry: str

@app.post("/answer")
async def answer_question(data: InquiryRequest):
    crew = create_crew(data.customer, data.person, data.inquiry)
    result = await asyncio.to_thread(crew.kickoff)
    return {"response": result}
