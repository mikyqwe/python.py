"""Write a script to simulate loto 6/49 draw (numbers extraction). The output should be a list of six numbers between 1 and 49 representing the winning combination."""
import random

NUMBERS_TO_EXTRACT=6 #we will extract 6 numbers
RANGE=49 #we will extract numbers from 1 to 49


def lotto():
	extracted=[]
	numbersExtracted=0
	while numbersExtracted<NUMBERS_TO_EXTRACT:
		new_number=random.randint(1,49)
		if new_number not in extracted:
			extracted.append(new_number)
			numbersExtracted+=1
	return extracted

print(lotto())