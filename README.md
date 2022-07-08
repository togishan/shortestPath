shortestPath function takes nested list as an input. Format of nested list is like this: [NodeFrom, NodeTo, Edge1, Edge2, Edge3 ...]

First element of nested list is beginning node and second one is end node. Remaining elements are edges between this nodes. Edges are bi-directional and weighted. Format of any edge is like this: [Node_x, Node_y, Distance]

Task of shortestPath function is obvious: Finding the shortest path between beginning and end nodes, and also finding the total distance between them using Dijkstra's shortest path algorithm. Format of return value of this function is like this:  

"Path: NodeFrom - Node_a - Node_b - ... - NodeTo <br />Distance: N" 


