import os
from fpdf import FPDF

pdf = FPDF()


pdf.add_page()

pdf.set_font("Arial", size = 9)

save_path1 = os.getcwd()+'\Output'
file_name1 = "txt.file"
cName = os. path. join(save_path1, file_name1)
f = open(os. path. join(save_path1, file_name1), "r")

# insert the texts in pdf
for x in f:
	pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

# save the pdf with name .pdf
save_path = os.getcwd()+'\Output'
file_name = "XSS_Parameters.pdf"
completeName = os. path. join(save_path, file_name)

pdf.output(completeName)
