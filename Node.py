class Node:
    def __init__(self, data, next_node=None, is_root=False):
        self.data = data
        self.next = next_node
        self.is_root = is_root
        self.chain_length = None

    def print_to_root(self):
        cur_node = self
        while not cur_node.is_root:
            print str(cur_node.data) + "->",
            cur_node = cur_node.next
        print "1"

    def length(self):
        if self.length != None:
            return self.chain_length
        else:
            l = 1
            cur_node = self
            while not cur_node.is_root:
                l += 1
                cur_node = cur_node.next
            return l
