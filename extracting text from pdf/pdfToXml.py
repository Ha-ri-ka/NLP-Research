import aspose.pdf as pdf
# Load the license
license = pdf.License()
# license.set_license("Aspose.Total.lic")
# Create a Document class object
path="D:/NLP/extracting text from pdf/sample.pdf"
document = pdf.Document(path)
# Convert PDF to XML
document.save("PDFtoXML.xml" , pdf.SaveFormat.PDF_XML)
print("PDF to XML Converted Successfully")