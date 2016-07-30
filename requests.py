import re
import os
from rmdoc import *

path = '' 
def php_requests(file_name,var_name='false',line_num = 0,flag=0):
	
	if flag != 0:
		print 'Enter main path:'
		global path
		path = raw_input()
		

	#simple-support-ticket-system
	if path not in file_name:
		file_name =  path + file_name

	 

	doc_command = 0
	if var_name == 'false' and '_tmp' not in file_name :
		php_rmdoc(file_name)

		for line in open(file_name+'_tmp') :
			line_num += 1

			if line.find('$_POST') != -1 or line.find('$_GET') != -1 or line.find('$_REQUEST') != -1: 
				
				if line.find("if") != -1:
					continue

				if line.find("=") == -1:
					print "---> Vulnerability is found: "+ line;
					print "line numberf : " + str(line_num)
					continue

				if line.find("=") != -1 and line.find("$")<line.find("="):
					var_name = line.rsplit("=")[0]
					# print var_name
					# print "line number : " + str(line_num)

				php_requests(file_name+'_tmp',var_name,line_num)

			if line.find('require_onc') != -1:
				file_name1 =  re.search("'(.+?)'",line ).group(1) 
				if line.find('"') != -1:
					file_name1 =  re.search('"(.+?)"',line ).group(1)

				php_requests(file_name1)


			if line.find('include_onc') != -1:
				if re.search("'(.+?)'",line ) and line.find("'") != -1:
					file_name1 =  re.search("'(.+?)'",line ).group(1) 
				if re.search("'(.+?)'",line ) and line.find('"') != -1:
					file_name1 =  re.search('"(.+?)"',line ).group(1) 

				php_requests(file_name1)
				
			
	else:
		esc = 0
		for line1 in open(file_name) :
			line1 = line1.strip()
			var_name1 = var_name.strip()
			var_name = var_name1.replace('$','');

			var_exp = r"\b" + re.escape(var_name) + r"\b" #whole word section 
			if var_name1.find(var_name1) != -1 and re.search(var_exp,line1):  
		
				if line1.find('esc_sql(') != -1 or line1.find('(int)') != -1 or line1.find('real_escape_string') != -1:
					esc = 1
					break
		 
		if esc == 0:
			print "\n---> Vulnerability is found : $"+ var_name + "\nfile name: "+file_name.replace('_tmp','')
			print "Line number : " + str(line_num)



		 
