import PyPDF2
import re

def extract_questions_from_pdf(file):

    reader = PyPDF2.PdfReader(file)
    text = ""

    # 🔥 Extract full text
    for page in reader.pages:
        text += page.extract_text() + "\n"

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    questions = []

    current_q = None
    current_a = ""

    i = 0
    while i < len(lines):
        line = lines[i]

        # ✅ Case 1: "Q1 What is Python?"
        if re.match(r"^Q\d+\s+.+", line):
            
            if current_q:
                questions.append({
                    "question": current_q,
                    "answer": current_a.strip()
                })

            current_q = line
            current_a = ""

        # ✅ Case 2: "Q1" (next line is actual question)
        elif re.match(r"^Q\d+$", line):

            if current_q:
                questions.append({
                    "question": current_q,
                    "answer": current_a.strip()
                })

            # next line is actual question
            if i + 1 < len(lines):
                current_q = f"{line} {lines[i+1]}"
                i += 1  # skip next line
            else:
                current_q = line

            current_a = ""

        # ✅ Everything else = answer
        else:
            if current_q:
                current_a += " " + line

        i += 1

    # ✅ Last question
    if current_q:
        questions.append({
            "question": current_q,
            "answer": current_a.strip()
        })

    # 🔥 DEBUG (optional)
    print("🔥 Extracted Questions:", questions[:2])

    return questions