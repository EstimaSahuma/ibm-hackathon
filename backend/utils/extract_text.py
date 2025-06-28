from PIL import Image
import pytesseract

def extract_text_image(caminho, idioma: str = 'pt'):
    texto = pytesseract.image_to_string(Image.open(caminho), lang=idioma)
    return texto