# Usage Guide

## File Integrity Checker - How to Use

### Scenario 1: Storing a File Hash

1. Launch the application by running `python app.py`
2. Open your browser to `http://localhost:5000`
3. Click the upload zone or drag a file onto it
4. Click the **"Store Hash"** button
5. You'll see a success message: "Hash stored successfully for 'filename.txt'. SHA-256: abc123def456..."

### Scenario 2: Verifying File Integrity (Unchanged File)

1. Upload the same file again
2. Click the **"Verify Integrity"** button
3. Success message: "File integrity verified! 'filename.txt' has not been modified."
4. Green indicator shows the file is intact

### Scenario 3: Detecting File Modifications

1. Open the original file in a text editor and make any change
2. Upload the modified file
3. Click **"Verify Integrity"**
4. Warning message: "File integrity check failed! 'filename.txt' has been modified or corrupted."
5. Red indicator alerts you to the modification

### Scenario 4: Checking an Unknown File

1. Upload a file that hasn't been stored yet
2. Click **"Verify Integrity"**
3. Warning message: "No stored hash found for 'newfile.txt'. Please store the hash first."
4. Orange indicator suggests storing the hash first

## Use Cases

### Software Distribution
Verify that downloaded software hasn't been tampered with by comparing against the official hash.

### Legal/Compliance
Prove that documents haven't been altered since a specific date by storing their hashes.

### Personal Backups
Ensure your backup files match your originals by periodically checking file integrity.

### Security Auditing
Monitor critical system files for unauthorized changes in a basic security monitoring setup.

## Technical Details

### Hash Algorithm
- **Algorithm:** SHA-256 (Secure Hash Algorithm 256-bit)
- **Output:** 64-character hexadecimal string
- **Security:** Cryptographically secure, collision-resistant

### Storage Format
Hashes are stored in `file_hashes.txt` in the format:
```
filename.txt:a1b2c3d4e5f6...
document.pdf:9f8e7d6c5b4a...
```

### Limitations
- Basic implementation stores hashes in a text file (production apps should use a database)
- No user authentication (any user can access all hashes)
- File names must be unique (duplicate names will have multiple hash entries)
- No hash history tracking (only the most recent hash is used for verification)

## Keyboard Shortcuts

- **Tab** - Navigate between upload zone and buttons
- **Enter/Space** - Activate focused element
- **Escape** - Clear file selection (when focused on upload zone)

## Browser Compatibility

Tested and working on:
- Chrome 120+
- Firefox 121+
- Safari 17+
- Edge 120+
- Mobile Chrome (Android)
- Mobile Safari (iOS)

## Troubleshooting

### Issue: "No file selected" error
**Solution:** Make sure you've selected a file before clicking either button.

### Issue: File upload doesn't work
**Solution:** Check file permissions and ensure the Flask app has write access to the directory.

### Issue: Drag and drop not working
**Solution:** Ensure JavaScript is enabled in your browser.

### Issue: Styles not loading
**Solution:** Verify the `static` folder contains `style.css` and `app.js`.
