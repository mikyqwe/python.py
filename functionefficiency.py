"""Write two functions to check if a number is prime, and check which of them is more time-efficient."""
def isPrime1(num):#less efficient
	if num > 1:
		# check for factors
		for i in range(2,num):
			if (num % i) == 0:
				return False
				break
		return True

import math

def isPrime2(num):#more efficient
	if num > 1:
		# check for factors
		for i in range(2,1+int(math.sqrt(num))):
			if (num % i) == 0:
				return False
				break
		return True

import time
#we will measure the time it takes for each function in miliseconds
def checkefficiency(a,b):
	time1started=int(time.time()*1000)#time 1st function starts
	a(399989)
	time1ended=int(time.time()*1000)#time 1st endswith
	effic1=time1ended-time1started#efficiency measured in time for isPrime1
	time2started=int(time.time()*1000)#time 2nd fction starts
	b(399989)#we call the function for the same number as isPrime1
	time2ended=int(time.time()*1000)#time 2nd function ends
	effic2=time2ended-time2started#efficiency measured in time for isPrime2
	if(effic1<effic2):
		print("The first function is more efficient than the second one!")
	else:
		print("The second function is more efficient than the first one!")

checkefficiency(isPrime1,isPrime2)
