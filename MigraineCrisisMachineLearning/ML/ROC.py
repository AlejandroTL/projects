
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

wb = openpyxl.load_workbook('ROC0.xlsx', data_only=True)
sheet_ranges = wb['ROC0']

celda1 = 'R19'
celda2 = 'R152'

celda3 = 'S19'
celda4 = 'S152'

fpr = []
tpr = []
suma = 0

seleccion = sheet_ranges[celda1:celda2]
seleccion2 = sheet_ranges[celda3:celda4]
for row in seleccion:
	for cell in row:
		"""print(cell.value)
		if cell.value != 100:
			suma = suma + 1
			print(suma)"""
		#print(isinstance(cell.value, float))
		dato = float(cell.value)
		fpr.append(dato)
		#print(dato)
		#print(fpr)

#print(fpr.shape)
print("DONE")
for row in seleccion2:
	for cell in row:
		"""print(cell.value)
		if cell.value != 100:
			suma = suma + 1
			print(suma)"""
		#print(isinstance(cell.value, float))
		dato2 = float(cell.value)
		tpr.append(dato2)
#print(tpr.shape)

roc_auc= auc(fpr, tpr)

plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--', label='Clasificación aleatoria' % roc_auc)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Curva ROC Clase 0')
plt.legend(loc="lower right")
plt.show()

