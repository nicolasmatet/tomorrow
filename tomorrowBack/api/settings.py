from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    endpoint_url:str = os.environ.get('endpoint_url')