#####################
#  Auto XML to CSV  #
#####################

import argparse
import pandas as pd
import xml.etree.ElementTree as ET
import os
import glob
import time


description = """
This python script creates a csv out of all the XMLs and
displays file names, count of each object tagged in it.
"""


def _main_(args):
	xml_folder_path = args["input"]  # xml_folder_path as input
	if not args["output"]:
		csv_folder_path = args["input"]  #folder_path to csv as output
		output_folder = os.path.join(csv_folder_path,'output_csv')
		os.makedirs(output_folder,exist_ok=True)
	else:
		output_folder = None
		csv_folder_path = args["output"]  #folder_path to csv as output
		os.makedirs(csv_folder_path,exist_ok=True)

	def get_labels(xml_folder_path):
		labels = []
		for xml_file in sorted(glob.glob(os.path.join(xml_folder_path, '*.xml'))):
			tree = ET.parse(xml_file)
			root = tree.getroot()
			labels += [i.text for i in root.iter('name') if i not in labels]
		return list(set(labels))


	labels = get_labels(xml_folder_path) # list of all the objects tagged 

	print(f"INFO: Labels found: {labels}")


	var_dict = {i:[] for i in labels} #dictionary of empty list for each label
	# print(var_dict)

	file_name = [] #to store file name

	for xml_file in sorted(glob.glob(os.path.join(xml_folder_path, '*.xml'))):
		# print(xml_file)
		_, xml_name = os.path.split(xml_file) #extracting file name from xml path
		file_name.append(xml_name)
		tree = ET.parse(xml_file)
		root = tree.getroot()
		items = [items.text for items in root.iter('name')]
		for x in labels:
			count = items.count(x)
			var_dict[x].append(count)

	col_dict = {'File_name':file_name}

	# dictionary for columns  
	col_dict.update(var_dict) 

	df = pd.DataFrame(col_dict) #complete dataframe


	timestmp = time.strftime("%d_%m_%Y_%H_%M") #generate timestamp
	# print (timestmp)

	# if not os.path.exists(csv_folder_path):   #check if output folder exists
	# 	os.makedirs(csv_folder_path)          #if not create one
	if output_folder:
		df.to_csv(os.path.join(output_folder , f"xml2csv_{timestmp}.csv"))
	else:
		df.to_csv(os.path.join(csv_folder_path , f"xml2csv_{timestmp}.csv"))
	print('INFO: Successfully created CSV')


if __name__ == '__main__':
	argparser = argparse.ArgumentParser(description = description)
	argparser.add_argument('-i', '--input', help='path to directory of XMLs',required=True)
	argparser.add_argument('-o', '--output', help='path to directory of CSV output')
	args = vars(argparser.parse_args())
	_main_(args)


##########################################################################################################################
# 
# python auto_xml2csv.py -i '../ppe_corrected_mayur/v1/yolo/train/data/modified_val_xml' 
#
##########################################################################################################################
