"""
Created on Fri Mar 17 08:48:31 2023

@author: Gadiel Jimenez
"""
#100 a 120
#18 a 45

edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad >= 18 and edad <= 45:
	print('Eres menor de edad.')
elif edad >= 100 and edad <= 120:
	print('Eres mayor de edad.')
else:
	print('Edad no válida.')