import cv2
import pytesseract

imagem = cv2.imread('Fotografia - Comprovante de Entrega - Mobile - mobile.jpg')

pytesseract.pytesseract.tesseract_cmd= r'C:\Users\vitorgomes\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(imagem,lang="por")

print(text)