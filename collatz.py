from Node import Node

def collatz(node, graph):
    if node.data % 2 == 0:
        next_node_data = node.data / 2
    else:
        next_node_data = 3 * node.data + 1

    for i in range(0, len(graph)):
        if next_node_data == graph[i].data:
            node.next = graph[i]
            return node
    node.next = collatz(Node(next_node_data), graph)
    return node

def gen_collatz_chains(n):
    root = Node(1, is_root=True)
    graph = [root]
    for n in range(1, n+1):
        node = Node(n)
        graph.append(collatz(node, graph))
    return graph

if __name__ == "__main__":
    chains = gen_collatz_chains(5)

    for chain in chains:
        chain.print_to_root()
