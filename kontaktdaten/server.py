from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__, static_folder='resources')  # statische Dateien werden weiterhin aus dem 'resources'-Ordner geladen
DATA_FILE = './resources/kontakte.json'

# Kontakte laden
def lade_kontakte():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

# Kontakte speichern
def speichere_kontakte(kontakte):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(kontakte, f, ensure_ascii=False, indent=4)

# Route: Kontakte abrufen
@app.route('/kontakte', methods=['GET'])
def get_kontakte():
    kontakte = lade_kontakte()
    return jsonify(kontakte)

# Route: Kontakt hinzufügen
@app.route('/kontakte', methods=['POST'])
def add_kontakt():
    kontakt = request.json
    kontakte = lade_kontakte()
    kontakte.append(kontakt)
    speichere_kontakte(kontakte)
    return jsonify({'message': 'Kontakt hinzugefügt!', 'kontakt': kontakt}), 201

# Route: Homepage mit der Kontaktliste anzeigen
@app.route('/')
def index():
    return render_template('index.html')  # rendert die index.html im 'templates'-Ordner

# Route: Statische Datei (z.B. JSON) senden
@app.route('/resources/<path:filename>')
def serve_static(filename):
    return send_from_directory('resources', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
