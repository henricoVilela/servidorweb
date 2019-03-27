import datetime

#Compara as datas, return TRUE: Precisa att e FALSE: nao att
def compara_data(data_at_mod,data_if_mod):
	dia = 1
	mes = 2
	ano = 3
	# print(data_if_mod)
	# print(data_at_mod)
	data_at_mod[len(data_at_mod) - 1] = data_at_mod[len(data_at_mod) - 1].split(":")
	hora_at = data_at_mod[len(data_at_mod) - 1]
	
	data_if_mod[len(data_if_mod) - 2] = data_if_mod[len(data_if_mod) - 2].split(":")
	hora_if = data_if_mod[len(data_if_mod) - 2]
	
	# print(data_if_mod)
	# print(data_at_mod)

	if(int(data_at_mod[ano]) > int(data_if_mod[ano])):
		return True
	else:
		if(return_month(data_at_mod[mes]) > return_month(data_if_mod[mes])):
			return True
		else:
			if(int(data_at_mod[dia]) > int(data_if_mod[dia])):
				return True
			else:
				if(int(hora_at[0]) > int(hora_if[0])):
					return True
				else:
					if(int(hora_at[1]) > int(hora_if[1])):
						return True
					else:
						if(int(hora_at[2]) > int(hora_if[2])):
							return True
						else:
							return False

#retorna os numeros de acordo com o nome do mes
def return_month(name_month):
	if(name_month == "Jan"):
		return 1
	elif(name_month == "Feb"):
		return 2
	elif(name_month) == "Mar":
		return 3
	elif(name_month) == "Apr":
		return 4
	elif(name_month) == "May":
		return 5
	elif(name_month) == "Jun":
		return 6
	elif (name_month) == "Jul":
		return 7
	elif (name_month) == "Aug":
		return 8
	elif (name_month) == "Sep":
		return 9
	elif (name_month) == "Oct":
		return 10
	elif (name_month) == "Nov":
		return 11
	elif (name_month) == "Dec":
		return 12

#abrevia os nomes para enviar ao cliente
def abrevia(data):
	mod = str(data)
	m = mod.split()
	aux = m[0]
	m[0] = aux[:3] + ","
	aux = m[2]
	m[2] = aux[:3]
	dat = " ".join(m)
	return dat

#pega a data atual
def getData():
	dt = datetime.datetime.now()
	date = dt.strftime("%A, %d %B %Y %H:%M:%S")
	at = abrevia(date)
	return at