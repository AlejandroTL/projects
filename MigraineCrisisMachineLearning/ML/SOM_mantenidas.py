import Media_temporal
import histograma
import SAX
import SAX_complete
import openpyxl


wb = openpyxl.load_workbook('Medias_SOM_mantenidas.xlsx', data_only=True)
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
humor = Media_temporal.media_temporal_ponderada(3, 232, 0, 72, 7, 'humor')

print("MEDIA APETITO")
apetito = Media_temporal.media_temporal_ponderada(3, 232, 0, 72, 4, 'apetito')

print("MEDIA SUENO")
sueno = Media_temporal.media_temporal_ponderada(3, 232, 0, 72, 2, 'sueno')

print("MEDIA COGNITIVOS")
cognitivos = Media_temporal.media_temporal_ponderada(3, 232, 0, 72, 3, 'cognitivos')

print("MEDIA TERMICOS")
termicos = Media_temporal.media_temporal_ponderada(3, 232, 0, 72, 2, 'termicos')

print("MEDIA OTROS")
otros = Media_temporal.media_temporal_ponderada(3, 232, 0, 72, 12, 'otros')

print("MEDIA GASTROINTESTINALES")
gastrointestinales = Media_temporal.media_temporal_ponderada(3, 232, 0, 72, 5, 'gastrointestinales')


#Estas lineas sirven para meter los datos en la hoja de excel
seleccion = sheet_ranges['A1':'G230']
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


wb.save("Medias_SOM_mantenidas.xlsx")
	

