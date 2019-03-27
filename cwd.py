# encoding: utf-8
import os
lis_aux = []



def busca_caminho(parm):
	global lis_aux
	a = parm.split(".")
	if(len(a) == 2):
		dirlist = os.listdir(parm)

		for i in dirlist:
			lis_aux.append(os.path.abspath(i))
	else:
		dirlist = os.listdir(parm)

		for i in dirlist:
			b = i.split('.')
			lis_aux.append(parm +"/"+ i)

	li = list(lis_aux)
	return li

#verifica se e diretorio ou arquivo
def verifica_tipo(lista):
	lis = []
	for i in range(len(lista)):
		a = lista[i].split(".")
		if(len(a)==1):
			lis.append(a[0])
	return lis

def lista_arquivos(n):
	global lis_aux
	l = busca_caminho(".")
	# print("l:"+str(l))
	i = 0
	aux = verifica_tipo(l)
	while i < len(aux):
		
		# print(str(aux) + "\n") 
		if(len(aux) > 0):
			tok = aux[i].split("/")
			l = busca_caminho(aux[i])
			# print("l"+str(i)+":"+str(l))

		i = i + 1
		aux = verifica_tipo(l)
		# print(len(lis_aux))


	resp = busca_por_nome(n)
	cwd = os.getcwd()
	if resp != False:
		resp = resp.replace(str(cwd),'')
	return resp

def busca_por_nome(nome):
	global lis_aux
	for i in range(len(lis_aux)):
		aux = lis_aux[i].split("/")
		if nome in lis_aux[i] and "/"+aux[len(aux) - 1] == nome :
			return lis_aux[i]
		elif nome.find("/") == 0:
			cw = os.getcwd()
			if lis_aux[i].replace(str(cw),"") == nome:
				return lis_aux[i]
	return False
	
# a = lista_arquivos("/ex.html")
# print a
