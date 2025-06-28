from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\EstimaSahuma\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def extract_text_image(caminho, idioma: str = 'pt'):
    texto = pytesseract.image_to_string(Image.open(caminho), lang='por')
    return texto