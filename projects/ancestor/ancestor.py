from util import Stack

def earliest_ancestor(ancestors, starting_node):

    # Convert list of tuples into graph of parent relationship
    vertices = {}
    for a in ancestors:
        if a[1] not in vertices:
            vertices[a[1]] = set()
        vertices[a[1]].add(a[0])

    paths = []

    def find_all_paths_to_ancestors(child, path=None):
        if path is None:
            path = []

        path.append(child)

        if child not in vertices:
            paths.append(path)
            return
        else:
            for parent in vertices[child]:
                path_copy = path.copy()
                find_all_paths_to_ancestors(parent, path_copy)

    find_all_paths_to_ancestors(starting_node)
    current_max_length = 0
    current_id = 0

    for p in paths:
        if len(p) > current_max_length:
            current_max_length = len(p)
            current_id = p[-1]

        elif len(p) == current_max_length:
            if p[-1] < current_id:
                current_id = p[-1]

    if current_id == starting_node:
        return -1
    return current_id


def earliest_ancestor_iterative(ancestors, starting_node):
    s = Stack()

    vertices = {}
    for a in ancestors:
        if a[1] not in vertices:
            vertices[a[1]] = set()
        vertices[a[1]].add(a[0])

    paths = []

    s.push([starting_node])

    while s.size() > 0:
        path = s.pop()
        child = path[-1]

        if child not in vertices:
            paths.append(path)
        else:
            for parent in vertices[child]:
                new_path = path.copy()
                new_path.append(parent)
                s.push(new_path)

    current_max_length = 0
    current_id = 0

    for p in paths:
        if len(p) > current_max_length:
            current_max_length = len(p)
            current_id = p[-1]

        elif len(p) == current_max_length:
            if p[-1] < current_id:
                current_id = p[-1]

    if current_id == starting_node:
        return -1
    return current_id


"""
{3: {1, 2}, 6: {3, 5}, 7: {5}, 5: {4}, 8: {11, 4}, 9: {8}, 1: {10}}


   10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
"""
