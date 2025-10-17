# process_images.py
from PIL import Image, ImageOps
import json
import os

INPUT_DIR = "photos/original"
OUT_DIR = "static/photos"           # fotos finais direto na pasta static
THUMB_DIR = "static/photos/thumbs"  # thumbs direto na pasta static
MAX_DIM = 2400        # max largura/altura para fotos finais
THUMB_SIZE = (400, 400)
BORDER = 40           # px
BORDER_COLOR = (245, 242, 238)  # cor da moldura (tupla RGB)

os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

def process_image(in_path):
    # Converte o nome do arquivo para minúsculas e muda a extensão para .webp
    base_name = os.path.splitext(os.path.basename(in_path).lower())[0]
    out_path = os.path.join(OUT_DIR, f"{base_name}.webp")
    thumb_path = os.path.join(THUMB_DIR, f"{base_name}.webp")

    with Image.open(in_path) as im:
        # Garante que a imagem está em modo RGB antes de processar
        im = im.convert("RGB")

        # redimensiona se maior que MAX_DIM
        w, h = im.size
        if max(w, h) > MAX_DIM:
            scale = MAX_DIM / max(w, h)
            im = im.resize((int(w*scale), int(h*scale)), Image.LANCZOS)

        # Adiciona borda e salva a foto final em WebP
        framed = ImageOps.expand(im, border=BORDER, fill=BORDER_COLOR)
        final_w, final_h = framed.size
        framed.save(out_path, 'webp', quality=90)

        # criar thumbnail
        thumb = im.copy()
        thumb.thumbnail(THUMB_SIZE, Image.LANCZOS)
        # Adiciona uma borda menor para o thumbnail
        thumb_border = 10
        thumb = ImageOps.expand(thumb, border=thumb_border, fill=BORDER_COLOR)
        thumb.save(thumb_path, 'webp', quality=80)

        # Retorna os dados da imagem para o JSON
        return {
            "src": os.path.basename(out_path),
            "thumb": os.path.basename(thumb_path),
            "w": final_w,
            "h": final_h
        }

if __name__ == "__main__":
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.jpg','.jpeg','.png'))]
    files.sort()
    
    image_data = []
    for f in files:
        in_path = os.path.join(INPUT_DIR, f)
        print("Processando:", f)
        data = process_image(in_path)
        image_data.append(data)

    # Salva os metadados em um arquivo JSON
    with open(os.path.join(OUT_DIR, 'photos.json'), 'w') as f:
        json.dump(image_data, f, indent=2)

    print("\nPronto! Fotos processadas e 'photos.json' criado.")
