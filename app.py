from fastapi import FastAPI, File, UploadFile
import pdfplumber

app = FastAPI()

@app.post("/parse")
async def parse_pdf(file: UploadFile = File(...)):
    # Read PDF binary
    data = await file.read()
    text = ""
    with pdfplumber.open(io.BytesIO(data)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return {"text": text}
