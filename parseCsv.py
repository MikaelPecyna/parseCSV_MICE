# -*- coding: utf-8 -*-



def getMaxTaille(tab):
	max = 0 

	for t in tab: 
		if len(t) > max:
			max = len(t)

	return max 


import sys 
def parseCSV(file):
	with open(file,'r') as t:

	    lines = t.readlines()
	    if lines[3].startswith("Num"):
	    	lines = lines[3:]
	    else:
	    	lines = lines[2:]
	    
	    lines = lines[::-1]
	    gain = 0 
	    listeName = []
	    listeSurname = []
	    listeEmail = []
	    
	    
	    for line in lines:
	    	name = line.split(";")

	    	listeName.append(name[2].replace('\"', '').upper())
	    	listeSurname.append(name[3].replace('\"', '').capitalize())
	    	listeEmail.append(name[1].lower())



	    	gain += float(name[6].replace(",","."))



	    	maxName = getMaxTaille(listeName)
	    	maxSurname = getMaxTaille(listeSurname)

	    	
	    	
	    print("\033[0;31m" + '|NOM:'.ljust(maxName+10) + "|Prénom:".ljust(maxSurname+10) + "|Mail:" )
	    for i in range(len(listeName)):
	    	strNum = "[" + str(i+1) + "]"
	    	strNum = strNum.ljust(6)
	    	if i%2==0:
	    		print("\033[0;35m"+ strNum + "|" + listeName[i].ljust(maxName+5)  + "|" + listeSurname[i].ljust(maxSurname+5) +  "|" + listeEmail[i])
	    	else: 
	    		print("\033[0;33m"+ strNum + "|" + listeName[i].ljust(maxName+5)  + "|" + listeSurname[i].ljust(maxSurname+5) +  "|" + listeEmail[i])

	    print('\033[47m' +  '\033[4m' +"Gain: " + str(gain)[:6] + "\033[00m")






parseCSV(sys.argv[1])


