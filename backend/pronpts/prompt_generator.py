def prompt_message_presentation() -> str:
    return f"""
        👋🏾 Olá! Eu sou o *AgriBank Assist*, seu assistente digital para apoio bancário rural. Posso ajudar com:

        ✅ Abrir conta com BI ou Cartão de Agricultor  
        ✅ Pedir crédito agrícola para suas plantações  
        ✅ Explicar taxas, serviços e documentos  

        Pode escrever em português simples ou nas línguas locais (Kimbundu, Umbundu...). Vamos começar?
    """

def prompt_open_account(user_msg: str) -> str:
    return f"""O camponês diz: "{user_msg}"

            Explique como ele pode abrir uma conta bancária com BI ou Cartão de Agricultor. Use linguagem simples.
        """

def prompt_agri_credit(user_msg: str) -> str:
    return f"""O agricultor diz: "{user_msg}"

        Explique como funciona o processo de solicitação de crédito agrícola e quais dados ele deve fornecer.
    """
    
def prompt_open_account_kimbundu(user_msg: str) -> str:
    return f"""
        O camponês diz em Kimbundu: "{user_msg}"

        Traduz essa frase para português simples, entenda o pedido e responda com instruções de como abrir uma conta bancária como agricultor, mesmo sem salário fixo.

        Responda no mesmo idioma, se possível. Aqui vai um exemplo de tradução para Kimbundu:

        Português: "Para abrir uma conta, envie seu BI ou Cartão de Agricultor"
        Kimbundu: "K'u sole kufuta conta, kalukila BI wela kartão dia mufundi."
    """
    
def prompt_financial_education(topico: str) -> str:
    return f"""
        Explique de forma clara e acessível para um camponês com pouca literacia financeira o que significa: "{topico}".

        Use exemplos da vida rural (plantio, colheita, venda no mercado) e linguagem simples.
    """

def prompt_translation_kimbundu(frase: str) -> str:
    return f"""
        Traduza esta frase para Kimbundu: "{frase}"

        Se possível, mantenha a estrutura original da frase.
    """