import pdfplumber
import re

def extract_text_from_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    text += "\n"
    except Exception as e:
        print(f"An error occurred: {e}")
    # print(text)
    return text


def extract_info(text):
    name = re.search(r"\b[A-Z][a-z]*\s[A-Z][a-z]*\b", text)

    # 
    phone = re.search(r"\+?\d{1,3}[\s-]?\(?\d{2,3}\)?[\s-]?\d{3,4}[\s-]?\d{4,5}", text)

    # 
    email = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)

    #
    education_pattern = r"(•.+?)(\d{4}\s?-\s?\d{4})"
    # print(\\b(Experience(s?)|EXPERIENCE(S?))\\b")
    education_matches = re.findall(education_pattern, text)
    education = [{"institution": edu[0].strip("• "), "years": edu[1]} for edu in education_matches]

    # Ex
    education_pattern = r"(•.+?)(\d{4}\s?-\s?\d{4})"
    education_matches = re.findall(education_pattern, text)
    education = [{"institution": edu[0].strip("• "), "years": edu[1]} for edu in education_matches]

    # )
    experience_pattern = r"•(.+?)\s*(?:\(?([A-Za-z]+\s\d{4})\s–\s([A-Za-z]+\s\d{4})|\(?(\d{4})\s*–\s*(\d{4})\))"
    experience_matches = re.findall(experience_pattern, text)
      # 
    experience_pattern = r"•(.+?)\s*(?:\(?([A-Za-z]+\s\d{4})\s–\s([A-Za-z]+\s\d{4})|\(?(\d{4})\s*–\s*(\d{4})\))"
    experience_matches = re.findall(experience_pattern, text)
    experience = []
    
    for exp in experience_matches:
        company = exp[0].strip()
        if exp[1] and exp[2]:  #
            experience.append({
                "company": company,
                "start_date": exp[1],
                "end_date": exp[2]
            })
        elif exp[3] and exp[4]:  
            experience.append({
                "company": company,
                "start_year": exp[3],
                "end_year": exp[4]
            })
        else:
            
            experience.append({
                "company": company,
                "start_date": exp[1] or exp[3] or "Unknown",
                "end_date": exp[2] or exp[4] or "Unknown"
            })
    #
    technologies = re.findall(r"Languages:\s*(.*)", text)
    dev_tools = re.findall(r"Developer Tools:\s*(.*)", text)
    frameworks = re.findall(r"Frameworks:\s*(.*)", text)
    other_skills = re.findall(r"other skills:\s*(.*)", text)
    achivements=re.findall(r'Achievements/Participations\s+•(.+?)\.\s+•(.+?)\.\s+•(.+?)\.', text)

    return {
        "name": name.group(0) if name else None,
        "phone": phone.group(0) if phone else None,
        "email": email.group(0) if email else None,
        "education": education,
        "experience": experience if experience else "Experience details not found",
        "technologies": dev_tools+technologies  if dev_tools+technologies else "technologies details not found",
        "others":other_skills+frameworks if other_skills+frameworks else "others skills not found",
        'achivements': achivements if achivements else "achivements not found",
    }