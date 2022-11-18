import heapq
#Here I will use a adjacency list to represent the relation between nodes and their weights
graph = {"A":("B","C"), "B":("C", "D"), "C":("E"), "D":("D"), "E":("B","D")}
#All edge weughts have to be non negative
pathWeights = {"A":[("B", 1), ("C", 4)], "B":[("C", 2), ("D", 8)], "C":[("E", 3)], "D":[("D", 2)], "E":[("B", 2), ("D", 1)]} 

def getWeight(n1, n2):
    #Weight of path from n1 to n2
    for node, w in pathWeights[n1]:
        if node == n2:
            return w
    return -1

def getIndex(s):
    return ord(s) - ord("A")

def fix(Q, d, w):
    for i in range(len(Q)):
        x, y = Q[i]
        if y == w:
            Q[i] = (d, w)
            break
    heapq.heapify(Q)
    
def DijkstraShortestPath(G, s):
    #s is the starting node
    dist = [-1] * len(G)
    prev = ["none"] * len(G)
    Q = [] #Our min heap
    #Initialize starting node to 0
    dist[getIndex(s)] = 0
    for u in G:
        #Distance for all except the starting node are set to inf
        if u != s:
            dist[getIndex(u)] = float("inf")
        prev[getIndex(u)] = "none"
        #Pushing elements into the heap
        heapq.heappush(Q, (dist[getIndex(u)], u))   
    visited = set()
    while(Q):
        #Popping element with smallest distance
        ignore, u = heapq.heappop(Q)
        #A viisted set is being used because once elements are popped from the heap
        #they are not used
        visited.add(u)

        for w in graph[u]:
            if w not in visited:
                d = dist[getIndex(u)] + getWeight(u, w)
                if d < dist[getIndex(w)]:
                    dist[getIndex(w)] = d
                    prev[getIndex(w)] = u
                    fix(Q, d, w)
    
    return dist, prev

print(DijkstraShortestPath(graph, "A"))