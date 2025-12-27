# AI Skin Scan Screening Device

A modern, minimal web application for AI-powered skin scan analysis.

## Features

- 🎨 Modern, minimal UI inspired by contemporary design principles
- 📸 Image upload via drag-and-drop or file browser
- 🔄 Real-time image preview
- 🚀 Flask backend with model integration ready
- 📱 Fully responsive design
- ♿ Accessible UI components

## Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
.
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── styles.css        # CSS styling
│   └── script.js         # JavaScript functionality
├── uploads/              # Uploaded images storage
└── README.md
```

## Model Integration

To integrate your ML model:

1. Add your model file to the project
2. Install required ML dependencies in `requirements.txt`
3. Update the model loading section in `app.py`:

```python
# Load your model
from your_model_module import load_model
model = load_model('path_to_model')

# Use in /analyze endpoint
prediction = model.predict(image_path)
```

## Design Features

- **Color Scheme**: Warm beige (#E8E2D8) background with coral (#E77656) accents
- **Typography**: Poppins font family for clean, modern aesthetics
- **Layout**: Centered, card-based design with smooth animations
- **Interactions**: Hover effects, smooth transitions, and intuitive UX

## API Endpoints

- `GET /` - Main application page
- `POST /analyze` - Image analysis endpoint
- `GET /health` - Health check endpoint

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## License

MIT License
