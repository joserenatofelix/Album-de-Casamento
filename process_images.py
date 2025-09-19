# process_images.py
from PIL import Image, ImageOps
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

def process_image(in_path, out_path, thumb_path):
    with Image.open(in_path) as im:
        im = im.convert("RGBA")
        # redimensiona se maior que MAX_DIM
        w, h = im.size
        if max(w, h) > MAX_DIM:
            scale = MAX_DIM / max(w, h)
            im = im.resize((int(w*scale), int(h*scale)), Image.LANCZOS)

        # cria borda usando ImageOps.expand
        framed = ImageOps.expand(im, border=BORDER, fill=BORDER_COLOR)

        # salvar foto final
        framed = framed.convert("RGB")
        framed.save(out_path, quality=95)

        # criar thumbnail
        thumb = im.copy()
        thumb.thumbnail(THUMB_SIZE, Image.LANCZOS)
        thumb = thumb.convert("RGB")
        thumb = ImageOps.expand(thumb, border=10, fill=BORDER_COLOR)
        thumb.save(thumb_path, quality=85)

if __name__ == "__main__":
    files = [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(('.jpg','.jpeg','.png'))]
    files.sort()
    for f in files:
        in_p = os.path.join(INPUT_DIR, f)
        out_p = os.path.join(OUT_DIR, f)
        thumb_p = os.path.join(THUMB_DIR, f)
        print("Processando:", f)
        process_image(in_p, out_p, thumb_p)
    print("Pronto. Fotos processadas em", OUT_DIR, "e thumbs em", THUMB_DIR)
