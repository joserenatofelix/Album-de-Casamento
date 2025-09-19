import os
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Configurações
app.config['PHOTO_DIR'] = 'static/photos'
app.config['THUMB_DIR'] = 'static/photos/thumbs'

def get_photos():
    """Retorna lista de fotos processadas"""
    if not os.path.exists(app.config['PHOTO_DIR']):
        return []
    
    photos = [f for f in os.listdir(app.config['PHOTO_DIR']) 
              if f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.startswith('.')]
    return sorted(photos)

@app.context_processor
def inject_now():
    """Injeta a data atual em todos os templates"""
    return {'now': datetime.now()}

visitor_count = 0

@app.route("/")
def album():
    global visitor_count
    visitor_count += 1
    photos = get_photos()
    return render_template("album.html", photos=photos, visitor_count=visitor_count)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)