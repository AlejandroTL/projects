import Media_temporal
import histograma
import SAX
import SAX_complete
import openpyxl


wb = openpyxl.load_workbook('Datos_cronologia_mantenidos.xlsx', data_only=True)
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
humor = SAX_complete.SAX_global_chronology_mantenido(7, 'humor', 3)

print("MEDIA APETITO")
apetito = SAX_complete.SAX_global_chronology_mantenido(4, 'apetito', 3)

print("MEDIA SUENO")
sueno = SAX_complete.SAX_global_chronology_mantenido(2, 'sueno', 2)

print("MEDIA COGNITIVOS")
cognitivos = SAX_complete.SAX_global_chronology_mantenido(3, 'cognitivos', 3)

print("MEDIA TERMICOS")
termicos = SAX_complete.SAX_global_chronology_mantenido(2, 'termicos', 2)

print("MEDIA OTROS")
otros = SAX_complete.SAX_global_chronology_mantenido(12, 'otros', 3)

print("MEDIA GASTROINTESTINALES")
gastrointestinales = SAX_complete.SAX_global_chronology_mantenido(5, 'gastrointestinales', 3)

ver = SAX.cronologia (humor, apetito, sueno, cognitivos, termicos, gastrointestinales, otros)
print(ver)

seleccion = sheet_ranges['A9':'D238']
for row in seleccion:
	count = count + 1
	for cell in row:
		if count == 229:
			break
		else:
			if (cell.column == 'A'):
				cell.value = ver[count][0]
			elif (cell.column == 'B'):
				cell.value = ver[count][1]
			elif (cell.column == 'C'):
				cell.value = ver[count][2]
			elif (cell.column == 'D'):
				cell.value = ver[count][3]

wb.save("Datos_cronologia_mantenidos.xlsx")

