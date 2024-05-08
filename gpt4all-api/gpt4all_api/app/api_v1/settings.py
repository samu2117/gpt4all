from pydantic import BaseSettings
from pathlib import Path
DEFAULT_MODEL_DIRECTORY = f"{Path(__file__).resolve().parent.parent.parent}/models"

class Settings(BaseSettings):
    app_environment = 'dev'
    model: str = 'mistral-7b-openorca.gguf2.Q4_0.gguf'
    gpt4all_path: str = DEFAULT_MODEL_DIRECTORY
    inference_mode: str = "cpu"
    hf_inference_server_host: str = "http://gpt4all_gpu:80/generate"
    sentry_dns: str = None

    temp2 = 0.18
    top_p = 1.0
    top_k = 50
    repeat_penalty = 1.18



settings = Settings()
