from dataclasses import dataclass
//implementacion 5.1

======================================================
==========		Búsqueda en profundidad		=====
======================================================

//https://www.w3schools.com/python/python_classes.asp


clase node:
	name:str
	cost:int
	state:bool
	%%%%%%%%%%%%%%%%%%%%%%%%%
	nextNod:
	NextRouteCost:
	%%%%%%%%%%%%%%%%%%%%%%%%%

	def __init__(self,name,cost,nextNod)
		self.name = name
		self.cost = cost
		self.nextNod = nextNod

	def addNode(self,name,cost)
	//nextNod puede contener varios puntero nodos
	//NextRouteCost puede contener varios costos asociado.


======================================================
	========	clase costos de la ruta		========
======================================================
//https://stackoverflow.com/questions/53131002/creating-a-list-of-pairs-python
//tipo datos: https://docs.python.org/es/3/tutorial/datastructures.html
//9.7 Cambalache:https://docs.python.org/es/3/tutorial/classes.html#odds-and-ends

clase routeCost:
	origen: str
	destination: str
	state:bool
	cost:int

	def __init__(self,origin,destination,cost)
		self.origin = origin
		self.destination = destination
		self.cost = cost






