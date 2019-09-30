import numpy as np

def nuevo_tamano (startX, startY, endX, endY, ID):

	resta1 = (startX[ID] - endX[ID]) ** 2 
	resta2 = (startY[ID] - endY[ID]) ** 2
	valor = (resta1 + resta2) ** 0.5
	nuevo_tamano = np.round(valor,3)

return nuevo_tamano
