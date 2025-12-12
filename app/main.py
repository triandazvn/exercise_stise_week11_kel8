from pathlib import Path
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load config
REPLACE_MAP = {}
REPLACE_PATH = Path(__file__).resolve().parent / "replaced_chars.txt"

if REPLACE_PATH.exists():
    content = REPLACE_PATH.read_text(encoding="utf-8")
    lines = content.splitlines()
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            REPLACE_MAP[key.strip()] = value.strip()

# --- Fungsi Logika dipisah agar bisa di-test di test_unit.py ---
def replace_text(text, char_map):
    result_text = ""
    for char in text:
        lower_char = char.lower()
        if lower_char in char_map:
            result_text += char_map[lower_char]
        else:
            result_text += char
    return result_text

@app.post("/replace") 
def replace_endpoint():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")
    
    # Panggil fungsi logika
    clean_text = replace_text(text, REPLACE_MAP)
            
    return jsonify({"result": clean_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)