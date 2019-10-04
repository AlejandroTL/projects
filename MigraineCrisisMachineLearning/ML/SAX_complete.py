import Media_temporal
import histograma
import SAX

#--------------------------
#Funcion que saca las cadenas de caracteres de cada tipo en ventanas temporales 

def SAX_global (numero_atributos, nombre_tipo, numero_caracteres):
	
	hystogram = Media_temporal.media_temporal_ponderada(3, 232, 0, 200, numero_atributos, nombre_tipo)
	datos= Media_temporal.media_temporal_ponderada(3, 232, 0, 6, numero_atributos, nombre_tipo)
	array=histograma.histograma(hystogram)
	datos1 = Media_temporal.media_temporal_ponderada(3, 232, 6, 12, numero_atributos, nombre_tipo)
	datos2 = Media_temporal.media_temporal_ponderada(3, 232, 12, 24, numero_atributos, nombre_tipo)
	datos3 = Media_temporal.media_temporal_ponderada(3, 232, 24, 72, numero_atributos, nombre_tipo)
	
	if (numero_caracteres == 3):
		if (nombre_tipo == 'gastrointestinales' or nombre_tipo == 'Gastrointestinales' or nombre_tipo == 'cognitivos' or nombre_tipo == 'Cognitivos'):
			print('HOLAAAA')
			cadena_de_caracteres = SAX.sticky_very_SAX3(datos3, datos2, datos1, datos, array, numero_caracteres)
		else:
			cadena_de_caracteres = SAX.sticky_SAX3(datos3, datos2, datos1, datos, array, numero_caracteres)
	else:
		cadena_de_caracteres = SAX.sticky_SAX(datos3, datos2, datos1, datos, array, numero_caracteres)

	return(cadena_de_caracteres)

#--------------------------
#Funcion que saca el estado cronologico del paciente en ventanas temporales

def SAX_global_chronology (numero_atributos, nombre_tipo, numero_caracteres):
	
	hystogram = Media_temporal.media_temporal_ponderada(3, 232, 0, 200, numero_atributos, nombre_tipo)
	datos= Media_temporal.media_temporal_ponderada(3, 232, 0, 6, numero_atributos, nombre_tipo)
	array=histograma.histograma(hystogram)
	datos1 = Media_temporal.media_temporal_ponderada(3, 232, 6, 12, numero_atributos, nombre_tipo)
	datos2 = Media_temporal.media_temporal_ponderada(3, 232, 12, 24, numero_atributos, nombre_tipo)
	datos3 = Media_temporal.media_temporal_ponderada(3, 232, 24, 72, numero_atributos, nombre_tipo)
	
	#print datos
	if nombre_tipo == 'otros':
		print numero_caracteres

	if (numero_caracteres == 3):
		if (nombre_tipo == 'gastrointestinales' or nombre_tipo == 'Gastrointestinales' or nombre_tipo == 'cognitivos' or nombre_tipo == 'Cognitivos'):
			print('VERY')
			cadena_de_caracteres = SAX.sticky_SAX_chronology(datos3, datos2, datos1, datos, array, numero_caracteres)

		else:
			print('NOT')
			cadena_de_caracteres = SAX.sticky_SAX_chronology(datos3, datos2, datos1, datos, array, numero_caracteres)
			print cadena_de_caracteres
	else:
		print('NORMAL')
		cadena_de_caracteres = SAX.sticky_SAX_chronology(datos3, datos2, datos1, datos, array, numero_caracteres)

	return(cadena_de_caracteres)

#--------------------------
#Funcion que saca las cadenas de caracteres de cada tipo en ventanas temporales7
#DARLE UN OJO A ESTO, CREO QUE ES MEJOR 0-72, 6-72, 12-72 y 24-72

def SAX_global_mantenido (numero_atributos, nombre_tipo, numero_caracteres):
	
	hystogram = Media_temporal.media_temporal_ponderada(3, 232, 0, 200, numero_atributos, nombre_tipo)
	datos= Media_temporal.media_temporal_ponderada(3, 232, 0, 72, numero_atributos, nombre_tipo)
	array=histograma.histograma(hystogram)
	datos1 = Media_temporal.media_temporal_ponderada(3, 232, 6, 72, numero_atributos, nombre_tipo)
	datos2 = Media_temporal.media_temporal_ponderada(3, 232, 12, 72, numero_atributos, nombre_tipo)
	datos3 = Media_temporal.media_temporal_ponderada(3, 232, 24, 72, numero_atributos, nombre_tipo)
	
	if (numero_caracteres == 3):
		if (nombre_tipo == 'gastrointestinales' or nombre_tipo == 'Gastrointestinales' or nombre_tipo == 'cognitivos' or nombre_tipo == 'Cognitivos'):
			print('HOLAAAA')
			cadena_de_caracteres = SAX.sticky_very_SAX3(datos3, datos2, datos1, datos, array, numero_caracteres)
		else:
			cadena_de_caracteres = SAX.sticky_SAX3(datos3, datos2, datos1, datos, array, numero_caracteres)
	else:
		cadena_de_caracteres = SAX.sticky_SAX(datos3, datos2, datos1, datos, array, numero_caracteres)

	return(cadena_de_caracteres)

#--------------------------
#Funcion que saca el estado cronologico del paciente SIN ventanas temporales

def SAX_global_chronology_mantenido (numero_atributos, nombre_tipo, numero_caracteres):
	
	hystogram = Media_temporal.media_temporal_ponderada(3, 232, 0, 200, numero_atributos, nombre_tipo)
	datos= Media_temporal.media_temporal_ponderada(3, 232, 0, 72, numero_atributos, nombre_tipo)
	array=histograma.histograma(hystogram)
	datos1 = Media_temporal.media_temporal_ponderada(3, 232, 6, 72, numero_atributos, nombre_tipo)
	datos2 = Media_temporal.media_temporal_ponderada(3, 232, 12, 72, numero_atributos, nombre_tipo)
	datos3 = Media_temporal.media_temporal_ponderada(3, 232, 24, 72, numero_atributos, nombre_tipo)
	
	if (numero_caracteres == 3):
		if (nombre_tipo == 'gastrointestinales' or nombre_tipo == 'Gastrointestinales' or nombre_tipo == 'cognitivos' or nombre_tipo == 'Cognitivos'):
			print('HOLAAAA')
			cadena_de_caracteres = SAX.sticky_SAX_chronology(datos3, datos2, datos1, datos, array, numero_caracteres)
		else:
			cadena_de_caracteres = SAX.sticky_SAX_chronology(datos3, datos2, datos1, datos, array, numero_caracteres)
	else:
		cadena_de_caracteres = SAX.sticky_SAX_chronology(datos3, datos2, datos1, datos, array, numero_caracteres)

	return(cadena_de_caracteres)

#--------------------------------
#Funcion que RECODIFICA desde SAX

def SAX_recodificated (numero_atributos, nombre_tipo, numero_caracteres, ventana):
	
	hystogram = Media_temporal.media_temporal_ponderada(3, 232, 0, 200, numero_atributos, nombre_tipo)
	datos= Media_temporal.media_temporal_ponderada(3, 232, 0, 72, numero_atributos, nombre_tipo)
	array=histograma.histograma(hystogram)
	datos1 = Media_temporal.media_temporal_ponderada(3, 232, 6, 72, numero_atributos, nombre_tipo)
	datos2 = Media_temporal.media_temporal_ponderada(3, 232, 12, 72, numero_atributos, nombre_tipo)
	datos3 = Media_temporal.media_temporal_ponderada(3, 232, 24, 72, numero_atributos, nombre_tipo)
	
	if (numero_caracteres == 3):
		if (nombre_tipo == 'gastrointestinales' or nombre_tipo == 'Gastrointestinales' or nombre_tipo == 'cognitivos' or nombre_tipo == 'Cognitivos'):
			print('HOLAAAA')
			cadena_de_caracteres = SAX.SAX_very_recodification(datos3, datos2, datos1, datos, array, numero_caracteres, ventana)
		else:
			cadena_de_caracteres = SAX.SAX_recodification3(datos3, datos2, datos1, datos, array, numero_caracteres, ventana)
	else:
		cadena_de_caracteres = SAX.SAX_recodification(datos3, datos2, datos1, datos, array, numero_caracteres, ventana)

	return(cadena_de_caracteres)

#--------------------------
