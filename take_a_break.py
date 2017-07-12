import time
import webbrowser
import os

print "Time interval between two consecutive breaks?"
hr=int(raw_input("how many hrs->"))
minute=int(raw_input("how many min->"))
sec=int(raw_input("how many sec->"))
t=hr*3600+minute*60+sec
total=int(raw_input("total no. of breaks?->"))
flag=0
while (flag<total):
	time.sleep(t)
	flag+=1
	webbrowser.open("https://www.google.co.in",new=0,autoraise=True)
	os.system("clear")
	print str(flag)+" break"
print "				The End				"
