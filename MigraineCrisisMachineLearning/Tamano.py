import numpy as np

def calculo_tamano(startX, startY, endX, endY, tamano_anterior):
	"""startX = np.random.randint(256,size=5)
	startY = np.random.randint(256,size=5)
	endX = np.random.randint(256,size=5)
	endY = np.random.randint(256,size=5)
	distancia = 0.24"""
	restas = []
	restas_ok = []

	print startX, startY, endX, endY

	result = []
	result_sorted = []

	for i in range(0, len(startX)):
		resta1 = (endX[i] - startX[i]) ** 2 
		resta2 = (endY[i] - startY[i]) ** 2
		valor = (resta1 + resta2) ** 0.5
		valor = np.round(valor,3)
		result.append(valor)

	result_ordenado = np.sort(result)

	print result

	mayor = result_ordenado[len(result)-1]

	print mayor

	result_ok = result / mayor

	print result_ok

	for h in range (0, len(result)):
		value = abs((result_ok[h])-tamano_anterior)
		restas.append(value)

	print "RESTAS", restas

	restas_ok = np.sort(restas)

	igual = restas_ok[0]
	igual2 = restas_ok[1]
	print "IGUAL", igual

	bounding_box_ID = np.where(restas == igual)[0][0]
	bounding_box_ID2 = np.where(restas == igual2)[0][0]

	print bounding_box_ID, bounding_box_ID2


def nuevo_tamano (startX, startY, endX, endY, ID):

	if len(startX) > 0:
		resta1 = (startX[ID] - endX[ID]) ** 2 
		resta2 = (startY[ID] - endY[ID]) ** 2
		valor = (resta1 + resta2) ** 0.5
		nuevo_tamano = np.round(valor,3)

		return nuevo_tamano
	else:
		return None
		
