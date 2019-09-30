import Media_temporal
import histograma
import SAX
import SAX_complete
import openpyxl


wb = openpyxl.load_workbook('Datos_parseados_mantenidos.xlsx', data_only=True)
sheet_ranges = wb['Sheet1']

humor = []
apetito = []
sueno = []
cognitivos = []
termicos = []
otros = []
gastrointestinales = []
cronologia = []
count = -1
count_real = 0

columnas = { 'A': humor, 'B': apetito, 'C': sueno, 'D' : cognitivos, 'E' : termicos, 'F' : gastrointestinales, 'G' : otros}


print("MEDIA HUMOR")
humor = SAX_complete.SAX_global_mantenido(7, 'humor', 3)

print("MEDIA APETITO")
apetito = SAX_complete.SAX_global_mantenido(4, 'apetito', 3)

print("MEDIA SUENO")
sueno = SAX_complete.SAX_global_mantenido(2, 'sueno', 2)

print("MEDIA COGNITIVOS")
cognitivos = SAX_complete.SAX_global_mantenido(3, 'cognitivos', 3)

print("MEDIA TERMICOS")
termicos = SAX_complete.SAX_global_mantenido(2, 'termicos', 2)

print("MEDIA OTROS")
otros = SAX_complete.SAX_global_mantenido(12, 'otros', 3)

print("MEDIA GASTROINTESTINALES")
gastrointestinales = SAX_complete.SAX_global_mantenido(5, 'gastrointestinales', 3)
print gastrointestinales


#Estas lineas sirven para meter los datos en la hoja de excel
seleccion = sheet_ranges['A13':'G242']
for row in seleccion:
	count = count + 1
	for cell in row:
		if count == 229:
			break
		else:
			if (cell.column == 'A'):
				cell.value = humor[count]
			elif (cell.column == 'B'):
				cell.value = apetito[count]
			elif (cell.column == 'C'):
				cell.value = sueno[count]
			elif (cell.column == 'D'):
				cell.value = cognitivos[count]
			elif (cell.column == 'E'):
				cell.value = termicos[count]
			elif (cell.column == 'F'):
				cell.value = gastrointestinales[count]
			else:
				cell.value = otros[count]


wb.save("Datos_parseados_mantenidos.xlsx")
