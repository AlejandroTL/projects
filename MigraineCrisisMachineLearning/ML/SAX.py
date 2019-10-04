

def sticky_SAX (data, data1, data2, data3, double_array, caracteres):

	area = len(data)
	study_area = area / caracteres
	"""print(study_area)"""
	
	data_real = [[0] * 0 for i in range(0,area)]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = -1
	"""menos uno para que empiece el while en cero"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	"""print(division1_is)"""

	"""este for pilla los datos de las ventanas temporales y los mete en un mismo array"""
	for k in range (0, area):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		"""print(data_real[k])"""

	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, area):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			else: 
				data_real[j][h] = 'b'

	for j in range(0, area):		
			chain = data_real[j][0] + data_real[j][1] + data_real[j][2] + data_real[j][3] 		
			data_chain.append(chain)

	#print(data_chain)
	return(data_chain)

#-------------------------------------------------

def sticky_SAX3 (data, data1, data2, data3, double_array, caracteres):

	"""Calculo area sin columna de cero en histograma"""

	#print double_array

	area = 0
	for i in range (1, len(double_array[0])):
		area = area + double_array[1][i]
	
	study_area = area / caracteres
	#print(area)
	#print study_area
	
	longitud = len(data)
	data_real = [[0] * 0 for i in range(0,len(data))]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = 0
	"""cero para que empiece el while en uno"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	#print(division1_is)
	#print i
	#print len(double_array[1])
	j = i 

	while(check_b > 0):
		j = j + 1
		#print j
		check_b = check_b - double_array[1][j]
		if j == len(double_array[1])-1:
			break

	if j != (len(double_array[1])-1):
		division2_is = double_array[0][j]
	else:
		division2_is = double_array[0][1]
	#print(division2_is)


	#este for pilla los datos de las ventanas temporales y los mete en un mismo array
	for k in range (0, longitud):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		"""print(data_real[k])"""
	
	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, longitud):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			elif (data_real[j][h] >= division1_is) and (data_real[j][h] < division2_is): 
				data_real[j][h] = 'b'
			else:
				data_real[j][h] = 'c'
	"""print(data_real[j])"""
			
	for j in range(0, longitud):
			chain = data_real[j][0] + data_real[j][1] + data_real[j][2] + data_real[j][3] 		
			data_chain.append(chain)

	#print(data_real[j])
	#print(data_chain)
	return(data_chain)

#-------------------------------------------------

def sticky_very_SAX3 (data, data1, data2, data3, double_array, caracteres):

	"""Calculo area sin columna de cero en histograma"""

	#print double_array

	area = 0
	for i in range (1, len(double_array[0])):
		area = area + double_array[1][i]
	
	study_area = area / caracteres
	#print(area)
	#print study_area
	
	longitud = len(data)
	data_real = [[0] * 0 for i in range(0,len(data))]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = 0
	"""cero para que empiece el while en uno"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	#print division1_is

	#este for pilla los datos de las ventanas temporales y los mete en un mismo array
	for k in range (0, longitud):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		#print(data_real[k])
	
	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, longitud):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			elif (data_real[j][h] == division1_is): 
				data_real[j][h] = 'b'
			elif (data_real[j][h] > division1_is):
				data_real[j][h] = 'c'
		#print(data_real[j])
			
	for j in range(0, longitud):
			chain = data_real[j][0] + data_real[j][1] + data_real[j][2] + data_real[j][3] 		
			data_chain.append(chain)

	#print(data_real[j])
	#print(data_chain)
	return(data_chain)

#-------------------------------------------------

def sticky_SAX3_chronology (data, data1, data2, data3, double_array, caracteres):

	"""Calculo area sin columna de cero en histograma"""
	area = 0
	for i in range (1, len(double_array[0])):
		area = area + double_array[1][i]
	
	study_area = area / caracteres
	#print(area)
	
	longitud = len(data)
	data_real = [[0] * 0 for i in range(0,len(data))]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = 0
	"""cero para que empiece el while en uno"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	"""print(division1_is)"""
	j = i 

	while(check_b > 0):
		j = j + 1
		check_b = check_b - double_array[1][j]

	division2_is = double_array[0][j]
	"""print(division2_is)"""


	"""este for pilla los datos de las ventanas temporales y los mete en un mismo array"""
	for k in range (0, longitud):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		"""print(data_real[k])"""
	
	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, longitud):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			elif (data_real[j][h] >= division1_is) and (data_real[j][h] < division2_is): 
				data_real[j][h] = 'b'
			else:
				data_real[j][h] = 'c'

	#print(data_real)
	return(data_real)

#-------------------------------------------------

def cronologia (humor, apetito, sueno, cognitivos, termicos, gastrointestinales, otros):
	"""Los inputs de esta funcion son los arrays de dos dimensiones
	donde se guardan los datos ya tratados como caracteres de las diferentes ventanas temporales"""
	
	longitud = len(humor)
	#print(humor)
	
	count = 0
	data_real = [[0] * 0 for i in range(0,longitud)]
	data_chain = []	

	
	for j in range(0, longitud):	
		for h in range(0,4):
			chain = humor[j][count] + apetito[j][count] + sueno[j][count] + cognitivos[j][count] + termicos[j][count] + gastrointestinales[j][count] + otros[j][count]	
			data_real[j].append(chain)
			if count != 3:
				count = count + 1
			else:
				count = 0
		print(data_real[j])

	"""for j in range(0, longitud):
		chain = data_real[j][0] + '-' + data_real[j][1] + '-' + data_real[j][2] + '-' + data_real[j][3] 		
		data_chain.append(chain)"""
	
	
	return(data_real)

#-------------------------------------------------

def sticky_SAX_chronology (data, data1, data2, data3, double_array, caracteres):

	area = len(data)
	study_area = area / caracteres
	#print(study_area)
	
	data_real = [[0] * 0 for i in range(0,area)]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = -1
	"""menos uno para que empiece el while en cero"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	"""print(division1_is)"""

	"""este for pilla los datos de las 4 temporales y los mete en un mismo array"""
	for k in range (0, area):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		"""print(data_real[k])"""

	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, area):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			else: 
				data_real[j][h] = 'b'
	#print(data_real)
	return(data_real)

#-------------------------------------------

#Funcion para recodificar el SAX a numeros
#Ventana 3 es de 0 a 6
#Ventana 0 es de 24 a 72

def SAX_recodification3 (data, data1, data2, data3, double_array, caracteres, ventana):

	"""Calculo area sin columna de cero en histograma"""

	#print double_array

	area = 0
	for i in range (1, len(double_array[0])):
		area = area + double_array[1][i]
	
	study_area = area / caracteres
	#print(area)
	#print study_area
	
	longitud = len(data)
	data_real = [[0] * 0 for i in range(0,len(data))]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = 0
	"""cero para que empiece el while en uno"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	#print(division1_is)
	#print i
	#print len(double_array[1])
	j = i 

	while(check_b > 0):
		j = j + 1
		print j
		check_b = check_b - double_array[1][j]
		if j == len(double_array[1])-1:
			break

	if j != (len(double_array[1])-1):
		division2_is = double_array[0][j]
	else:
		division2_is = double_array[0][1]
	#print(division2_is)


	#este for pilla los datos de las ventanas temporales y los mete en un mismo array
	for k in range (0, longitud):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		"""print(data_real[k])"""
	
	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, longitud):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			elif (data_real[j][h] >= division1_is) and (data_real[j][h] < division2_is): 
				data_real[j][h] = 'b'
			else:
				data_real[j][h] = 'c'
	print(data_real)
			
	
	for j in range(0, longitud):
		number = 0
		#for h in range(0,4):
		if data_real[j][ventana] == 'a':
			number = number
		if data_real[j][ventana] == 'b':
			number = number + 1
		if data_real[j][ventana] == 'c':
			number = number + 2
		print number, j
		data_chain.append(number)
	print data_chain

	"""for j in range(0, longitud):
			chain = data_real[j][0] + data_real[j][1] + data_real[j][2] + data_real[j][3] 		
			data_chain.append(chain)"""

	#print(data_real[j])
	#print(data_chain)
	return(data_chain)

#---------------------


def SAX_recodification (data, data1, data2, data3, double_array, caracteres, ventana):

	area = len(data)
	study_area = area / caracteres
	"""print(study_area)"""
	
	data_real = [[0] * 0 for i in range(0,area)]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = -1
	"""menos uno para que empiece el while en cero"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	"""print(division1_is)"""

	"""este for pilla los datos de las ventanas temporales y los mete en un mismo array"""
	for k in range (0, area):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		"""print(data_real[k])"""

	"""este for crea la cadena de caracteres, usamos 0 a ventana porque hay ventana ventanas temporales"""
	for j in range(0, area):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			else: 
				data_real[j][h] = 'b'


	for j in range(0, area):
		number = 0
		#for h in range(0,4):
		if data_real[j][ventana] == 'a':
			number = number
		if data_real[j][ventana] == 'b':
			number = number + 1
		data_chain.append(number)
	"""for j in range(0, area):		
			chain = data_real[j][0] + data_real[j][1] + data_real[j][2] + data_real[j][3] 		
			data_chain.append(chain)"""

	#print(data_chain)
	return(data_chain)


#-------------------------------------------------

def SAX_very_recodification (data, data1, data2, data3, double_array, caracteres, ventana):

	"""Calculo area sin columna de cero en histograma"""

	#print double_array

	area = 0
	for i in range (1, len(double_array[0])):
		area = area + double_array[1][i]
	
	study_area = area / caracteres
	#print(area)
	#print study_area
	
	longitud = len(data)
	data_real = [[0] * 0 for i in range(0,len(data))]
	data_chain = []
	check_a = study_area
	check_b = study_area
	i = 0
	"""cero para que empiece el while en uno"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	#print division1_is

	#este for pilla los datos de las ventanas temporales y los mete en un mismo array
	for k in range (0, longitud):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		#print(data_real[k])
	
	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, longitud):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			elif (data_real[j][h] == division1_is): 
				data_real[j][h] = 'b'
			elif (data_real[j][h] > division1_is):
				data_real[j][h] = 'c'
		#print ("pintar")
		#print(data_real[j])
	print data_real
			
	for j in range(0, longitud):
		number = 0
		#for h in range(0,4):
		if data_real[j][ventana] == 'a':
			number = number
		if data_real[j][ventana] == 'b':
			number = number + 1
		if data_real[j][ventana] == 'c':
			number = number + 2
		print number, j
		data_chain.append(number)
	#print data_chain
	
	#print len(data_chain)
	"""for j in range(0, longitud):
			chain = data_real[j][0] + data_real[j][1] + data_real[j][2] + data_real[j][3] 		
			data_chain.append(chain)"""

	#print(data_real[j])
	#print(data_chain)
	return(data_chain)


#------------------------------
#Funcion para el calculo de la media por ventanas temporales cronologicas. Para el SOM

def SOM_cronologia (humor, apetito, sueno, cognitivos, termicos, gastrointestinales, otros, ventana):
	"""Los inputs de esta funcion son los arrays de dos dimensiones
	donde se guardan los datos ya tratados como caracteres de las diferentes ventanas temporales"""
	
	longitud = len(humor) #para saber cual es la longitud de los datos, miramos la longitud de cualquiera de los de entrada
	#print(humor)
	
	count = 0
	data_real = []
	data_chain = []	

	
	for j in range(0, longitud):	
		if humor[j][ventana] == 'a':
			number = number
		elif humor[j][ventana] == 'b':
			number = number + 1
		elif humor[j][ventana] == 'c':
			number = number + 2

		if apetito[j][ventana] == 'a':
			number = number
		elif apetito[j][ventana] == 'b':
			number = number + 1
		elif apetito[j][ventana] == 'c':
			number = number + 2

		if sueno[j][ventana] == 'a':
			number = number
		elif sueno[j][ventana] == 'b':
			number = number + 1
		elif sueno[j][ventana] == 'c':
			number = number + 2

		if cognitivos[j][ventana] == 'a':
			number = number
		elif cognitivos[j][ventana] == 'b':
			number = number + 1
		elif cognitivos[j][ventana] == 'c':
			number = number + 2

		if termicos[j][ventana] == 'a':
			number = number
		elif termicos[j][ventana] == 'b':
			number = number + 1
		elif termicos[j][ventana] == 'c':
			number = number + 2

		if gastrointestinales[j][ventana] == 'a':
			number = number
		elif gastrointestinales[j][ventana] == 'b':
			number = number + 1
		elif gastrointestinales[j][ventana] == 'c':
			number = number + 2

		if otros[j][ventana] == 'a':
			number = number
		elif otros[j][ventana] == 'b':
			number = number + 1
		elif otros[j][ventana] == 'c':
			number = number + 2
				
		data_real[j] = number
		#print(data_real[j])

	"""for j in range(0, longitud):
		chain = data_real[j][0] + '-' + data_real[j][1] + '-' + data_real[j][2] + '-' + data_real[j][3] 		
		data_chain.append(chain)"""
	
	#print(data_real)
	return(data_real)

