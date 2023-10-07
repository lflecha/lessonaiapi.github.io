import openai
from settings import settings


async def prompt_gpt(
    grade_level: str,
    subject: str,
    lesson_title: str,
    lesson_description: str
):
    openai.api_key = settings.OPENAPI_KEY
    prompt_text = f"""
    Create a {grade_level} lesson plan on "{lesson_title}":
    Subject: {subject}
    Description: {lesson_description}
    Topic: [Topic]
    Objectives & Outcomes:
    - [Objective .]
    Materials:
    - [Relevant materials.]
    Warm-up:
    - [Warm-up activity.]
    Direct Instruction:
    - [Instructions.]
    Guided Practice:
    - [Guided activity.]
    Independent Practice:
    - [Independent activity.]
    Closure:
    - [Lesson conclusion.]
    Assessment:
    - [Assessment method.]
    """
    # Get the response from GPT-3.5 using the curie engine
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        max_tokens=3800
    )
    return response.choices[0].text.strip()
