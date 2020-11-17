"""Write a program that will write the minutes passed from the start, every x seconds, where x is random chosen at each iteraton (from the inteval [a, b] , where a, b are arguments). The program will run infinitely."""
import time, random

def f(a,b):
	t = time.localtime()
	while(1):
		time.sleep(random.randint(a,b))
		t1=time.localtime()
		time_passed=(t1.tm_mday*24*60*60+t1.tm_hour*60*60+t1.tm_min*60+t1.tm_sec)-(t.tm_mday*24*60*60+t.tm_hour*60*60+t.tm_min*60+t.tm_sec)
		print(time_passed)
f(1,5)