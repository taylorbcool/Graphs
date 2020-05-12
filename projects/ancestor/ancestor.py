
def earliest_ancestor(ancestors, starting_node):
    # need dict to hold parent child pairs
    ancestors_dict = dict()
    # for each pair in ancestors
        # if child in dict
            # append parent
        # else add child and parent
    for parent, child in ancestors:
        if child in ancestors_dict:
            ancestors_dict[child].append(parent)
        else:
            ancestors_dict[child] = [parent]

    # if starting_node isn't in ancestors
        # return -1
    if starting_node not in ancestors_dict:
        return -1

    # create list paths to hold list of traversal paths
    paths = [[starting_node]]
    
    # for item in paths
        # another list to hold the child's parents
        # for item in list
            # if child in list
                # extend list with dict[child]
        # after iteration, if length of parents > 0
            # append list to paths
    for path in paths:
        parents = []
        for child in path:
            if child in ancestors_dict:
                parents.extend(ancestors_dict[child])
        if len(parents) > 0:
            paths.append(parents)

    # find the end value of the longest path
    return min(paths[-1])