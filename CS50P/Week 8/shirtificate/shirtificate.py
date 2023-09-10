from fpdf import FPDF
from PIL import Image

title = 'CS50 Shirtificate'

class PDF(FPDF):
    def header(self):
        self.set_font('helvetica' , 'B' , 30)
        title_width = self.get_string_width(title) + 6
        doc_width = self.w
        self.set_x((doc_width - title_width) / 2)
        self.cell(title_width , 10 , title , border=False , ln=1 ,  align='C')
        self.ln(10)



        self.set_font('helvetica' , size=25)



def main():

    make_pdf(input('Name: '))


def make_pdf(name):

    pdf = PDF()

    pdf.add_page(orientation="portrait")
    pdf.set_font('helvetica' , size=25)
    pdf.image('shirtificate.png', 10 , 70 , 190)
    pdf.set_text_color(255 , 255 , 255)
    pdf.cell(0 , 213 , f'{name} took CS50!' , border=False , align='C')

    pdf.output('shirtificate.pdf')

if __name__ == '__main__':
    main()