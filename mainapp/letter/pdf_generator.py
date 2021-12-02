from filestack import Client
from fpdf import FPDF
import os
from dotenv import load_dotenv
import time

load_dotenv(override=True)


class PdfGenerator:

    def __init__(self, title, content, signature,
                 api_key=os.environ['FILESTACK_API_KEY']):
        self.title = title
        self.content = content
        self.signature = signature
        self.api_key = api_key
        self.filename = f"xmas{time.strftime('%Y%m%d-%H%M%S')}.pdf"

    def create(self):
        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page('P')

        folder = './letter/letters_pdf'
        pdf.image(os.path.join(folder, 'deer.png'), w=40, h=40)

        pdf.set_font('Times', 'B', 28)
        pdf.set_text_color(110, 0, 0)
        pdf.cell(0, 20, self.title, 0, align='C', ln=1)

        pdf.set_font('Times', '', 14)
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 8, self.content, 0, align='L')

        pdf.set_font('Times', 'B', 18)
        pdf.set_text_color(110, 0, 0)
        pdf.cell(0, 18, self.signature, 0, align='L', ln=2)

        pdf.output(os.path.join(folder, self.filename))

    def share(self):
        client = Client(self.api_key)
        link = client.upload(filepath=os.path.join('./letter/letters_pdf', self.filename))
        return link.url
