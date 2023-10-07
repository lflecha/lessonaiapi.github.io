from pydantic_settings import BaseSettings
from pydantic import validator
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    OPENAPI_KEY: str = os.getenv("OPENAPI_KEY")
    ORIGINS: str = os.getenv("ORIGINS").split("*")
    
        


settings = Settings()