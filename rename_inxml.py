import os
import xml.etree.ElementTree as xmlParser
from natsort import natsorted
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--x", required = True, help = "folder of path all xml files to be rename")
args = vars(ap.parse_args())

ano_path = args["x"]
all_files = natsorted(os.listdir(ano_path))
for file in all_files:
    xmlDoc = xmlParser.parse(os.path.join(ano_path,file))
    rootElement = xmlDoc.getroot()
    
    for element in rootElement.iter('filename'):
        element.text = os.path.splitext(file)[0] + '.JPEG'
        new_file = element.text 
        
    for element in rootElement.iter('folder'):
        element.text = file[:7]
        new_file = element.text
        
# Saving the xml
    xmlDoc.write(os.path.join(ano_path, file))