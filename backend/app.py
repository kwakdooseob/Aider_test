from flask import Flask, request, jsonify
import os
from file_parser import parse_docx, parse_pdf, parse_pptx

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        
        file_type = get_file_type(file_path)
        if not file_type:
            return jsonify({'error': 'Unsupported file type'}), 400
        
        text = None
        if file_type == 'docx':
            text = parse_docx(file_path)
        elif file_type == 'pdf':
            text = parse_pdf(file_path)
        elif file_type == 'pptx':
            text = parse_pptx(file_path)
        
        if not text:
            return jsonify({'error': 'Failed to parse file'}), 500
        
        return jsonify({'text': text}), 200

def get_file_type(file_path):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext == '.docx':
        return 'docx'
    elif ext == '.pdf':
        return 'pdf'
    elif ext == '.pptx':
        return 'pptx'
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
