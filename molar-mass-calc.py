# Molar Mass Calculator
import sys
import periodictable as pt

def isNumber(x):
	nums = ['0','1','2','3','4','5','6','7','8','9']
	if x in nums:
		return True
	else:
		return False

# Ended up not needing this function (might come in use later?)
def countElements(compound):
	counter = 0
	for i in range(0,len(compound)):
		if compound[i].isupper():
			counter += 1
	return counter

def divideByElements(compound):
	# currElement = ""
	# nextElement = ""
	# elementList = []
	# for i in range(0,countElements(compound)-1):
	# 	# Find next upper case letter
	# 	for y in range(len(compound)-1,0,-1):
	# 		if compound[y].isupper() == True:
	# 			nextElement = compound[y]
	# 	currElement += compound[0:compound.index(nextElement)]
	# 	elementList.append(currElement)
	# 	compound = compound[compound.index(nextElement):]
	comp = compound
	elementIndex = 0
	element = ""
	elementList = []
	for i in range(0,countElements(comp)):
		for y in range (0,len(comp)):
			if comp[y].isupper() == True:
				elementIndex = y
		element = comp[elementIndex:]
		comp = comp[0:elementIndex]
		elementList.append(element)


	return elementList


while True:
	comp = input("Enter compound. Type 'exit' to leave program: ")
	if comp == "exit":
		sys.exit("Program exited.")
	elementList = divideByElements(comp)
	mmList = []
	# print(countElements(comp))
	# print(divideByElements(comp))

	coeff = 0
	for x in elementList:
		if isNumber(x[-1]):
			coeff = int(x[-1])
			x = x[:-1]
			g = getattr(pt,x)
			mm = g.mass
			mm = mm*coeff
			mmList.append(mm)
		elif isNumber(x[-1]) == False:
			g = getattr(pt,x)
			mm = g.mass
			mmList.append(mm)
	# print(mmList)
	mmFinal = 0
	for x in mmList:
		mmFinal += x
	print("Molar Mass: " + str(mmFinal) + " g/mol")


# counter = 0
# lowerBound = 0
# upperBound = 0
# ele = ""
# for i in range (0,len(comp)-2):
# 	if comp[i].isupper(): 	 
# 		lowerBound = i
# 		if isNumber(comp[i+1]):
# 			upperBound = i+2
# 		elif comp[i+1].islower():
# 			upperBound = i+1
# 		ele = comp[lowerBound:upperBound]
# 		g = getattr(pt,ele)
# 		if isNumber(comp[i+1]):
# 			counter += (g.mass * int(comp[i+1]))
# 		elif isNumber(comp[i+2]):
# 			counter += (g.mass* int(comp[i+2]))# 			counter += g.mass

# print("Molar mass: ", counter)