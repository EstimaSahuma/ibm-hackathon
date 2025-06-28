from fastapi import FastAPI, Form, UploadFile, File
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

@app.post("/presentation/")
def presentation():
    return {"response": prompt_message_presentation()}

@app.post("/open-account/")
def open_account(msg: str = Form(...), lang: str = Form('pt')):
    prompt = prompt_open_account(msg, lang)
    resposta = get_granite_response(prompt)
    return {"response": resposta}

@app.post("/agri-credit/")
def agri_credit(msg: str = Form(...), lang: str = Form('pt')):
    prompt = prompt_agri_credit(msg, lang)
    resposta = get_granite_response(prompt)
    return {"response": resposta}

@app.post("/process-simulation/")
def process_simulation(msg: str = Form(...), lang: str = Form('pt')):
    prompt = prompt_agri_credit(msg, lang)
    resposta = get_granite_response(prompt)
    solicitacao_doc = "envie seu BI" in resposta.lower() or "documento" in resposta.lower()
    return {
        "resposta_granite": resposta,
        "documento_requisitado": solicitacao_doc,
        "acao_sugerida": "Notificar cliente para envio do BI." if solicitacao_doc else "Aguardar mais dados."
    }

@app.post("/financial-education/")
def financial_education(topico: str = Form(...), lang: str = Form('pt')):
    prompt = prompt_financial_education(topico, lang)
    resposta = get_granite_response(prompt)
    return {"response": resposta}

@app.post("/upload-documento/")
def upload_documento(file: UploadFile = File(...), lang: str = Form('pt')):
    conteudo = file.file.read()
    path = Path(f"temp/{file.filename}")
    with open(path, "wb") as f:
        f.write(conteudo)
    
    texto = extract_text_image(path, lang)
    return {"texto_extraido": texto}
