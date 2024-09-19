# This app does not have any GUI(Graphical user interface)
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}")

    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {invoice_nr}")


    pdf.output(f"PDFs/{filename}.pdf")