from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from schemas import PromptBase, PrompRes
from prompt import prompt_gpt
from settings import settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/prompt", status_code=status.HTTP_200_OK, response_model=PrompRes)
async def create_prompt(
    prompt_in: PromptBase
):
    response = await prompt_gpt(grade_level=prompt_in.grade_level, 
                                subject=prompt_in.subject,
                                lesson_title=prompt_in.lesson_title, 
                                lesson_description=prompt_in.lesson_description)
    
    return PrompRes(plan=response)
    ...