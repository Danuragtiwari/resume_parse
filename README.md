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
<br>
![Screenshot (136)](https://github.com/user-attachments/assets/313cf3a0-4706-4b81-b877-ebda588e09ef)
<br><br>
![Screenshot (135)](https://github.com/user-attachments/assets/1c8a6dc6-5563-4fa1-bdfa-87d38d75adf5)
<br><br>
![Screenshot (134)](https://github.com/user-attachments/assets/46702f3c-e84b-40dc-9a0b-f61cd711e733)
<br><br><br>
![Screenshot (133)](https://github.com/user-attachments/assets/205c2579-70fe-4fb8-95a2-b508ebd47e05)
<br>
<br>
