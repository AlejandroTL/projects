import scipy
import numpy
import random
from matplotlib.pylab import hist, show
def histograma (data):
	
	""" Creamos un array de dos dimensiones donde guardamos los valores que hay, y el numero de veces que sale"""
	data_set = set(data)
	data_set_sorted = sorted(data_set)
	n = len(data_set)
	a = [[0] * 0 for i in range(0,2)]
	for j in range(0, n):
		a[0].append(data_set_sorted[j])
		a[1].append(0)

	"""Hasta aqui, se ha creado un array de dos dimensiones en las que la primera dimension se corresponde con 
	los valores que va a haber de media, y estan ya metidos ahi. Ahora hace falta ver cuantas veces se repite cada uno"""

	data_real = sorted(data) 
	lowest = data_real[0]
	h = 0

	for i in range(0, len(data_real)): 
		if (data_real[i] == lowest):
			a[1][h] = a[1][h] + 1
		else :
			lowest = data_real[i]
			h = h + 1

	"""hist(data_real, n, (0,1))
	show()"""
	
	#print(a)
	return (a)

		
