from dataclasses import dataclass

class nodoP():
  nombre = str
  valor = int
  estado = bool
  profundidad = int
  vecinos = []

  def __init__(self,nombre,valor):    
    self.nombre = nombre
    self.costo = valor
    self.estado = False
    
  
class Búsquedaenprofundidad:
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
		pila.append(nodoActual)
		if nodoActual == nodoObjetivo:
			return pila
      
		nodosSucesores=nodo_actual.vecinos

		if len(nodosSucesores) > 0 :
			nodoAleatorio = random.choice(nodosSucesores)
		if nodoALeatorio.estado != False:
			nuevoNodo = buscar(nodoAleatorio,nodoObjetivo)
			pila.append(nuevoNodo)
		if nuevoNodo is None
			pila.pop(0)
			return None
		else:
			return nuevoNodo
      
class Búsqueda por costo uniforme(nodo):


class Búsqueda greedy(nodo):
#comentario

class AEstrella(nodo):
#comentario

#nodoXD
clase node:
	name:str
	cost:int
	state:bool
	nextNod:

	def __init__(self,name,cost,nextNod)
		self.name = name
		self.cost = cost
		self.nextNod = nextNod

	def addNode(self,name,cost)
	//nextNod puede contener varios puntero nodos
	//NextRouteCost puede contener varios costos asociado.

	
clase routeCost:
	origen: str
	destination: str
	state:bool
	cost:int

	def __init__(self,origin,destination,cost)
		self.origin = origin
		self.destination = destination
		self.cost = cost