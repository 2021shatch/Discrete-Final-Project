poly = []
  

p = int(input("Enter number of coefficients : "))
  
=
for i in range(0, p):
    ele = int(input('Please enter the coefficients of the polynomial from greatest to least degree: '))
  
    poly.append(ele) # adding the element


x = input('Enter value for x: ')
n = len(poly)

def horner(poly, n, x):


	result = poly[0]

	
	for i in range(1, n):

		result = result*x + poly[i]

	return result



print("Value of polynomial is " , horner(poly, n, x))

