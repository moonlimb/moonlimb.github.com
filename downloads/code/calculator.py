#Name: Lisa and Moon
#Exercise07 (10/3/2012)

""" Calculator function is a basic pre-fix calculator for no more than two values. 
The calculator prints the result of the input. The calculator ends when the user types
'q'.
"""

import arithmetic as math

result = 0 

while True:
	calc_input = raw_input()
	token = calc_input.split(" ")

	if len(token) == 1:
		if token[0] == 'q':
			break
		elif token[0] == "cube":
			result = math.cube(result)
		elif token[0] == "square":
			result = math.square(result)
		
	elif len(token) == 2:
		try:
			token[1] = int(token[1])
		except ValueError:
			print "Please enter a valid expression."	
			continue
		if token[0] == "square":
			result= math.square(token[1])
		elif token[0] == "cube":
			result= math.cube(token[1])
		elif token[0] == "+":
			result = math.add(result,token[1])
		elif token[0] == "-":
			result = math.subtract(result,token[1])
		elif token[0] == "*":
			result = math.multiply(result,token[1])
		elif token[0] == "/":
			result = math.divide(result,token[1])
		elif token[0] == "pow":
			result = math.power(result,token[1])
		elif token[0] == "mod":
			result = math.mod(result,token[1])
		else:
			print "Please enter a valid expression."
	else:
		try:
			token[1] = int(token[1])
			token[2] = int(token[2])
		except ValueError:
			print "Please enter a valid expression."
			continue
		if token[0] == "+":
			result = math.add(token[1],token[2])
		elif token[0] == "-":
			result = math.subtract(token[1],token[2])
		elif token[0] == "*":
			result = math.multiply(token[1],token[2])
		elif token[0] == "/":
			result = math.divide(token[1],token[2])
		elif token[0] == "pow":
			result = math.power(token[1],token[2])
		elif token[0] == "mod":
			result = math.mod(token[1],token[2])
		else:
			print "Please enter a valid expression."
	print result
