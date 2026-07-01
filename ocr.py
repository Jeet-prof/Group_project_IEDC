import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image_path):

    results = reader.readtext(image_path)

    text=""

    for r in results:
        text += r[1]+"\n"

    return text