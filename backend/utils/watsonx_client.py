import os
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai import Credentials, APIClient
from dotenv import load_dotenv

load_dotenv()

headers = {
    'Authorization': f"Bearer { os.getenv('IBM_REGION') }",
    'User-Agent': 'ibm-watsonx-ai/1.0.1 (lang=python; arch=x86_64; os=darwin; python.version=3.10.13)',
    'Content-Type': 'application/json'
}

credentials = Credentials(
    api_key =os.getenv("IBM_API_KEY"),
    url=os.getenv('IBM_URL')
)

model = ModelInference(
    model_id=os.getenv("MODEL_ID"),
    credentials=credentials,
    project_id=os.getenv("IBM_PROJECT_ID")
)

def get_granite_response(prompt: str) -> str:
    resp = model.chat(
        messages=[{"role":"system", "content":"Você é um assistente bancário que ajuda camponeses a abrir contas e pedir crédito."},
                  {"role":"user", "content": prompt}],
        params={
            "temperature": 0.7,
            "top_k": 50,
            "top_p": 0.85,
            "repetition_penalty": 1.05,
            "max_tokens": 200
        }
    )
    return resp['choices'][0]['message']['content']
