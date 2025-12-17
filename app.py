from flask import Flask, render_template, request
import hashlib
import os

app = Flask(__name__)

HASH_FILE = "file_hashes.txt"


def calculate_file_hash(file):
    sha256 = hashlib.sha256()
    file.seek(0)
    while True:
        data = file.read(4096)
        if not data:
            break
        sha256.update(data)
    file.seek(0)
    return sha256.hexdigest()


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    status_type = "neutral"

    if request.method == "POST":
        file = request.files.get("file")
        action = request.form.get("action")

        if not file or file.filename == "":
            message = "No file selected."
            status_type = "warning"

        else:
            file_hash = calculate_file_hash(file)

            if action == "store":
                with open(HASH_FILE, "a") as f:
                    f.write(f"{file.filename}:{file_hash}\n")

                message = "Hash stored successfully."
                status_type = "success"

            elif action == "check":
                stored_hash = None

                if os.path.exists(HASH_FILE):
                    with open(HASH_FILE, "r") as f:
                        for line in f:
                            name, hash_val = line.strip().split(":")
                            if name == file.filename:
                                stored_hash = hash_val
                                break

                if stored_hash is None:
                    message = "No stored hash found for this file."
                    status_type = "warning"
                elif stored_hash == file_hash:
                    message = "File integrity verified."
                    status_type = "success"
                else:
                    message = "Integrity check failed."
                    status_type = "error"
            else:
                message = "Invalid action."
                status_type = "error"

        # DEBUG CONFIRMATION (you can remove later)
        print("ACTION:", action)
        print("MESSAGE:", message)
        print("STATUS:", status_type)

    return render_template(
        "index.html",
        message=message,
        status_type=status_type
    )


if __name__ == "__main__":
    app.run(debug=True)
