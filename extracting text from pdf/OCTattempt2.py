from pdf2image import convert_from_path
#convert pdf to images
pdfs = r"D:/NLP/extracting text from pdf/sample.pdf"
pages = convert_from_path(pdfs, 350)
i = 1
for page in pages:
    image_name = "Page_" + str(i) + ".jpg"  
    page.save(image_name, "JPEG")
    i = i+1     