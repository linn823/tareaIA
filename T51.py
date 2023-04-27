from dataclasses import dataclass

class nodoProfundidad():

	def __init__(self,nombre,valor):    
		#nombre de nodo
		self.nombre = nombre
		#costo de nodo
		self.costo = valor
		#inicia estados de visitados es Falso
		self.estado = False
		#inicia con vecino None
		self.hijos = []


class Búsquedaenprofundidad:
	#ruta recorrido
	pila=[]

	nodoInicial=nodoP(Nodo_inicial,0)

	def AddPila(nodo):
		pila.append(nodo)

	def PopPila():
		pila.pop(0)
		#print(l.pop(0))elimina  primer elemento de Lista l.
		# a.pop() quita y retorna el último elemento de la lista.

	def generarArbol():

	def buscar(nodoActual,nodoObjetivo):
		AddPila(nodoActual)
		if nodoActual == nodoObjetivo:
			return pila

		nodosSucesores=nodo_actual.hijos

		#si nodos Sucesores no es vacio,elije un nodoSucesor cualquiera :
		#Aqui falta un caso.
		if len(nodosSucesores) > 0 :
			nodoAleatorio = random.choice(nodosSucesores)
		#si nodoAleatorio su estado no esta visitado:
		elif len(nodosSucesores) == 0:
			return None

		if nodoALeatorio.estado == False: 
			#llamar a un nuveoNodo y hacer buscar Recursiva
			nuevoNodo = buscar(nodoAleatorio,nodoObjetivo)
			#si nuevo nodo es None,devolvermos None para anterio.
			AddPila(nuevoNodo)
		else:
			return None

		#if 3 devuelve nuevo nodo si no es None
		#lo contrario devuelve infomacion None.
		if nuevoNodo is None
			#borramos lo que agregamos si es que es None
			PopPila()
			return None
		else:
			return nuevoNodo

 #tuto#Hayque generar el arbol,los metodos tampoco lo metí,me duele los ojos......aaaaaaaaaaaseñorrr...
  
class Búsqueda por costo uniforme():


class Búsqueda greedy():
	#ruta recorrido
	pila=[]

	nodoInicial=nodoP(Nodo_inicial,0)

	def AddPila(nodo):
		pila.append(nodo)

	def PopPila():
		pila.pop(0)
		#print(l.pop(0))elimina  primer elemento de Lista l.
		# a.pop() quita y retorna el último elemento de la lista.

	def buscar(nodoActual,nodoObjetivo):
		AddPila(nodoActual)
		if nodoActual == nodoObjetivo:
			return pila

		nodosSucesores=nodo_actual.hijos

		#si nodos Sucesores no es vacio,elije un nodoSucesor cualquiera :
		#Aqui falta un caso.
		if len(nodosSucesores) == 1 :
			nodoMejor = nodosSucesores
		elif len(nodosSucesores) > 1:
			nodoMejor = nodosSucesores
			for x in nodosSucesores:
				if nodoMejor.costo > x.costo:
					nodoMejor = x
		#si nodoAleatorio su estado no esta visitado:
		elif len(nodosSucesores) == 0:
			return None

		if nodoMejor.estado == False: 
			#llamar a un nuveoNodo y hacer buscar Recursiva
			nuevoNodo = buscar(nodoMejor,nodoObjetivo)
			#si nuevo nodo es None,devolvermos None para anterio.
			AddPila(nuevoNodo)
		else:
			return None

		#if 3 devuelve nuevo nodo si no es None
		#lo contrario devuelve infomacion None.
		if nuevoNodo is None
			#borramos lo que agregamos si es que es None
			PopPila()
			return None
		else:
			return nuevoNodo


class AEstrella(nodo):
#comentario

ListNodo = []
ListRuta = []