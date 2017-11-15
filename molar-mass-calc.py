# Molar Mass Calculator
import sys
# package found online
import periodictable as pt

def isNumber(x):
	nums = ['0','1','2','3','4','5','6','7','8','9']
	if x in nums:
		return True
	else:
		return False

def countElements(compound):
	counter = 0
	for i in range(0,len(compound)):
		if compound[i].isupper():
			counter += 1
	return counter

def divideByElements(compound):
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
