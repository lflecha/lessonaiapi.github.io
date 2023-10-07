from pydantic import BaseModel

class PromptBase(BaseModel):
    grade_level: str
    subject: str
    lesson_title: str
    lesson_description: str
    
class PrompRes(BaseModel):
    plan: str
    