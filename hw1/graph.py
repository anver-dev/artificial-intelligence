from collections import deque, defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    LAST_ELEMENT = -1

    def __init__(self):
        self.peopleGraph = defaultdict(list)

    def addEdge(self, origin, destination):
        self.peopleGraph[origin].append(destination)
        self.peopleGraph[destination].append(origin)
    
    def bfs(self, start, goal):
        start = start.upper()
        goal = goal.upper()

        queue = deque([[start]])

        levels = {0: [start]}
        currentLevel = 0

        print("*"*30)
        print(f"Init bfs from {start} to {goal}")
        print("*"*30)

        while queue:
            path = queue.popleft()
            currentPerson = path[self.LAST_ELEMENT]

            if currentPerson == goal:
                print("*"*30)
                print("\n-- Solution found!")
                print(f"-- Path: {' -> '.join(path)}")
                print("*"*30)
                return path

            friends = self.peopleGraph[currentPerson]

            for friend in friends:
                extendedPath = list(path)
                extendedPath.append(friend)

                queue.append(extendedPath)

                nextLevel = currentLevel + 1

                if nextLevel not in levels:
                    levels[nextLevel] = []

                levels[nextLevel].append(friend)

            # If the current level is over or the queue is empty, print the current level nodes
            if not queue or (queue and len(queue[0]) > nextLevel):
                print(f"-- Generated at level {currentLevel}: {levels[currentLevel]}")
                print("."*30)
                currentLevel += 1

        print("No connection found.")
        return None

    def renderPath(self, path=None, start=None, goal=None):
        G = nx.Graph()

        for currentPerson, friends in self.peopleGraph.items():
            for friend in friends:
                G.add_edge(currentPerson, friend)

        pos = nx.spring_layout(G, k=0.15)

        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)

        # If a path is provided, highlight the path
        if path:
            pathConnections = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=pathConnections, edge_color='orange', width=2)
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')

        # Highlight the start and goal nodes
        if start and goal:
            nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color='green')
            nx.draw_networkx_nodes(G, pos, nodelist=[goal], node_color='red')

            # Add a label to indicate start and goal nodes
            plt.text(pos[start][0], pos[start][1] + 0.1, 'Start', fontsize=10, ha='center')
            plt.text(pos[goal][0], pos[goal][1] + 0.1, 'Goal', fontsize=10, ha='center')

        # 
        # Show the plot
        plt.show()