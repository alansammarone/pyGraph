'''
	Simple class that implements a graph data structure.
	It can represent directed and undirected graphs, as well as simple and weighted graphs.
	It also implements breadth first search and Dijkstra.
'''

class Graph():

	# adj is the adjencency dict: adj[n] = {a: w1, b: w2} means the edge n -> a has weight w1, and the edge n -> b has weight w2
	def __init__(self, adj):
		self.adj = adj


	def AreNeighbors(self, n1, n2):
		return True

	def GetNeighbors(self, n):
		return self.adj[n]


	def GetPath(self, parents, d):
		p = [d]
		current_node = d
		while current_node:
			current_node = parents[current_node]
			p.append(current_node)

		return list(reversed(p[:len(p)-1]))

	def BreadthFirstSearch(self, s, d):

		frontier = {s}
		parents = {s: None}
		levels = {s: 0}
		l = 1

		while frontier:
			new_frontier = []
			for n in frontier:
				neighbors = self.GetNeighbors(n)
				for b in neighbors:
					if b not in levels:
						levels[b] = l
						parents[b] = n
						if b == d: return self.GetPath(parents, d)
						new_frontier.append(b)
			frontier = new_frontier
			l += 1

		return None



	'''
		Implements Dijkstra's algorithm to find the minimum path from s to d in a weighted graph.
	'''
	def Dijkstra(self, s, d):
		distances = {n: float('inf') for n in self.adj}
		distances[s] = 0
		parents = {s: None}
		unvisited = [n for n in self.adj]
		current_node = s

		while unvisited:

			ns = self.GetNeighbors(current_node)
			for n in ns:
				if n in unvisited:
					tentative_distance = distances[current_node] + self.adj[current_node][n]
					if tentative_distance < distances[n]:
						distances[n] = tentative_distance
						parents[n] = current_node

			if current_node == d:
				return self.GetPath(parents, d)

			else:

				tmp_unvisited = unvisited[:]
				del tmp_unvisited[tmp_unvisited.index(current_node)]
				next_node = tmp_unvisited[0]
				min_distance = distances[next_node]

				for i, n in enumerate(tmp_unvisited):

					if distances[n] < min_distance:
						min_distance = distances[n]
						next_node = n

				distance_to_next_node = distances[next_node]

				if distance_to_next_node == float('inf'):
					return False
				else:
					del unvisited[unvisited.index(current_node)]
					current_node = next_node

		return False
