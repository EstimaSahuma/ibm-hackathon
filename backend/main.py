from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.watsonx_client import get_granite_response
from utils.extract_text import extract_text_image
from pronpts.prompt_generator import ( 
                                      prompt_open_account, 
                                      prompt_agri_credit,
                                       prompt_message_presentation,
                                       prompt_financial_education,
                                      )
from pathlib import Path

app = FastAPI()

# CORS configuration (adjust as needed for deployment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/presentation/")
def presentation():
    return {"response": prompt_message_presentation()}

@app.post("/open-account/")
def open_account(msg: str = Form(...), lang: str = Form(...)):
    prompt = prompt_open_account(msg, lang)
    resposta = get_granite_response(prompt)
    return {"response": resposta}

@app.post("/agri-credit/")
def agri_credit(msg: str = Form(...), lang: str = Form(...)):
    prompt = prompt_agri_credit(msg, lang)
    resposta = get_granite_response(prompt)
    return {"response": resposta}

@app.post("/process-simulation/")
def process_simulation(msg: str = Form(...), lang: str = Form(...)):
    prompt = prompt_agri_credit(msg, lang)
    resposta = get_granite_response(prompt)
    solicitacao_doc = "envie seu BI" in resposta.lower() or "documento" in resposta.lower()
    return {
        "resposta_granite": resposta,
        "documento_requisitado": solicitacao_doc,
        "acao_sugerida": "Notificar cliente para envio do BI." if solicitacao_doc else "Aguardar mais dados."
    }

@app.post("/financial-education/")
def financial_education(msg: str = Form(...), lang: str = Form(...)):
    print(msg)
    print(lang)
    prompt = prompt_financial_education(msg, lang)
    resposta = get_granite_response(prompt)
    return {"response": resposta}

@app.post("/upload-documento/")
def upload_documento(file: UploadFile = File(...), lang: str = Form(...)):
    conteudo = file.file.read()

    # Garante que a pasta 'temp/' existe
    Path("temp").mkdir(parents=True, exist_ok=True)

    path = Path(f"temp/{file.filename}")
    with open(path, "wb") as f:
        f.write(conteudo)
    
    texto = extract_text_image(path, lang)
    return {"texto_extraido": texto}
