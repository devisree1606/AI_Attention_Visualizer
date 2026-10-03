# AI Attention Visualizer

AI Attention Visualizer is a Streamlit-based application that extracts text from an uploaded image using OCR and visualizes attention scores for the extracted words.

## Demo

[Live Demo - AI Attention Visualizer](https://aiattentionvisualizer-bnw9mqgaie7rb8ybm5cm8g.streamlit.app/)

## Screenshot
<img width="1366" height="768" alt="Screenshot (116)" src="https://github.com/user-attachments/assets/f713e602-6588-4ced-8041-cf84329f4689" />
<img width="1366" height="768" alt="Screenshot (117)" src="https://github.com/user-attachments/assets/cd7d6d35-7b0c-48ec-bf12-5665c6584601" />
<img width="1366" height="768" alt="Screenshot (118)" src="https://github.com/user-attachments/assets/4e9db536-4cee-424a-9515-96054ac7cc2e" />
<img width="1366" height="768" alt="Screenshot (119)" src="https://github.com/user-attachments/assets/42fa32fc-1e85-445f-b176-01ca03397202" />





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


pip install -r requirements.txt


Make sure Tesseract OCR is installed on your system.

## Run the Application


streamlit run app.py


The application will open in your browser.

## Author

Devisree T
