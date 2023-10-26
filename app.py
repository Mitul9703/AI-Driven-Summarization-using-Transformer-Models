from flask import Flask, render_template, request, redirect

import PyPDF2

app = Flask(__name__, static_folder="static", template_folder="templates")

# Function to get the first 500 lines from a PDF file
def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(min(500, len(pdf_reader.pages))):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf_file' not in request.files:
        return redirect(request.url)
    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
        return redirect(request.url)

    if pdf_file:
        # Extract and display the first 500 lines from the PDF
        text = extract_text_from_pdf(pdf_file)

        return render_template('index.html', pdf_file = pdf_file, text=text)

if __name__ == '__main__':
    app.run(debug=True)
