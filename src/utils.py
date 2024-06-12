from dataclasses import dataclass, field
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class AppConfig:
    access_token: str = field(init=False)
    llm_model_name: str = field(init=False)
    llm_model_tag: str = field(init=False)
    target_repo: str = field(init=False)

    def __post_init__(self):
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.llm_model_name = os.getenv("LLM_MODEL_NAME")
        self.llm_model_tag = os.getenv("LLM_MODEL_TAG")
        self.llm_model_name_and_tag = self.llm_model_name+':'+self.llm_model_tag
        self.target_repo = os.getenv("REPO_NAME")

def env_config(func):
    def wrapper(*args,**kwargs):
        kwargs['config'] = AppConfig()
        return func(*args, **kwargs)
    return wrapper
