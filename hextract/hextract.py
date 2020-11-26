"""Write a function that receives two parameters: a_path and to_hextract. If a_path is a valid zip archive and to_hextract  is a file inside the arhive the function will return the md5 digest for unzipped content of to_hextract and None otherwise."""
import hashlib, zipfile, shutil
from zipfile import ZipFile
import os
FILE2FIND="test.txt"#path to the file you want to find
ARCHIVE="test.zip"#path to the archive where we'll search the file
WORK="FKMslPWsLwynsJSWwQPW"#random folder name where we will extract the archive

def file2md5(f):
	"""This function will return the file digested in md5"""
	hash_md5=hashlib.md5()
	with open(f,"rb") as f:
		for chunk in iter(lambda:f.read(4096),b""):#reading chunks b of 4096bytes from the file
			hash_md5.update(chunk)
	return hash_md5.hexdigest()
md5FileToFind=file2md5(FILE2FIND)

def hextract(a_path, to_hextract):
	if (zipfile.is_zipfile(a_path)):#if a_path is a valid zip
		print("is zipfile")#debug only
		with ZipFile(a_path, 'r') as zip:
			zip.extractall(WORK)
			listOfFileNames=zip.namelist()
			for file in listOfFileNames:
				if(file.endswith(to_hextract)):#if the name was found in the archive
					path=os.getcwd()+"/"+WORK+"/"+file#path to unpacked file
					md5currentFile=file2md5(path)
					if (md5FileToFind==md5currentFile):
						print("The md5 digest for the content of the file found in the archive is:" + md5currentFile)
		shutil.rmtree(WORK)#after working with the unzipped archive we will delete it
	else:
		return False
		
hextract(ARCHIVE, FILE2FIND)
