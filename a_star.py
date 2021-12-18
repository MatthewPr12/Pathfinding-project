"""
each vertex has three parametres which are its coordinates
x: index in the inner list
y: index in the main nested list
z: the height given as the element of the list
"""
import csv
import math


def read_csv(path_to_file):
    """
    the function which turns csv file into the nested list
    :param path_to_file:
    :return:
    """
    graph = []
    with open(path_to_file, "r", encoding="utf-8") as my_file:
        csv_reader = csv.reader(my_file, delimiter=" ")
        for idx, row in enumerate(csv_reader):
            if idx > 2:
                for k in range(len(row)):
                    row[k] = float(row[k])
                graph.append(row)
            elif idx == 2:
                ending_vertex = (int(row[-2]), int(row[-1]))
            elif idx == 1:
                starting_vertex = (int(row[-2]), int(row[-1][:-1]))
    return starting_vertex, ending_vertex, graph


def calc_heuristic(curr_vertex, finish_vertex, graph):
    """
    calculate heuristic distance for the current vertex
    PS: that's manhattan distance which counts based on x,y,z
    coordinates of the vertex
    :param curr_vertex:
    :param finish_vertex:
    :return:
    """
    x_difference = (curr_vertex[0] - finish_vertex[0])**2
    y_difference = (curr_vertex[1] - finish_vertex[1])**2
    z_start = graph[curr_vertex[1]][curr_vertex[0]]
    z_finish = graph[finish_vertex[1]][finish_vertex[0]]
    z_difference = (z_start - z_finish)**2
    return math.sqrt(x_difference + y_difference + z_difference)


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


def get_path(current_vertex, walked_through):
    path = []
    node = current_vertex
    while node is not None:
        path.append(node)
        node = walked_through[node]
    return path[::-1]  # reversed path as we store it backwards


def path_finding(graph, start_vertex, finish_vertex, step):
    """

    :param graph:
    :param start_vertex:
    :param finish_vertex:
    :return: list of tuples (indexes x,y of each vertex in the path)
    """
    walked_through = {}  # store all the nodes that we walked through with their parents to get the path later
    walked_through[start_vertex] = None
    start_g = 0
    start_h = calc_heuristic(start_vertex, finish_vertex, graph)
    start_f = start_h + start_g
    start_parent = None
    open_dct = {}
    closed_lst = []
    open_dct[start_vertex] = [start_g, start_h, start_f, start_parent]
    while open_dct:
        curr_vertex = min(open_dct.items(), key=lambda x: x[1][-2])[0]  # set the current vertex via smallest f
        walked_through[curr_vertex] = open_dct[curr_vertex][-1]
        curr_g = open_dct[curr_vertex][0]
        del open_dct[curr_vertex]
        closed_lst.append(curr_vertex)

        # if got to the finish
        if curr_vertex == finish_vertex:
            return get_path(curr_vertex, walked_through)

        # look through all the adjacent vertexes
        children = find_adjacent(curr_vertex, graph)
        for child in children:
            if child not in closed_lst:
                child_g = curr_g + step * 1
                child_h = calc_heuristic(child, finish_vertex, graph)
                child_f = child_g + child_h
                if child in open_dct:
                    if child_f < open_dct[child][-2]:
                        open_dct[child][-2] = child_f
                else:
                    open_dct[child] = [child_g, child_h, child_f, curr_vertex]
    print("The path does not exist")
    return None


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
    start_heuristic = calc_heuristic(start_vertex, finish_vertex, graph)
    start_g = 0  # g_distance of a start vertex is 0 as it is the distance to start vertex
    start_f = start_heuristic + start_g
    start_value = [start_g, start_heuristic, start_f, None]
    # last element is None because start vertex doesn't have parent :(
    open_dict[start_vertex] = start_value
    path = []
    while curr_vertex != finish_vertex:
        # this is the main while loop
        # which runs till we get to our final destination
        adjacent_vertexes = find_adjacent(curr_vertex, graph)
        f_adj = float("inf")  # to find the minimum f_value
        for vertex in adjacent_vertexes:
            if vertex not in closed_set and vertex not in open_dict:
                vertex_g = open_dict[curr_vertex][0] + step * 1  # get the g_distance of the vertex from
                # which we got here and add the step multiplied by the difference=1
                vertex_h = calc_heuristic(vertex, finish_vertex, graph)
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
    # print(find_adjacent((2, 1),
    #                     [[1888.2200, 2992.222, 453.333], [234.333, 765.987, 762.433], [1234.567, 432.675, 999.999]]))
    # main()

    info = read_csv("/Users/matthewprytula/pythonProject/Pathfinding-project/task1/task1_data/example1.csv")
    graph = info[-1]
    # start = info[0]
    # finish = info[1]
    # print(parsing_info(graph, 2, start, finish))
    # print(find_adjacent((2, 1),
    #                     [[1888.2200, 2992.222, 453.333], [234.333, 765.987, 762.433], [1234.567, 432.675, 999.999]]))
    # main()
    # graph = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5, 3, 6, 2, 7, 345, 7, 34, 346, 46], [23, 4, 6, 3, 55, 474, 2, 45, 3, 0],
             # [3, 4, 346, 44, 33, 4, 632, 63, 466, 34], [34, 34, 83, 422, 745, 55, 30, 35, 63, 97],
             # [45, 6, 2, 545, 73, 2, 7, 245, 747, 4], [46, 4, 3, 1, 27, 4, 7, 74, 42, 54],
             # [54, 4, 72, 27, 227, 25, 70, 2793, 3, 3], [23, 647, 3, 456, 38, 2, 8, 2, 47, 457],
             # [362, 7, 2, 28, 29, 49, 50, 37, 547, 8356]]
    # print(len(graph))
    start = (0, 0)
    finish = (300, 300)
    # print(info)
    print(path_finding(graph, start, finish, 5))
    print("found")
