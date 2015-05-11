MAX = 2**31

class Edge():
	"""
	Edge class that conains its first vertex, its second and its weight
	"""
	def __init__(self,s_vertex,e_vertex, weight):
		"""
		Constructor to the Edge
		s_vertex -- primer vertice de la arista
		e_vertex -- segundo vertices de la arista
		weight -- peso de la arista
		"""
		self.start_vertex = s_vertex
		self.end_vertex = e_vertex
		self.weight = weight

	def __str__(self):
		"""
		Edge in string
		"""
		return "( " + str(self.start_vertex) + ", " + str(self.end_vertex) + ") " \
				+ "("+ str(self.weight) +")"

	def get_first(self):
		"""
		Return the first vertex of the edge
		"""
		return self.start_vertex

	def get_last(self):
		"""
		Return the last vertex of the edge
		"""
		return self.end_vertex

	def get_weight(self):
		"""
		Return the weight of the edge
		"""
		return self.weight

#End class Edge

class Vertex():
	"""
	Vertex class of the Graph
	"""
	def __init__(self, id_v):
		"""
		id_v -- ID of the Vertex
		"""
		self.ide = id_v
		self.pred = None
		self.dist = 0
		self.adjacency = list()

	def __str__(self):
		"""
		String form of the Vertex
		"""

		return str(self.ide)

	def __eq__(self,other):
		"""
		To compare two Vertex by ==
		"""
		if self.ide == other.ide:
			for i in self.adjacency:
				if not (i in other.adjacency):
					return False
			return True
		else:
			return False
	
	def get_id(self):
		"""
		Return the ID of the Vertex
		"""
		return self.ide
	
	def get_adjacencylist(self):
		"""
		Return the adjacency list of the Vertex
		this list contains of the Edges which the first 
		vertex is this
		"""
		return self.adjacency
	
	def get_pre(self):
		"""
		Return the predecessor of the Vertex in some path
		"""
		return self.pred
	
	def set_pre(self,pre):
		"""
		set the predecessor of the Vertex in some path
		"""
		self.pred = pre

	def get_dist(self):
		"""
		Return the distance of the Vertex to the source vertex
		"""

		return self.dist

	def set_dist(self, dist):
		"""
		Set the distance of the Vertex to some source vertex
		"""
		self.dist = dist
	
	def connect(self, vertex2, weight):
		"""
		Connect two Vertices
		"""
		edge = Edge(self,vertex2,weight)
		self.adjacency.append(edge)
#End class vertex

class Graph():
	"""
	Graph class using adjacency list
	"""

	def __init__(self,is_directed):
		"""
		is_directed -- it say if the Graph is directed
		"""
		self.vertices = list()
		self.n_vertices = 0
		self.is_directed = is_directed

	def find_vertex(self, id_vertex):
		"""
		Find one Vertex on the Graph using its ID
		"""
		for i in self.vertices:
			if i.get_id() == id_vertex:
				return i
		return None

	def add_vertex(self, id_vertex):
		"""
		Add a Vertex in the Graph
		id_vertex -- ID of the new Vertex
		"""
		v = Vertex(id_vertex)
		self.vertices.append(v)
		self.n_vertices +=1

	def connect_vertices(self, id_vertex1, id_vertex2,weight):
		"""
		Connect two Vertices in the Graph
		"""
		u = self.find_vertex(id_vertex1)
		v = self.find_vertex(id_vertex2)
		if u is None or v is None:
			return False
		if self.is_directed:
			u.connect(v,weight)
		else:
			u.connect(v,weight)
			v.connect(u,weight)
		return True

	def relax(self,u,v,w):
		"""
		Function to Relax vertices
		u -- vertex previos of v
		v -- vertex to relax
		w -- weight of the edge of u and v
		"""
		if v.get_dist() > u.get_dist() + w:
			v.set_dist(u.get_dist()+ w)

	def bellman_ford(self, id_source_vertex):
		"""
		This algorithm say if there is a negative cycle in the graph
		and created the shortest path of some source vertex to all
		vertices in the Graph
		id_source_vertex -- ID of the source vertex for the path to construct
		Return True if it find a negative cycle
		"""
		source_vertex = None
		for vertex in self.vertices:
			if(vertex.get_id() == id_source_vertex):
				vertex.set_dist(0)
				vertex.set_pre(None)
				source_vertex = vertex
			else:
				vertex.set_dist(MAX)
				vertex.set_pre(None)
		if source_vertex is None:
			print ("No existe ese vertice en la grafica.")
			return True

		for i in range(self.n_vertices-1):
			for vertex in self.vertices:
				edges = vertex.get_adjacencylist()
				for edge in edges:
					u = edge.get_first()
					v = edge.get_last()
					weight = edge.get_weight()
					self.relax(u,v,weight)

		for vertex in self.vertices:
			edges = v.get_adjacencylist()
			for edge in edges:
				v2 = edge.get_last()
				weight = edge.get_weight()
				if(v2.get_dist() > vertex.get_dist() + weight):
					return True
		return False

	def print_distances(self, id_source_vertex):
		"""
		Print the distance of all vertices in the Graph by some source vertex
		id_source_vertex -- ID of the source vertex of the path created before
		"""
		source_vertex = self.find_vertex(id_source_vertex)
		print("Start " + "\t"+"Vertex" + "\t", "Distance")
		for vertex in self.vertices:
			print(str(source_vertex)+"\t"+str(vertex)+"\t"+str(vertex.get_dist()))
# End class Graph

def main():
	g = Graph(True)
	g.add_vertex("a")
	g.add_vertex("b")
	g.add_vertex("c")
	g.add_vertex("d")
	g.add_vertex("e")
	g.add_vertex("f")
	g.connect_vertices("a","b",-1)
	g.connect_vertices("a","c",2)
	g.connect_vertices("b","d",3)
	g.connect_vertices("c","e",5)
	g.connect_vertices("e","f",-7)
	g.connect_vertices("f","b",11)
	has_negative = g.bellman_ford("a")
	if has_negative:
		print("Tiene un ciclo negativo")
	else:
		print("No tiene un ciclo negativo")
	print()
	g.print_distances("a")

if __name__ == '__main__':
	main()
