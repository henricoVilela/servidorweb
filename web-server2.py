# encoding: utf-8
import socket
import os, sys
import thread
import time
import datetime
from cwd import *
from response import *
from data import *


PORTA = 13000
#tread que gerencia as reposta 
def thread_con(socketConn, addr,nt):
	#socketConn.settimeout(5.0)
	#msg = recv_http(socketConn)
	flag = True
	socketConn.settimeout(5.0)
	soma = 0.0
	while flag:
		
		try:
			msg = recv_http(socketConn)
		except socket.timeout:
			break
		
		#print(nt)
		print(msg)
		camposMsg = msg.split()
		
		# Trata caso 1
		if camposMsg[0].upper() == "GET" or camposMsg[0].upper() == "HEAD":
			MODO = camposMsg[0].upper()
			resp = lista_arquivos(str(camposMsg[1]))
			# print(resp)
			if(resp != False and str(resp) == str(camposMsg[1])):
				# print(resp+"1")
				condicao = verifica_get_condicional(msg)
				ext = camposMsg[1].split('.')
				cwd = os.getcwd()
				caminho = str(cwd) + str(camposMsg[1])
				#print caminho
				try:
					mtime = datetime.datetime.fromtimestamp(os.path.getmtime(caminho))
				except os.error:
					continue
				dt = mtime.strftime("%A, %d %B %Y %H:%M:%S") #retorna a data da Ultima modificacao
				data_mod = abrevia(dt)
				data_atual = getData()
				print (data_atual,data_mod)
				filename = getFileName(camposMsg) # recupera o nome do arquivo
				if(condicao == "/f"):
					ok_200(socketConn,filename,ext,data_mod,data_atual,MODO)
				else:
						# print("aqui= "+str(condicao))
						if(compara_data(data_mod.split(), condicao)):
							ok_200(socketConn,filename,ext,data_mod,data_atual,MODO)
						else:
							not_modified_304(socketConn,data_atual,data_mod)
				#print mtime
			elif(str(resp) != str(camposMsg[1])):
				if(resp!=False):
					see_other_303(socketConn,resp,PORTA)
				else:
					not_found(socketConn)
				# print(resp+"2")
		else:
			print(camposMsg)
			bad_request(socketConexao)
			socketConn.close()
			
		for i in range(len(camposMsg)):
			if camposMsg[i] == "Connection:" and camposMsg[i+1] == "Close" :
				
				flag = False
	
	#print("sai")
	socketConn.close()

#verifica se existe uma condicao no get
def verifica_get_condicional(m_text):
	tokens = m_text.split("\r\n")
	t = '/f'
	for i in range(len(tokens)):
		ax = tokens[i].split()
		# print ax
		if len(ax) > 0:
			if ax[0] == 'If-Modified-Since:':
				# print(tokens[i])
				t = ax[1:]
				break

	return t

# Le a requisicao HTTP do socket (Soh funciona com msg GET)
def recv_http(socketConn):
	
	msg = socketConn.recv(2048)
	request = msg
	while msg.endswith("\r\n\r\n") == False:
		msg = socketConexao.recv(2048)
		request += msg
		
	return request

# recupera nome do arquivo da msg http Get
def getFileName(camposGetMsg):
	filename = camposGetMsg[1]
	if filename[0] == '/':
		return filename[1:] #elimina a barra para procurar no diretorio local
	else:
		return filename
	
#funcao principal
if __name__ == "__main__":
	try:
		# cria o socket para aguardar conexoes TCP
		socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socketServidor.error as msg:
		socketServidor = None
		#continue
	try:

		socketServidor.bind(('',PORTA))
		socketServidor.listen(5)
	except socketServidor.error as msg:
		socketServidor.close()
		socketServidor = None
		#continue
	#break  
	if socketServidor is None:
		print( 'could not open socket')
		sys.exit(1)

	num_thread = 1
	# looping para tratar conexoes
	while True:
		
		print("Servidor aguardando conexoes...")
		print("therad: "+str(num_thread))
		
		
		#cria uma therad para tratar a conexao
		try:
			#primeiro param e o cara que conectou, 
			socketConexao, addr = socketServidor.accept()
			

			thread.start_new_thread(thread_con,(socketConexao, addr, num_thread))
			num_thread = num_thread + 1
		except thread.error as e:
		#except (ImportError,OSError,IOError)  as e:
			print("Erro na criacao da thread",e)
		# lendo a msg de requisicao http
		'''
		msg = recv_http(socketConexao)

		# recupera campos da msg HTTP e trata:
		#  1 Se nao for um GET retornar codigo 400 - bad requet
		#    1.1 Se for um GET, mas o arquivo solicitado nao for 
		#        encontrado na pasta, retornar codigo 404 - not found
		#  2 Se for um GET e o arquivo for encontrado retornar
		#    codigo 200 (ok), junto com o arquivo solicitado 

#https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method
 # https://pythonhelp.wordpress.com/2013/03/12/acessando-recursos-na-web-com-python/

https://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol#POST

 '''