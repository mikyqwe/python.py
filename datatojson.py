"""Write a script that receives a directory as argument and creates a JSON file with data about all the files in that directory. For each file, the following information will be displayed: file_name, md5_file, sha256_file, size_file (in bytes), time when the file was created (human-readable) and the absolute path to the file."""
import os
import hashlib
import json
import time

path="."
dict={}
for filename in os.listdir(path):
	filedict={}
	filedict["nume_fisier"]=filename
	hash_md5=hashlib.md5()
	hash_sha256=hashlib.sha256()
	with open(filename, "rb") as f:
		content=f.read()
		hash_md5.update(content)
		hash_sha256.update(content)
	filedict["md5_file"]=hash_md5.hexdigest()
	filedict["sha256_file"]=hash_sha256.hexdigest()
	filedict["size"]=os.stat(os.path.join(path,filename)).st_size
	filedict["creation_date"]=time.asctime(time.gmtime(os.stat(os.path.join(path,filename)).st_ctime))
	filedict["absolute_path"]=os.path.abspath(filename)
	dict[filename]=filedict

with open('data.json', 'w') as f:
	json.dump(dict,f)