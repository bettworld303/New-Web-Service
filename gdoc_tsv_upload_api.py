from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

DATA_FILE = 'gdoc_tsv_upload_parsed.json'

@app.route('/gdoc_tsv_upload_parsed', methods=['GET'])
def get_parsed_data():
    if not os.path.exists(DATA_FILE):
        return jsonify({'error': f'{DATA_FILE} not found'}), 404
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def index():
    return 'Gdoc TSV Upload API is running.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)