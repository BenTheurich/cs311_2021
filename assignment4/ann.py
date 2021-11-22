#Artificial Neural Network

import random
import string

NODE_COUNT_PER_LAYER = [4,3,2]

class Node:
    def __init__(self):
        self.children = []
        self.weight = []
        self.node_name = ''.join([random.choice(string.ascii_uppercase) for i in range(2)])

    def make_children(self, current_layer_number, node_per_layer_map):
        if current_layer_number >= len(node_per_layer_map):
            return

        for i in range(node_per_layer_map[current_layer_number]):
            self.children.append(Node())
        
        self.children[0].make_children(current_layer_number + 1, node_per_layer_map)
        
        for i in range(1, len(self.children)):
                self.children[i].children = self.children[0].children[:]


    def pretty_print(self, current_layer_number, node_per_layer_map):

        indent = '    ' * current_layer_number
        if current_layer_number >= len(node_per_layer_map):
            print(f"{indent} {self.node_name}")
            return
        
        print(f"{indent} {self.node_name} is connected to:")
        for i in range(len(self.children)):
            self.children[i].pretty_print(current_layer_number + 1, node_per_layer_map)
            try:
                print(f"{indent} with weight {self.weight[i]}")
            except:
                pass 
        return

    def set_random_weights(self, current_layer_number, node_per_layer_map):
        if current_layer_number >= len(node_per_layer_map):
            return
        self.weight = [0.0] * len(self.children)
        for i in range(len(self.children)):
            self.weight[i] = random.uniform(0,1)
            self.children[i].set_random_weights(current_layer_number + 1, node_per_layer_map)
        return

new_node = Node()

new_node.make_children(0, NODE_COUNT_PER_LAYER)

new_node.pretty_print(0, NODE_COUNT_PER_LAYER)

print("AFTER WEIGHTS")

new_node.set_random_weights(0, NODE_COUNT_PER_LAYER)

new_node.pretty_print(0, NODE_COUNT_PER_LAYER)
