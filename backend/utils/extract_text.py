from PIL import Image
import pytesseract

def extract_text_image(caminho):
    texto = pytesseract.image_to_string(Image.open(caminho), lang='por')
    return texto