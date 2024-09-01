from graph import Graph

if __name__ == "__main__":
    peopleGraph = Graph()

    peopleGraph.addEdge('A', 'B')
    peopleGraph.addEdge('A', 'D')
    peopleGraph.addEdge('B', 'C')
    peopleGraph.addEdge('B', 'E')
    peopleGraph.addEdge('C', 'F')
    peopleGraph.addEdge('D', 'G')
    peopleGraph.addEdge('D', 'E')
    peopleGraph.addEdge('E', 'F')
    peopleGraph.addEdge('F', 'I')
    peopleGraph.addEdge('G', 'H')
    peopleGraph.addEdge('H', 'I')

    minimalConnections = peopleGraph.bfs('I', 'A')

    # Draw the graph with the minimal connections
    peopleGraph.renderPath(minimalConnections, 'I', 'A')