

def sticky_SAX3 (data, data1, data2, data3, double_array, caracteres):

	"""Calculo area sin columna de cero en histograma"""
	for i in range (1, len(double_array) - 2):
		area = area + double_array[1][i]
	
	study_area = area / caracteres
	
	data_real = [[0] * 0 for i in range(0,area)]
	check_a = study_area
	check_b = study_area
	i = 0
	"""cero para que empiece el while en uno"""

	while(check_a > 0):
		i = i + 1
		check_a = check_a - double_array[1][i]

	division1_is = double_array[0][i]
	j = i 

	while(check_b > 0):
		j = j + 1
		check_b = check_b - double_array[1][j]

	division2_is = double_array[0][j]

	"""este for pilla los datos de las ventanas temporales y los mete en un mismo array"""
	for k in range (0, area):
		data_real[k] = [data[k],data1[k],data2[k],data3[k]]
		print(data_real[k])

	"""este for crea la cadena de caracteres, usamos 0 a 4 porque hay 4 ventanas temporales"""
	for j in range(0, area):
		for h in range(0, 4):
			if data_real[j][h] == 0:
				data_real[j][h] = 'a'
			elif (data_real[j][h] => division1_is) and (data_real[j][h] =< division1_is): 
				data_real[j][h] = 'b'
			else:
				data_real[j][h] = 'c'

		print(data_real[j])



