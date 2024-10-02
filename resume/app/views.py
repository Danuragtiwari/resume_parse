

from django.shortcuts import render
from .utils import extract_text_from_pdf, extract_info

def upload_resume(request):
    if request.method == 'POST':
        file = request.FILES['file']
        text = extract_text_from_pdf(file)
        extracted_data = extract_info(text)
        return render(request, 'result.html', {'data': extracted_data})

    return render(request, 'upload.html')
