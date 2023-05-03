import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx") # grabbing a list of the valid file extentions

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") # read each excel file
    pdf = FPDF(orientation="P", unit="mm", format="A4") # prep the  page
    pdf.add_page()
    filename = Path(filepath).stem # grab the name of the file
    invoice_nr = filename.split("-")[0] # split by - and grab only the invoice number
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")
    pdf.output(f"PDFs/{filename}.pdf") # output as invoice pdf