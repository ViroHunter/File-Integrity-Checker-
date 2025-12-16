from flask import Flask, render_template, request
import hashlib
import os

app = Flask(__name__)

HASH_STORAGE_FILE = 'file_hashes.txt'

def calculate_file_hash(file):
    sha256_hash = hashlib.sha256()
    for byte_block in iter(lambda: file.read(4096), b""):
        sha256_hash.update(byte_block)
    file.seek(0)
    return sha256_hash.hexdigest()

def store_hash(filename, file_hash):
    with open(HASH_STORAGE_FILE, 'a') as f:
        f.write(f"{filename}:{file_hash}\n")

def get_stored_hash(filename):
    if not os.path.exists(HASH_STORAGE_FILE):
        return None

    with open(HASH_STORAGE_FILE, 'r') as f:
        for line in f:
            stored_filename, stored_hash = line.strip().split(':', 1)
            if stored_filename == filename:
                return stored_hash
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html',
                                 message="No file uploaded. Please select a file.",
                                 status_type="error")

        file = request.files['file']

        if file.filename == '':
            return render_template('index.html',
                                 message="No file selected. Please choose a file to upload.",
                                 status_type="error")

        action = request.form.get('action')
        filename = file.filename
        file_hash = calculate_file_hash(file)

        if action == 'store':
            store_hash(filename, file_hash)
            return render_template('index.html',
                                 message=f"Hash stored successfully for '{filename}'. SHA-256: {file_hash[:16]}...",
                                 status_type="success")

        elif action == 'check':
            stored_hash = get_stored_hash(filename)

            if stored_hash is None:
                return render_template('index.html',
                                     message=f"No stored hash found for '{filename}'. Please store the hash first.",
                                     status_type="warning")

            if stored_hash == file_hash:
                return render_template('index.html',
                                     message=f"File integrity verified! '{filename}' has not been modified.",
                                     status_type="success")
            else:
                return render_template('index.html',
                                     message=f"Warning: File integrity check failed! '{filename}' has been modified or corrupted.",
                                     status_type="error")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
