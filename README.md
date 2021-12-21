# Pathfinding-project
## Discrete math


* Introduction.


This project implements an algorithm for finding the shortest path between two points on the surface.
Pathfinder algorithms are essential because they are used in applications such as Google Maps, satellite navigation systems, and packet routing over the Internet. The use of path search algorithms is not limited to navigation systems. The general idea can be applied to other applications, such as computer games. In games, as in life, we often want to find ways from one place to another, with the shortest distance. In such cases, it would be advisable to take into account travel time. There are several algorithms for finding the shortest distance between two points on the surface. The most popular of these are the Dijkstra algorithms and the A * algorithm. Algorithm A * improves Dijkstra's shortest path algorithm, including additional information using a heuristic function that determines which paths should be explored next. Thanks to this optimization, the shortest paths are found faster. Algorithm A * can be used to find the shortest paths between individual pairs of places where GPS coordinates are known.

Algorithm A * is implemented in Python. The algorithm is divided into smaller subtasks. Using the methods of functional decomposition

* Pseudocode


<img width="601" alt="Screenshot 2021-12-21 at 17 17 30" src="https://user-images.githubusercontent.com/91616807/146954037-671b2b6e-fd20-433e-a9ef-d2e8f4c11c21.png">

Algorithm A * is described by one simple formula: **F = G + H.

G is the value that is the price through all the edges passed from the initial vertex to the current one.

H is the value that is the estimated distance from the current vertex to the final one—calculated by the formula manhattan distance.

For the current vertex, adjacent vertices are selected and added to the set of open vertices. For each of the vertices, G, H, and, in particular, their sum, F, are calculated. The current vertex is added to the set of closed vertices so that it is not checked again and not returned to it.

After that, the shortest path (F distance) is selected and goes to the vertex with the smallest F. However, other vertices are not closed. They will close when the algorithm passes them and sees that their F value does not fit. Thus, the algorithm moves forward until it reaches the final vertex.

The advantage of the A * algorithm over the Dijkstra algorithm is that A * finds only the shortest path and does not find all variations of the path.

The length of the shortest path will be the minimum G distance at the top of the destination.

* Conclusion

The shortest distance search algorithm is widely used in various aspects of technological life. For example, NPC game heroes often move this way.

A * does not visit every vertex of the graph, so it is more optimized than, for example, Dijkstra's algorithm.

This algorithm selects the top with the greatest potential to lead us to the final point.

The more accurate the estimation distance, the faster the shortest path

The array of open vertices is stored as a priority queue.
