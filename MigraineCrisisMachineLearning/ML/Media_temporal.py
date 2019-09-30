import openpyxl
from decimal import Decimal
"""from openpyxl import Workbook"""
"""print("Hola holita")"""

wb = openpyxl.load_workbook('tiempos.xlsx', data_only=True)
sheet_ranges = wb['tiempos']
"""print(sheet_ranges['K4'].value)"""

def media_temporal (celda_inicio, celda_limite, hora_inicio, hora_final, parametros, tipo):

	suma = 0
	valor_limite0 = hora_inicio*60
	valor_limite1 = hora_final*60
	data = []

	if (tipo == 'humor' or tipo == 'Humor'):
		tipo_inicio = 'B'
		tipo_final = 'G'
	elif (tipo == 'apetito' or tipo == 'Apetito'):
		tipo_inicio = 'H'
		tipo_final = 'K'
	elif (tipo == 'sueno' or tipo == 'Sueno'):
		tipo_inicio = 'L'
		tipo_final = 'M'
	elif (tipo == 'cognitivos' or tipo == 'Cognitivos'):
		tipo_inicio = 'N'
		tipo_final = 'P'
	elif (tipo == 'termicos' or tipo == 'Termicos'):
		tipo_inicio = 'Q'
		tipo_final = 'R'
	elif (tipo == 'gastrointestionales' or tipo == 'Gastrointestinales'):
		tipo_inicio = 'S'
		tipo_final = 'W'
	elif (tipo == 'otros' or tipo == 'Otros'):
		tipo_inicio = 'X'
		tipo_final = 'AI'

	for row in range(celda_inicio, celda_limite):
	
		celda1 = tipo_inicio + str(row)
		celda2 = tipo_final + str(row)

		seleccion = sheet_ranges[celda1:celda2]
		for row in seleccion:
			for cell in row:
				if (cell.value != "-" and cell.value <= valor_limite1 and cell.value >= valor_limite0):
					suma = suma + 1

		media_ventana = float(suma)/float(parametros)
		real = round(media_ventana, 5)
		suma = 0
		media_ventana = 0		
		"""print(real)"""
		data.append(real)

	#print(data)
	return(data)


def media_temporal_ponderada (celda_inicio, celda_limite, hora_inicio, hora_final, parametros, tipo):

	suma = 0
	valor_limite0 = hora_inicio*60
	valor_limite1 = hora_final*60
	data = []

	if (tipo == 'humor' or tipo == 'Humor'):
		tipo_inicio = 'B'
		tipo_final = 'G'
	elif (tipo == 'apetito' or tipo == 'Apetito'):
		tipo_inicio = 'H'
		tipo_final = 'K'
	elif (tipo == 'sueno' or tipo == 'Sueno'):
		tipo_inicio = 'L'
		tipo_final = 'M'
	elif (tipo == 'cognitivos' or tipo == 'Cognitivos'):
		tipo_inicio = 'N'
		tipo_final = 'P'
	elif (tipo == 'termicos' or tipo == 'Termicos'):
		tipo_inicio = 'Q'
		tipo_final = 'R'
	elif (tipo == 'gastrointestinales' or tipo == 'Gastrointestinales'):
		tipo_inicio = 'S'
		tipo_final = 'W'
	elif (tipo == 'otros' or tipo == 'Otros'):
		tipo_inicio = 'X'
		tipo_final = 'AI'

	for row in range(celda_inicio, celda_limite):
	
		celda1 = tipo_inicio + str(row)
		celda2 = tipo_final + str(row)

		seleccion = sheet_ranges[celda1:celda2]
		for row in seleccion:
			for cell in row:
				if (cell.value != "-" and cell.value <= valor_limite1 and cell.value >= valor_limite0):
					if (cell.column == 'H') or (cell.column == 'I') or (cell.column == 'L') or (cell.column == 'M') or (cell.column == 'Q') or (cell.column== 'R'):
						suma = suma + 2
					else:
						suma = suma + 1

		media_ventana = float(suma)/float(parametros)
		real = round(media_ventana, 5)
		suma = 0
		media_ventana = 0		
		"""print(real)"""
		data.append(real)

	#print(data)
	return(data)

"""
media_temporal(3, 39, 200, 7, 'sueno')
print("CAMBIO")
media_temporal(3, 39, 200, 7, 'humor')"""


