import pytesseract
from PIL import Image

def process_image(image_path):
    # OCR processing to identify cryptocurrency name
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    
    # Simple pattern matching (customize based on common chart formats)
    crypto_names = ['BTC', 'ETH', 'BNB', 'XRP', 'ADA', 'SOL', 'DOT']
    for name in crypto_names:
        if name in text:
            return name
    return 'UNKNOWN_CRYPTO'