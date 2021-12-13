"""
each vertex has three parametres which are its coordinates
x: index in the inner list
y: index in the main nested list
z: the height given as the element of the list
"""


def calc_heuristic(curr_vertex, finish_vertex):
    """
    calculate heuristic distance for the current vertex
    PS: that's manhattan distance which counts based on x,y,z
    coordinates of the vertex
    :param curr_vertex:
    :param finish_vertex:
    :return:
    """
    pass


def calc_f_value(g_distance, heuristic_distance):
    """
    literally the sum of both arguments
    :param g_distance:
    :param heuristic_distance:
    :return:
    """
    pass


def find_adjacent(curr_vertex):
    """
    this function find ALL the vertexes that are connected to the current
    one based on the next condition:
    only those vertexes are connected that have a difference=1 of only one parameter (either x or y)
    :param curr_vertex:
    :return: adjacent_list
    adjacent_list is gonna be a list of tuples
    each tuple consists of to integers: x and y index of a vertex

    ATTENTION:
    Please take into account the fact that not all vertexes are gonna have
    four connected vertexes with them as some of them are going to be the ones on the side
    meaning they have only three adjacent vertexes
    and some of them are going to be in the corner
    meaning they only have two adjacent vertexes
    """
    pass


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
    while curr_vertex != finish_vertex:
        # this is the main while loop
        # which runs till we get to our final destination
        adjacent_vertexes = find_adjacent(curr_vertex)
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
        closed_set.add(curr_vertex)
        # get the vertex with the minimum f_value from the open dict and make it current
        curr_vertex = min(open_dict.items(), key=lambda x: x[1][-2])[0]
        del open_dict[curr_vertex]  # remove vertex with the lowest f_value from the open list


def main():
    pass


if __name__ == '__main__':
    main()
