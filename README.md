# File Integrity Checker - Frontend

A modern, professional cybersecurity web application for hash-based file integrity verification.

## Features

- **Dark Theme Design** with blue and green security accents
- **Drag & Drop File Upload** with visual feedback
- **Responsive Layout** optimized for desktop and mobile devices
- **Professional UI** with smooth animations and transitions
- **Accessibility** with keyboard navigation and high contrast
- **Status Indicators** for success, error, and warning messages

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Flask application:**
   ```bash
   python app.py
   ```

3. **Open your browser:**
   ```
   http://localhost:5000
   ```

## File Structure

```
project/
├── app.py              # Flask backend with hash storage/verification
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Main HTML template (Flask Jinja2)
├── static/
│   ├── style.css       # All styling and responsive design
│   └── app.js          # Drag & drop functionality and UX enhancements
└── README.md           # This file
```

## How It Works

### Backend (app.py)

The Flask backend implements two main operations:

1. **Store Hash** - Calculates SHA-256 hash of uploaded file and stores it in `file_hashes.txt`
2. **Verify Integrity** - Compares current file hash with stored hash to detect modifications

```python
# Hash calculation
def calculate_file_hash(file):
    sha256_hash = hashlib.sha256()
    for byte_block in iter(lambda: file.read(4096), b""):
        sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```

### Frontend Integration

The HTML template uses Flask's Jinja2 templating with the following structure:

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    # Process file upload and return status
    return render_template('index.html',
                         message=message,
                         status_type=status_type)
```

### Status Types

The template supports four status types for the status indicator:

- `success` - Green indicator (file verified, hash stored)
- `error` - Red indicator (integrity check failed, errors)
- `warning` - Orange indicator (warnings, cautions)
- `neutral` - Blue indicator (informational messages)

### Form Data

The form sends:
- **Method:** `POST`
- **Encoding:** `multipart/form-data`
- **File field name:** `file`
- **Action field name:** `action`
  - Value: `store` for storing hash
  - Value: `check` for verifying integrity

## Design Features

### Color Palette
- **Primary Accent:** Blue (#3b82f6)
- **Secondary Accent:** Green (#10b981)
- **Error State:** Red (#ef4444)
- **Warning State:** Orange (#f59e0b)
- **Background:** Dark gradients (#0a0e1a to #141821)

### Typography
- System font stack with Inter preference
- 150% line height for readability
- Gradient text for headlines
- Responsive font sizing

### Interactions
- Hover effects on all interactive elements
- Smooth transitions (250ms)
- Drag & drop visual feedback
- Button press animations
- File name display after selection

### Responsive Breakpoints
- Desktop: 768px and above
- Tablet: 480px to 768px
- Mobile: Below 480px

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Accessibility

- WCAG 2.1 Level AA compliant
- Keyboard navigation support
- High contrast text (4.5:1 minimum)
- Focus indicators on all interactive elements
- Screen reader friendly markup
- Reduced motion support for users with motion sensitivity

## License

Created for cybersecurity internship demonstration purposes.
