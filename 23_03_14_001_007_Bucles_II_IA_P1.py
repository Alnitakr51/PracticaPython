"""
Created on Fri Mar 17 08:48:31 2023

@author: Gadiel Jimenez
"""
x = 0

while x <= 30:
	x += 1

	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor', x, 'de x')
		continue

	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía:', x)
		break

	print(x)