import numpy as np

def Ordenar_vectores(startX, startY, endX, endY):
	#ejemplo para 5 personas
	"""startX = np.random.randint(256,size=5)
	startY = np.random.randint(256,size=5)
	endX = np.random.randint(256,size=5)
	endY = np.random.randint(256,size=5)"""

	orden =([])
	startX_sorted = np.sort(startX)
	startY_sorted =([])
	endX_sorted =([])
	endY_sorted =([])

	for i in range(0,len(startX)):
		
		print np.where(startX_sorted[i] == startX)[0][0]
		valor = np.where(startX_sorted[i] == startX)[0][0]
		orden.append(valor) 		

	#hay que ordenar startY,endX y endY de acuerdo a los indices del array 'orden'

	for j in range(0,len(startX)):
		print "---------"	
		print orden[j]
		startY_sorted.append(startY[orden[j]])
		endX_sorted.append(endX[orden[j]])
		endY_sorted.append(endY[orden[j]])


	"""print "Puntos iniciales: "
	print startX
	print startY
	print endX
	print endY
	print 
	print "Puntos ordenados de izquierda a derecha: "
	print startX_sorted
	print startY_sorted
	print endX_sorted
	print endY_sorted"""
	return startX_sorted, startY_sorted, endX_sorted, endY_sorted

