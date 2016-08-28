Exercise 2.2

For an N x N adjacency matrix A, in order to find the connected components, you could use a breadth first search on the matrix to find all the connected component clusters.

Starting with an initial node i, traverse the matrix and find all connections (where Aij = 1) and add it the initial cluster c. Repeat for every node not in a cluster. Once all nodes 0 to i are in a cluster, then you have your final list of connected components.