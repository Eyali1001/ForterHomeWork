from fuzzywuzzy import fuzz
from nicknames import NameDenormalizer 
'''
I use fuzzywuzzy, a fuzzy logic string matching module in order to compare names with typos.
the function fuzz.ratio() returns a score up to a hundred indicating how similar the two strings are.
we always use fuzz.ratio() instead of == so that typos are ok.
nicknames is a premade parser for names.csv (nickname database I downloaded from github)
-eyal merhavi-
'''



def countUniqueNames(bf,bl,sf,sl,cn):
	TYPOTHRESHOLD = 85 #this constant decides how tolerant we are of typos
	nicknamesGet = NameDenormalizer()
	cn = cn.split(" ") # for easier use
	bf = bf.split(" ")[0] #remove middle name
	sf = sf.split(" ")[0]
	try: 
		possibleNames = nicknamesGet[bf] # returns a set with all possible nicknames in lower case
	except KeyError:
		possibleNames = set([bf]) #if the name is not in the nickname database we just create a set with it
		
	uniqueCounter = 0
	
	for n in [(sf,sl),(cn[0],cn[-1])]: #we only want the first and last names in cn
		if (not isNickname(n[0],possibleNames,TYPOTHRESHOLD) and fuzz.ratio(n[0],bf)<TYPOTHRESHOLD) or (fuzz.ratio(n[1].lower(),bl.lower())<TYPOTHRESHOLD) : #if the name is not a nickname (or equals to the name) or the family name is different add 1 to the unique name counter
			uniqueCounter+=1
			

	
	#now we need to check if the shipping adress name and credit card name are unique to each other:
	try: 
		possibleNames = nicknamesGet[sf] 
	except KeyError:
		possibleNames = set([sf])
	if (not isNickname(cn[0],possibleNames,TYPOTHRESHOLD) and fuzz.ratio(cn[0],bf)<TYPOTHRESHOLD) or (fuzz.ratio(cn[-1].lower(),sl.lower())<TYPOTHRESHOLD):
		uniqueCounter+=1
	
	return uniqueCounter if uniqueCounter!=0 else 1 #if no names are different then there are 1 unique names
	
	
def isNickname(name,set,TYPOTHRESHOLD): #gets a name and a set of names and checks if it is in the set (considering typos)
	for n in set:
		if fuzz.ratio(name.lower(),n)>TYPOTHRESHOLD:
			return True
	return False
	
	
#I've tested the program with the exmaples in the challenge instructions and the following and they all returned the expected results:

# countUniqueNames("eyal","elk","eyali","elk","Deborah elkik") = 2

# countUniqueNames("eyal","elk","eyali","elk","eyal j elki") = 1

# countUniqueNames("bill","john","will","john","Bill John") = 1 since will and bill are nicknames

# countUniqueNames("bill","john","will","john","Gill John") = 2

# countUniqueNames("something","john","will","john","Bill John") = 2

# countUniqueNames("something","john","something else","john","Bill John") = 2

# countUniqueNames("name","one","name","two","name three") = 3