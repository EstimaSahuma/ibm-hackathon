def prompt_message_presentation() -> str:
    return f"""
        'pt': "👋🏾 Olá! Eu sou o AgriBank Assist, seu assistente digital bancário rural.",
        'en': "👋🏾 Hello! I am AgriBank Assist, your rural banking digital assistant.",
        'kimbundu': "👋🏾 Ngevu! Mono ke AgriBank Assist, mudimu wakwetu na banku.",
        'umbundu': "👋🏾 Olá! Ohandi AgriBank Assist, okapayi koku banku lyoku camponês.",
        'kikongo': "👋🏾 Mbote! Mono ke AgriBank Assist, mosungi wa banku ya bilanga."
    """

def prompt_open_account(user_msg: str, idioma: str = 'pt') -> str:
    if idioma == 'en':
        return f"""The farmer says: "{user_msg}"

            Provide a simple explanation on how to open a bank account using a Farmer ID or National ID.
        """
    
    if idioma == 'kimbundu':
        return f"""Traduza a seguinte frase para Kimbundu e depois explique como abrir uma conta rural: "{user_msg}"

                    Exemplo:
                    Português: Para abrir uma conta, leve seu BI ou Cartão de Agricultor.
                    Kimbundu: K’u sole kufuta conta, kalukila BI wela kartão dia mufundi.
                """

    if idioma == 'umbundu':
        return f"""Traduza para Umbundu e explique como abrir uma conta com BI ou Cartão de Agricultor:
                    \"{user_msg}\"

                    Exemplo:
                    Português: Leve seu BI ou Cartão de Agricultor.
                    Umbundu: Feteka okuti BI wela ekartão lyocikola.
                """

    if idioma == 'kikongo':
        return f"""Explique em Kikongo como abrir uma conta bancária com BI ou cartão de agricultor: \"{user_msg}\"

                    Exemplo:
                    Português: Para abrir uma conta, traga seu documento.
                    Kikongo: Kana kufungula compte, lela na documentu yako.
                """

    return f"""O camponês diz: \"{user_msg}\"

                Explique como ele pode abrir uma conta bancária com BI ou Cartão de Agricultor. Use linguagem simples.
            """

def prompt_agri_credit(user_msg: str, idioma: str = 'pt') -> str:
    if idioma == 'en':
        return f"""The farmer says: \"{user_msg}\"

                    Explain how to apply for agricultural credit, including which documents are required.
                """
    
    if idioma == 'kimbundu':
        return f"""
                    Traduza a frase e explique em Kimbundu como pedir crédito agrícola com documentos mínimos: \"{user_msg}\"
                """

    if idioma == 'umbundu':
        return f"""
                    Explique em Umbundu como funciona o crédito agrícola e quais documentos são necessários: \"{user_msg}\"
                """

    if idioma == 'kikongo':
        return f"""Explique como o camponês pode conseguir crédito agrícola em Kikongo, com linguagem acessível: \"{user_msg}\""""

    return f"""O agricultor diz: \"{user_msg}\"

                Explique como funciona o processo de solicitação de crédito agrícola e quais documentos ele deve fornecer.
            """
    
def prompt_open_account_kimbundu(user_msg: str, lang: str = 'pt') -> str:
    return f"""
        O camponês diz em Kimbundu: "{user_msg}"

        Traduz essa frase para português simples, entenda o pedido e responda com instruções de como abrir uma conta bancária como agricultor, mesmo sem salário fixo.

        Responda no mesmo idioma, se possível. Aqui vai um exemplo de tradução para Kimbundu:

        Português: "Para abrir uma conta, envie seu BI ou Cartão de Agricultor"
        Kimbundu: "K'u sole kufuta conta, kalukila BI wela kartão dia mufundi."
    """
    
def prompt_financial_education(topico: str, idioma: str = 'pt') -> str:
    if idioma == 'en':
        return f"""Explain the concept \"{topico}\" in simple English, using rural/agriculture-related examples."""

    if idioma in ['kimbundu', 'umbundu', 'kikongo']:
        return f"""Explique o seguinte conceito em {idioma.upper()}, de forma simples e com exemplos agrícolas: \"{topico}\""""

    return f"""Explique para um camponês com pouca escolaridade o seguinte conceito: \"{topico}\". Use exemplos rurais e linguagem simples."""
