import re

def php_rmdoc(file_name):
	doc_command = 0
	fp = open(file_name+'_tmp', "w")

	for line in open(file_name) :
		
		if line.find('//') != -1:
			line = line.rsplit('//')[0];

		line = re.sub(r"/\*(.+?)\*/","",line )
		
		if line.find('/*') != -1:
			doc_command = 1 

		if doc_command == 1 and line.find('*/') != -1:
			doc_command = 0
			continue

		if doc_command == 1:
			continue


		
		# write file 
		fp.write(line)
	fp.close()
