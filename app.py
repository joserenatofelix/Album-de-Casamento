import os
import json
from flask import Flask, render_template
from datetime import datetime
import threading
import socket

app = Flask(__name__)

# Configurações
app.config['PHOTO_DIR'] = 'static/photos'
app.config['THUMB_DIR'] = 'static/photos/thumbs'
app.config['PHOTO_DATA_FILE'] = 'static/photos/photos.json'
app.config['VISITOR_COUNT_FILE'] = 'visitor_count.txt'

# --- Contador de Visitantes Persistente e Thread-Safe ---
_visitor_lock = threading.Lock()

def get_visitor_count():
    """Lê o número de visitantes de um arquivo."""
    try:
        with open(app.config['VISITOR_COUNT_FILE'], 'r') as f:
            return int(f.read())
    except (IOError, ValueError):
        return 0

def increment_visitor_count():
    """Incrementa e salva o número de visitantes."""
    with _visitor_lock:
        count = 0
        try:
            with open(app.config['VISITOR_COUNT_FILE'], 'r') as f:
                count = int(f.read())
        except (IOError, ValueError):
            pass # Se o arquivo não existir ou estiver vazio, count continua 0
        count += 1
        with open(app.config['VISITOR_COUNT_FILE'], 'w') as f:
            f.write(str(count))
        return count

def get_photos():
    """Lê os dados das fotos do arquivo JSON."""
    json_path = app.config['PHOTO_DATA_FILE']
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        return []

@app.context_processor
def inject_now():
    """Injeta a data atual em todos os templates"""
    return {'now': datetime.utcnow()}

@app.route("/")
def album():
    visitor_count = increment_visitor_count()
    photos = get_photos()
    return render_template("album.html", photos=photos, visitor_count=visitor_count)

if __name__ == "__main__":
    # Detect whether the system supports IPv6. If so, bind to '::' so
    # that connections to localhost resolving to ::1 will work.
    try:
        has_ipv6 = socket.has_ipv6
    except Exception:
        has_ipv6 = False

    if has_ipv6:
        bind_host = '::'
    else:
        bind_host = '0.0.0.0'

    print(f"Starting Flask on host={bind_host} port=5000\n")
    print("Open these URLs in your browser:")
    print("  http://127.0.0.1:5000/")
    print("  http://localhost:5000/  (if your system resolves localhost to 127.0.0.1 or ::1)")

    app.run(debug=True, host=bind_host, port=5000)