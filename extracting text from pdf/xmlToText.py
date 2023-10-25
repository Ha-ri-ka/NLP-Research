from xml.etree import cElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()

for page in root.findall('page'):
    print("Title: ", page.find('title').text)
    print("Content: ", page.find('content').text)