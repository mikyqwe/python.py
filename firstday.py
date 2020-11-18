"""Write a script that writes the day of the week for the New Year Day, for the last x years (x is given as argument)."""
import time

saptamana=["Luni","Marti","Miercuri","Joi","Vineri","Sambata","Duminica"]
def f(x):
	date="01-01"
	for i in range(1,x+1):
		currentYear=2020+1-i
		currentdate=date+"-"+str(currentYear)
		formatedate=time.strptime(currentdate,"%m-%d-%Y")
		print("Pentru anul {} prima zi a saptamanii este {}".format(currentYear,saptamana[formatedate.tm_wday]))
f(5)