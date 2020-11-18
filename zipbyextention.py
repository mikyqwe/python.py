"""Write a function that receives two parameters: a_path and ext. The script will add all files from the a_path folder that have the extension ext to a zip archive named the.zip."""
import zipfile
import os

def f(a_path,ext):
	z=zipfile.ZipFile("the.zip","w")
	for filename in os.listdir(a_path):
		if os.path.splitext(filename)[1]==ext:
			z.write(filename)
	z.close()
f(".",".py")