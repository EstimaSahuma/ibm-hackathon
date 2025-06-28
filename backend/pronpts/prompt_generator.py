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
        return f"""Mwana nyi okamba: "{user_msg}"

                    Olongi okuti o muntu alonge ombanka oco ku BI o Cartão de Agricultor
                """

    if idioma == 'umbundu':
        return f"""Olongi ulomboloka:
                    \"{user_msg}\"

                    Ohandi etavo okuti okuti ove okutilongela ombanka vali ku BI o Cartão de Agricultor.
                """

    if idioma == 'kikongo':
        return f"""Mbongi widi: \"{user_msg}\"

                    Ndinga ya kukebuka konta ya banki na BI to Kartãu ya Bantu ya bilanga.
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
                    Mwana nyi okamba: \"{user_msg}\"
                    
                    Zimba muntu otinxi dodolo dia kudihola kredi ya kulima, karinyina mona, makalata no kasuwa kesomba
                """

    if idioma == 'umbundu':
        return f"""
                    Olongi ulomboloka: \"{user_msg}\"
                    
                    Omunhu omaza okula okuposa kredi ya wingi wa kupangalapangwa, kwenda konta, epasa yange ya epasha, na silaka.
                """

    if idioma == 'kikongo':
        return f"""
                Mbongi widi: \"{user_msg}\"
                
                Moto yina ke ka diela kredi ya banzadi ya nzenza, mefuna ID, luzingu, mipanda ne biloko biye baleta.
            """

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

    if idioma == 'kimbundu':
        return f"""
                    Tulangulula kwa mukongo owa mesu kakululuka, diambu yai: \"{topico}\". Usemikíalo ya mbéni ye lukangulu lwak’úkati.
                """

    if idioma == 'umbundu':
        return f"""
                    Eyangela okuvangula vali onanjila yokutunga vesu, omanu aya: \"{topico}\". Tëngë misa ómolo ókumwe ye lukalivano lwalíya.
                """

    if idioma == 'kikongo':
        return f"""
                    Lambula na mosi ya buala, yina kele na mayele muke, nsangu yai: \"{topico}\". Sambila misá ya ntoto ye luvumbu luvula.
                """

    return f"""Explique para um camponês com pouca escolaridade o seguinte conceito: \"{topico}\". Use exemplos rurais e linguagem simples."""
