# AI Attention Visualizer

AI Attention Visualizer is a Streamlit-based application that extracts text from an uploaded image using OCR and visualizes attention scores for the extracted words.

## Demo

[Live Demo - AI Attention Visualizer](https://aiattentionvisualizer-bnw9mqgaie7rb8ybm5cm8g.streamlit.app/)

## Screenshot

![AI Attention Visualizer Demo](screenshots/demo.png)

## Features

* Upload an image
* Extract text using Tesseract OCR
* Split extracted text into words
* Generate word embeddings
* Calculate attention scores
* Visualize attention scores
* Display important words based on attention

## How It Works

Image Upload
↓
Tesseract OCR
↓
Extracted Text
↓
Word Splitting
↓
Word Embeddings
↓
Attention Score Calculation
↓
Attention Visualization

## Technologies Used

* Python
* Streamlit
* Tesseract OCR
* Pytesseract
* NumPy
* Matplotlib
* Pillow

## Project Structure

```text
AI_Attention_Visualizer/
│
├── app.py
├── ocr.py
├── attention.py
├── embedding.py
├── preprocessing.py
├── requirements.txt
├── packages.txt
├── README.md
└── screenshots/
    └── demo.png
```

## Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Make sure Tesseract OCR is installed on your system.

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Author

Devisree T
