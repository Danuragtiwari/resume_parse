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
      .
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
`pip install -r requirements.txt`
# Run the Django development server:
`python manage.py runserver`

Open your browser and navigate to http://127.0.0.1:8000/upload/ to upload a resume and extract the data.

## SS of the projects
<br>

![Screenshot (1)](https://github.com/user-attachments/assets/0fbca0d0-6817-4a0c-9607-2ee6078e7dca)
<br><br>
![Screenshot (2)](https://github.com/user-attachments/assets/00b61fb9-bea2-4be7-a59a-0b80cf252242)
<br><br>
![Screenshot (3)](https://github.com/user-attachments/assets/590a13cc-b269-4993-8c5b-05091bd4bbdb)
<br><br>
![Screenshot (4)](https://github.com/user-attachments/assets/2fe72b99-3286-4f66-9e45-451759f15e11)
<br>

