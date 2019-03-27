from data import *
import os
# Resposta com codigo 200 - OK
def ok_200(socketConn, filename, ext, last_mod, data_at, modo): # para ser implementado
	try:
		fileid = open(filename,"r")
		if ext[len(ext) - 1] == "html" or ext[len(ext) - 1] == "odt" or ext[len(ext) - 1] == "c" or ext[len(ext) - 1] == "py":
			tam = os.path.getsize(filename)
			resp = "HTTP/1.1 200 OK\r\n"
			socketConn.send(resp)
			resp = "Date: " + str(data_at) + " GMT\r\n"
			socketConn.send(resp)
			resp = "Content-Type: text/"+ext[len(ext) - 1]+"\r\n"
			socketConn.send(resp)
			resp = "Content-Length: "+str(tam)+"\r\n"
			socketConn.send(resp)
			'''resp = "Keep-Alive: timeout=5, max=100\r\n"
			socketConn.send(resp)'''
			resp = "Last-Modified: " + str(last_mod) + " GMT\r\n"
			socketConn.send(resp)
			resp = "Connection: Keep-Alive\r\n"
			socketConn.send(resp)
			resp = "\r\n"
			socketConn.send(resp)
			if(modo == "GET"):
				sendFile(socketConn,fileid)

		elif ext[len(ext) - 1] == "gif" or ext[len(ext) - 1] == "jpg" or ext[len(ext) - 1] == "png" or ext[len(ext) - 1] == "ico":
			tam = os.path.getsize(filename)
			resp = "HTTP/1.1 200 OK\r\n"
			socketConn.send(resp)
			resp = "Date: " + str(data_at) + " GMT\r\n"
			socketConn.send(resp)
			resp = "Content-Type: img/"+ext[len(ext) - 1]+"\r\n"
			socketConn.send(resp)
			resp = "Content-Length: "+str(tam)+"\r\n"
			socketConn.send(resp)
			'''resp = "Keep-Alive: timeout=5, max=100\r\n"
			socketConn.send(resp)'''
			resp = "Last-Modified: " + str(last_mod) + " GMT\r\n"
			socketConn.send(resp)
			resp = "Connection: Keep-Alive\r\n"
			socketConn.send(resp)
			resp = "\r\n"
			socketConn.send(resp)
			if(modo == "GET"):
				sendFile(socketConn,fileid)

		elif ext[len(ext) - 1] == "pdf":
			tam = os.path.getsize(filename)
			resp = "HTTP/1.1 200 OK\r\n"
			socketConn.send(resp)
			resp = "Date: " + str(data_at) + " GMT\r\n"
			socketConn.send(resp)
			resp = "Content-Type: application/"+ext[len(ext) - 1]+"\r\n"
			socketConn.send(resp)
			resp = "Content-Length: "+str(tam)+"\r\n"
			socketConn.send(resp)
			'''resp = "Keep-Alive: timeout=5, max=100\r\n"
			socketConn.send(resp)'''
			resp = "Last-Modified: " + str(last_mod) + " GMT\r\n"
			socketConn.send(resp)
			resp = "Connection: Keep-Alive\r\n"
			socketConn.send(resp)
			resp = "\r\n"
			socketConn.send(resp)
			if(modo == "GET"):
				sendFile(socketConn,fileid)

		
		
	except (OSError, IOError) as e:
		not_found(socketConn)
		socketConn.close()

# Resposta com codigo 304 Not Modified
def not_modified_304(socketConn,data_atual,data_mod):
	try:
		resp = "HTTP/1.1 304 Not Modified\r\n"
		socketConn.send(resp)
		resp = "Date: "+ str(data_atual) +" GMT\r\n"
		socketConn.send(resp)
		resp = "Last-Modified: "+ str(data_mod) +" GMT\r\n"
		socketConn.send(resp)
		resp = "\r\n"
		socketConn.send(resp)
	except (OSError, IOError) as e:
		print("Erro ao enviar resp")

#resposta com o codigo 303 see other
def see_other_303(socketConn,resposta,PORTA):
	try:
		resp = "HTTP/1.1 303 See Other\r\n"
		# resp = "localhost:"+str(PORTA)+"/"+resp[1:]+"\r\n"
		socketConn.send(resp)
		resp = "Location: http://192.168.0.29:"+str(PORTA)+"/"+resposta[1:]+"\r\n"
		socketConn.send(resp)
		resp = "\r\n" 
		socketConn.send(resp) # fim do cabecalho
	except (OSError, IOError) as e:
		print("Erro ao enviar resp")

# Resposta com codigo 400 - BAD REQUEST
def bad_request(socketConn,data_at=getData()):
	
	#gera o html para imprimir na tela
	html = "<HTML>\n<TITLE>Bad Request</TITLE>\n<HEAD></HEAD>\n<BODY>\n"+"<P>400 - BAD REQUEST:<br>"+"Seu browser enviou uma requisicao mal formulada!"+"</BODY>\n</HTML>"
	htmlUnicode = unicode(html,"utf-8")         
	resp = "HTTP/1.1 400 BAD REQUEST\r\n"
	socketConn.send(resp)
	resp = "Date: " + str(data_at) + " GMT\r\n"
	socketConn.send(resp)
	resp = "Content-type: text/html; charset=utf-8\r\n"
	socketConn.send(resp)
	resp = "Content-Length: "+str(len(htmlUnicode))+"\r\n" 
	socketConn.send(resp) 
	resp = "\r\n"
	socketConn.send(resp)  # fim do cabechalho da msg de resposta
	socketConn.send(htmlUnicode)

# Resposta com codigo 404 - NOT FOUND
def not_found(socketConn,data_at=getData()):
	try:
	  
		html = "<HTML>\n<TITLE>Not Found</TITLE>\n<HEAD></HEAD>\n<BODY>\n"+"<P>404 - NOT FOUND:<br>"+"O arquivo solicitado nao foi encontrado no servidor!"+"</BODY>\n</HTML>"
		
		htmlUnicode = unicode(html,"utf-8")
		
		resp = "HTTP/1.1 404 NOT FOUND\r\n"
		socketConn.send(resp)
		resp = "Date: " + str(data_at) + " GMT\r\n"
		socketConn.send(resp)
		resp = "Content-type: text/html; charset=utf-8\r\n"
		socketConn.send(resp)
		resp = "Content-Length: "+str(len(htmlUnicode))+"\r\n"
		socketConn.send(resp)
		resp = "\r\n" 
		socketConn.send(resp) # fim do cabecalho
		socketConn.send(htmlUnicode)
	except (OSError, IOError) as e:
		print("Erro ao enviar resp")

# Copia o conteudo inteiro de um arquivo para o socket
def sendFile(socketConn, fd):
	while True:
		
		chunk = fd.read(2048)
		total = 0
		if chunk == "":
			break
		else:
			total = 0
			while total < len(chunk):
				sent = socketConn.send(chunk[total:])
				if sent == 0:
					print("Erro")
					sys.exit()
				total = total + sent

