#estadoEntrado="ACXXXXDBX"
#estadoEntrado="AXXXXXDBC"
#estadoEntrado="ACBXXXDXX"
#estadoEntrado="ACXBXXDXX"
def VerificacionPosDisponible(estadoEntrado):
	posDisponible=[]
	fila = 1
	pos = 0
	cont = 1
	#print("entro"+estadoEntrado)
	while(pos<9):
		#total hay 3 filas
		#si el fila la que esta mas arriba es una poscion disponible para bloque
		#print("##############################3la letra es ",estadoEntrado[pos],"posicion es:",pos)
		if (estadoEntrado[pos] == "X")&(cont == 1) :				
			posDisponible.append(pos)
			#modificamos posicion y saltamos a siguiente fila 
			#print("if cont 3 ,cont es: ",cont,"fila es: ",fila)
			pos += 3
			fila +=1
			cont = 1
			
			continue
				

		#si el fila la que esta en la segunda es un bloque
		elif (estadoEntrado[pos] == "X")&(cont == 2):
			posDisponible.append(pos)
			#print("if cont 2 ,cont es: ",cont,"fila es: ",fila)
			#modificamos posicion y saltamos a siguiente fila	
			pos += 2
			fila +=1
			cont = 1
					
			continue

		#si este fila la que esta en la tercera es un bloque
		elif (estadoEntrado[pos] == "X")&(cont == 3):
			posDisponible.append(pos)
			#print("if cont 1 ,cont es: ",cont,"fila es: ",fila)
			pos += 1
			fila +=1
			cont = 1
			
			continue

		else :
			#print("if cont 0 ,cont es: ",cont,"fila es: ",fila)
			pos += 1
			cont+= 1
			
			if cont == 4 :
				posDisponible.append("X")
				cont = 1
				fila+= 1

	#for i in posDisponible:	print(i)
	return (posDisponible)



#print("posBloqueDisponible:")
# ejemplo #estadoEntrado="ACXXXXDBX"
#X	!	X	!	X !
#C	!	X	!	B !
#A	v	X	v	D V
#<--------------------
# ejemplo # print ("ante de entrar estadoEntrado es:"+estadoEntrado)

def VerificacionBloqDisponible(estadoEntrado):
	#Lista en 3 filas los bloque diponible para nuevas combinaciones
	posDisponible=[]
	fila = 3
	pos = -1 
	cont = 3
	#print("entro"+estadoEntrado)
	while (pos>-10):

		#total hay 3 filas,posicion desde atras hacia adelante.	
		#si el fila la que esta mas arriba es un bloque
		#print("la letra es ",estadoEntrado[pos],"posicion es:",pos)
		if (estadoEntrado[pos] != "X")&(cont == 3) :				
			posDisponible.append(pos)
			#modificamos posicion y saltamos a siguiente fila 
			#print("if cont 3 ,cont es: ",cont,"fila es: ",fila)
			pos -= 3
			fila -=1
			cont = 3
			
			continue


		#si el fila la que esta en la segunda es un bloque
		elif (estadoEntrado[pos] != "X")&(cont == 2):
			posDisponible.append(pos)
			#print("if cont 2 ,cont es: ",cont,"fila es: ",fila)	
			pos -= 2
			fila -=1
			cont = 3
					
			continue

		#si el fila la que esta en la primera es un bloque
		elif (estadoEntrado[pos] != "X")&(cont == 1):
			posDisponible.append(pos)
			#print("if cont 1 ,cont es: ",cont,"fila es: ",fila)
			pos -= 1
			fila -=1
			cont = 3
			
			continue

		else :
			#print("if cont 0 ,cont es: ",cont,"fila es: ",fila)
			pos -= 1
			cont-= 1
			#print(pos)
			#print(cont,"numero de cont")
			if cont == 0 :
				#print("agregrego X0: ")
				posDisponible.append("X")
				
				cont = 3

				fila-= 1
	solucion=[]
 
	for i in reversed(posDisponible):	

		if i != "X":	
			solucion.append(str(9+int(i)))
		else:
			solucion.append(i)

	#for i in solucion:	print(i)	
	return (solucion)

#ejemplo="ACXBXXDXX"

def generarEstado(estadoEntrado):
	PosicionDisponible = VerificacionPosDisponible(estadoEntrado)
	BloqDisponible = VerificacionBloqDisponible(estadoEntrado)
	#for i in PosicionDisponible:	
	#	print(i)
	#for i in BloqDisponible:	
	#	print(i)
	nuevosEstados=[]

	for posLetra in BloqDisponible:
		
		if posLetra == "X":
			#print("entro siguiente bloqye")
			continue
		ListaEstado=[]
		auxList=ListaEstado

		if PosicionDisponible[0] != "X":	posB0=int(PosicionDisponible[0])	
		if PosicionDisponible[1] != "X":	posB1=int(PosicionDisponible[1])
		if PosicionDisponible[2] != "X":	posB2=int(PosicionDisponible[2])

	
		if posLetra == BloqDisponible[0]:

			if PosicionDisponible[1] != "X":
				auxEstado=""	
				for letra in estadoEntrado:
					ListaEstado.append(letra)

				ListaEstado[int(posLetra)]=estadoEntrado[posB1]
				ListaEstado[posB1]=estadoEntrado[int(posLetra)]

				for i in ListaEstado:
					auxEstado=auxEstado+i

				nuevosEstados.append(auxEstado)
				#print("entra1",nuevosEstados)


			if PosicionDisponible[2] != "X":
				auxEstado=""
				ListaEstado=[]
				
				for letra in estadoEntrado:
					ListaEstado.append(letra)

				ListaEstado[int(posLetra)]=estadoEntrado[posB2]
				ListaEstado[posB2]=estadoEntrado[int(posLetra)]

				for i in ListaEstado:
					auxEstado=auxEstado+i
				
				nuevosEstados.append(auxEstado)
				#print("entra1",nuevosEstados)


		elif posLetra == BloqDisponible[1]:

			if PosicionDisponible[0] != "X":
				auxEstado=""
				ListaEstado=[]

				for letra in estadoEntrado:
					ListaEstado.append(letra)


				ListaEstado[int(posLetra)]=estadoEntrado[posB0]
				ListaEstado[posB0]=estadoEntrado[int(posLetra)]

				for i in ListaEstado:
					auxEstado=auxEstado+i
				
				nuevosEstados.append(auxEstado)
				#print("entra2",nuevosEstados)

			if PosicionDisponible[2] != "X":
				auxEstado=""
				ListaEstado=[]

				for letra in estadoEntrado:
					ListaEstado.append(letra)


				ListaEstado[int(posLetra)]=estadoEntrado[posB2]
				ListaEstado[posB2]=estadoEntrado[int(posLetra)]

				for i in ListaEstado:
					auxEstado=auxEstado+i
				
				nuevosEstados.append(auxEstado)
				#print("entra3",nuevosEstados)
			
		elif posLetra == BloqDisponible[2]:

			if PosicionDisponible[0] != "X":
				auxEstado=""
				ListaEstado=[]

				for letra in estadoEntrado:
					ListaEstado.append(letra)


				ListaEstado[int(posLetra)]=estadoEntrado[posB0]
				ListaEstado[posB0]=estadoEntrado[int(posLetra)]

				for i in ListaEstado:
					auxEstado=auxEstado+i
				
				nuevosEstados.append(auxEstado)
				#print("entra3",nuevosEstados)

			if PosicionDisponible[1] != "X":
				auxEstado=""
				ListaEstado=[]

				for letra in estadoEntrado:
					ListaEstado.append(letra)


				ListaEstado[int(posLetra)]=estadoEntrado[posB1]
				ListaEstado[posB1]=estadoEntrado[int(posLetra)]

				for i in ListaEstado:
					auxEstado=auxEstado+i
				
				nuevosEstados.append(auxEstado)
				#print("entra3",nuevosEstados)
		else:
			print("no entro.")	
	return (nuevosEstados)




estados=[]
totalEstado=0
def reniciar_totalEstado():
	global totalEstado
	totalEstado+=1


def AgreegarEstado(estado):
		
		if estado not in estados:
			estados.append(estado)
			reniciar_totalEstado()
			print("totalEstado es :",totalEstado,"nuevo estado es : ",estado)
		#else:
			#print("ya existe tal estado: ",estado)



def BuscarEstados():

	estadoInicial="AXXBXXDCX"
	AgreegarEstado(estadoInicial)

	for estadoNuevo in estados:


		G=generarEstado(estadoNuevo)
		for x in G:
			AgreegarEstado(x)
		

		#print(estados)

BuscarEstados()

