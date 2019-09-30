import numpy as np


def calculo_distancias(startX, startY, endX, endY, inicialX, inicialY, bounding_box_ID_SIZE, bounding_box_ID2_SIZE):
	startX = np.random.randint(256,size=5)
	startY = np.random.randint(256,size=5)
	endX = np.random.randint(256,size=5)
	endY = np.random.randint(256,size=5)
	bounding_box_ID_SIZE = 1
	bounding_box_ID2_SIZE= 4
	inicialX = 142
	inicialY = 25
	result = []
	print startX, startY, endX, endY

	puntos_mediosX = abs((startX - endX)) / 2
	puntos_mediosY = abs((startY - endY)) / 2

	print puntos_mediosX, puntos_mediosY
	BOUND_ID_SIZE=[bounding_box_ID_SIZE, bounding_box_ID2_SIZE]

	for i in range (0, len(BOUND_ID_SIZE)):
		resta1 = (inicialX - puntos_mediosX[BOUND_ID_SIZE[i]]) ** 2 
		resta2 = (inicialY - puntos_mediosY[BOUND_ID_SIZE[i]]) ** 2
		valor = (resta1 + resta2) ** 0.5
		valor = np.round(valor,3)
		result.append(valor)

	print result 

	result_ok = np.sort(result)

	igual = result_ok[0]

	bounding_box_ID = np.where(result == igual)[0][0]

	print bounding_box_ID

	return bounding_boxID, puntos_mediosX[bounding_box_ID], puntos_mediosY[bounding_box_ID]



def distancia_arriba(startY, endY, centroY):
	
	distancia1 = abs(startY - centroY)
	distancia2 = abs(endY - centroY)
	
	distancias = [distancia1, distancia2]
	distancias = np.sort(distancias)

	if distancias(0) >= 100:
		return true
	else:
		return false
	
	






