# Resume Data Extractor

This project is a Django-based web application that allows users to upload resumes (in PDF format) and extracts key information such as Name, Phone Number, Email Address, Education, Work Experience, Technologies, and Achievements/Participations. It uses Python's `pdfplumber` for reading PDFs and Regular Expressions (Regex) for extracting specific sections of the resume.

## Features

- **PDF Upload:** Users can upload their resumes in PDF format.
- **Resume Parsing:** Extracts key information such as:
  - Name
  - Phone Number
  - Email Address
  - Education: Institutions and timeframes
  - Work Experience: Company names and durations
  - Technologies: List of technical skills mentioned
  - Achievements/Participations
- **User Interface:** Simple and user-friendly interface for uploading resumes and viewing extracted data.

## Tech Stack

- **Backend Framework:** Django
- **Frontend:** HTML, CSS
- **PDF Parsing:** pdfplumber
- **Data Extraction:** Python, Regular Expressions (Regex)

## Project Structure
resume/
│
├── app/
│   ├── templates/
│   │   ├── upload.html
│   │   ├── result.html
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── utils.py
│   └── forms.py
│
├── resume/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md

# Install the required dependencies:
pip install -r requirements.txt
# Run the Django development server:
python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/upload/ to upload a resume and extract the data.

## venv folder for virtual Environments