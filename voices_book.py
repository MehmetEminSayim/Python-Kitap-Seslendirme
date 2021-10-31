import pyttsx3
import PyPDF2

story = open("papatya.pdf","rb")
pdfVoice = PyPDF2.PdfFileReader(story)

engine = pyttsx3.init()
voices = engine.getProperty("voices")

engine.setProperty("voice",voices[0].id)

for page_num in range(0,pdfVoice.numPages):
    page = pdfVoice.getPage(page_num)
    write = page.extractText()
    engine.say(write)
    engine.runAndWait()