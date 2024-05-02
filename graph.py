class AdjacencyListGraph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    def display_graph(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

# Create a graph
graph = AdjacencyListGraph()

# Add vertices
graph.add_vertex("Banjarnegara")
graph.add_vertex("Wonosobo")
graph.add_vertex("Temanggung")























































graph.add_edge("Surakarta", "Pekalongan")
graph.add_edge("Blora", "Rembang")
graph.add_edge("Blora", "Pati")
graph.add_edge("Blora", "Kudus")
graph.add_edge("Blora", "Semarang")
graph.add_edge("Blora", "Kendal")
graph.add_edge("Blora", "Pekalongan")
graph.add_edge("Rembang","Pati")
graph.add_edge("Rembang", "Kudus")
graph.add_edge("Rembang", "Semarang")
graph.add_edge("Rembang", "Kendal")
graph.add_edge("Rembang", "Pekalongan")
graph.add_edge("Pati", "Kudus")
graph.add_edge("Pati", "Semarang") 
graph.add_edge("Pati", "Kendal")
graph.add_edge("Pati", "Pekalongan")
graph.add_edge("Kudus", "Semarang")
graph.add_edge("Kudus", "Kendal")
graph.add_edge("Kudus", "Pekalongan")
graph.add_edge("Semarang", "Kendal")
graph.add_edge("Semarang", "Pekalongan")
graph.add_edge("Kendal", "Pekalongan")


# Display the graph
graph.display_graph()
