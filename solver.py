def solver(connections):
    path = [0]
    visited = [0]
    first_try = True

    while not(len(path) == 1 or path[-1] == (len(connections) - 1)) or first_try:
        possible_steps = connections[path[-1]]
        node_to_add = None

        for step in possible_steps:
            if step[-1] not in visited:
                node_to_add = step[-1]

        if node_to_add == None:
            path.pop(-1)

        else:
            path.append(node_to_add)
            visited.append(node_to_add)

        if first_try:
            first_try  = False
        #print(path)
    return path

def recursively_solve(start, connections, visited, path):
    if start == len(connections) - 1:
        path.append(start)
        return True

    else:
        next_steps = []
        for connection in connections[start]:
            if connection[-1] not in visited:
                visited.append(connection[-1])
                next_steps.append(recursively_solve(connection[-1], connections, visited, path))

        if True in next_steps:
            path.append(start)
            if start == 0:
                return path
            return True

        else:
            return False

if __name__ == "__main__":
    connections = [[(0, 1), (0, 3)], [(1, 0), (1, 2), (1, 4)], [(2, 1), (2, 5)], [(3, 0), (3, 6)], [(4, 5), (4, 1)], [(5, 4), (5, 2)], [(6, 3), (6, 7)], [(7, 6), (7, 8)], [(8, 7)]]
    print(recursively_solve(0, connections, [0], []))
