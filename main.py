"""
each vertex has three parametres which are its coordinates
x: index in the inner list
y: index in the main nested list
z: the height given as the element of the list
"""


def calc_heuristic(curr_vertex, finish_vertex, graph):
    """
    calculate heuristic distance for the current vertex
    PS: that's manhattan distance which counts based on x,y,z
    coordinates of the vertex
    :param curr_vertex:
    :param finish_vertex:
    :return:
    """
    x_difference = abs(curr_vertex[0] - finish_vertex[0])
    y_difference = abs(curr_vertex[1] - finish_vertex[1])
    z_start, z_finish = graph[curr_vertex[1]][curr_vertex[0]], graph[finish_vertex[1]][finish_vertex[0]]
    z_difference = abs(z_start-z_finish)
    return x_difference + y_difference + z_difference


def calc_f_value(g_distance, heuristic_distance):
    """
    literally the sum of both arguments
    :param g_distance:
    :param heuristic_distance:
    :return: the sum of two given arguments
    """
    return g_distance + heuristic_distance


def find_adjacent(curr_vertex, graph):
    """
    this function find ALL the vertexes that are connected to the current
    one based on the next condition:
    only those vertexes are connected that have a difference=1 of only one parameter (either x or y)
    :param graph:
    :param curr_vertex:
    :return: adjacent_list
    adjacent_list is gonna be a list of tuples
    each tuple consists of to integers: x and y index of a vertex

    ATTENTION:
    Please take into account the fact that not all vertexes are going to have
    four connected vertexes with them as some of them are going to be the ones on the side
    meaning they have only three adjacent vertexes
    and some of them are going to be in the corner
    meaning they only have two adjacent vertexes
    """
    adjacent_list = []
    x, y = curr_vertex[0], curr_vertex[1]
    if x - 1 >= 0:
        adjacent_list.append((x - 1, y))
    if y - 1 >= 0:
        adjacent_list.append((x, y - 1))
    if x + 1 < len(graph):
        adjacent_list.append((x + 1, y))
    if y + 1 < len(graph[0]):
        adjacent_list.append((x, y + 1))
    return adjacent_list


def parsing_info(graph, step, start_vertex, finish_vertex):
    """
    that is the function which ties up all the other functions
    and goes before main
    there we initialise the dictionary of our open vertexes
    the key will be the tuple of two elements(x,y) of a vertex
    and the value is going to be a list
    where:
    the first element: g_distance of a vertex
    the second element: heuristic distance of a vertex
    the third element: f_value of a vertex
    the fourth element: tuple of the previous vertex
    PS: previous vertex means the vertex which we got to the current one from
    :param graph:
    :param step:
    :param start_vertex:
    :param finish_vertex:
    :return:
    """
    open_dict = {}
    closed_set = set()
    curr_vertex = start_vertex
    start_heuristic = calc_heuristic(start_vertex, finish_vertex)
    start_g = 0  # g_distance of a start vertex is 0 as it is the distance to start vertex
    start_f = start_heuristic + start_g
    start_value = [start_g, start_heuristic, start_f, ()]
    # last element is empty tuple because start vertex doesn't have previous one
    open_dict[start_vertex] = start_value
    path = []
    while curr_vertex != finish_vertex:
        # this is the main while loop
        # which runs till we get to our final destination
        adjacent_vertexes = find_adjacent(curr_vertex, graph)
        f_adj = float("inf")  # to find the minimum f_value
        for vertex in adjacent_vertexes:
            if vertex not in closed_set and vertex not in open_dict:
                # that's where all the fun begins)
                vertex_g = open_dict[curr_vertex][0] + step * 1  # get the g_distance of the vertex from
                # which we got here and add the step multiplied by the difference=1
                vertex_h = calc_heuristic(vertex, finish_vertex)
                vertex_f = calc_f_value(vertex_g, vertex_h)
                vertex_value = [vertex_g, vertex_h, vertex_f, curr_vertex]
                open_dict[vertex] = vertex_value  # add the vertex to the open dict
                if vertex_f < f_adj:
                    f_adj = vertex_f
                    curr_vertex = vertex
                    got_from = open_dict[curr_vertex][-1]
                    path.append(got_from)
        closed_set.add(curr_vertex)
        # get the vertex with the minimum f_value from the open dict and make it current
        curr_vertex = min(open_dict.items(), key=lambda x: x[1][-2])[0]
        the_distance = open_dict[curr_vertex][0]
        del open_dict[curr_vertex]  # remove vertex with the lowest f_value from the open list
    return path, the_distance


def main():
    pass

if __name__ == '__main__':
    print(find_adjacent((2, 1),
                        [[1888.2200, 2992.222, 453.333], [234.333, 765.987, 762.433], [1234.567, 432.675, 999.999]]))
    main()

