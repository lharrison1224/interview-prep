def main():
    directed_adj_list = [None]*5
    directed_adj_list[0] = [2, 3]
    directed_adj_list[1] = [0, 4]
    directed_adj_list[2] = [1]
    directed_adj_list[3] = [0, 1]
    directed_adj_list[4] = []

    print("Breadth first starting at 3")
    breadth_first_search(directed_adj_list, 3)
    print("Depth first starting at 2")
    depth_first_search_iterative(directed_adj_list, 2)
    print("Depth first (recursive) starting at 2")
    depth_first_search_recursive(directed_adj_list, 2)


def depth_first_search_recursive(adj_list, starting_node):
    def dfs_helper(adj_list, node, visited):
        visited[node] = True
        print(node)
        for adj in adj_list[node]:
            if visited[adj] == False:
                dfs_helper(adj_list, adj, visited)

    visited = [False] * len(adj_list)
    dfs_helper(adj_list, starting_node, visited)


def depth_first_search_iterative(adj_list, starting_node):
    stack = [starting_node]
    visited = [False] * len(adj_list)
    visited[starting_node] = True
    while stack:
        current_node = stack.pop(0)
        print(current_node)
        for node in adj_list[current_node]:
            if visited[node] == False:
                stack.insert(0, node)
                visited[node] = True


def breadth_first_search(adj_list, starting_node):
    Q = [starting_node]
    visited = [False] * len(adj_list)
    visited[starting_node] = True
    while Q:
        current_node = Q.pop(0)
        print(current_node)
        for node in adj_list[current_node]:
            if visited[node] == False:
                Q.append(node)
                visited[node] = True


if __name__ == "__main__":
    main()
