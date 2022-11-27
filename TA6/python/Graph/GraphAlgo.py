import heapq
import json
import math
import random
from typing import List
from DiGraph import DiGraph


class Trio:
    def __init__(self, prev: int, to: int):
        """
        This class is used in the priority queue to save the previous Node
        """
        self.prev: int = prev
        self.to: int = to

    def __lt__(self, other):
        return self


class Father:
    def __init__(self, prev: int, weight: float):
        """
        This class is used to save the previous node and current route weight
        """
        self.prev: int = prev
        self.weight: float = weight


def swap(j, i, li):
    """
    Swaps between two elements in a list
    """
    tmp = li[j]
    li[j] = li[i]
    li[i] = tmp


class GraphAlgo:

    def __init__(self, graph=1):
        """
        Initiates an algo
        """
        if graph != 1:
            self.graph = graph
        else:
            self.graph = DiGraph()

    def get_graph(self):
        """
        Returns the graph used in the algo
        """
        return self.graph

    def load_from_json(self, f: str) -> bool:
        """
        Loads a graph from a json file and initiates it.
        """
        self.graph = DiGraph()
        with open("../Data/" + f, "r") as fp:
            data = json.load(fp)
        nodes = data["Nodes"]
        for i in nodes:
            try:
                self.graph.add_node(i["id"], i["pos"].split(","))
            except:
                self.graph.add_node(i["id"], (random.randint(0, 10), random.randint(0, 10), 0.0))
        edges = data["Edges"]
        for i in edges:
            self.graph.add_edge(i["src"], i["dest"], (i["w"]))
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves a graph to a json file.
        """
        try:
            with open(file_name, "x") as new_file:
                new_file.write(json.dumps(self.parse_to_json(), indent=4))
            new_file.close()
            return True
        except Exception as exp:
            print(exp)
            return False

    def parse_to_json(self):
        """
        Parses a current graph information to a json string
        """
        nodes_d = self.get_graph().get_all_v()
        Nodes = []  # List of all the Nodes that will be added to the json file
        Edges = []  # List of all the Edges that will be added to the json file
        for node in nodes_d:  # Add each Node
            curr_node_data = nodes_d.get(node)
            curr_id = node
            out_edges = self.get_graph().all_out_edges_of_node(curr_id)
            for edge in out_edges.keys():  # Add each Edge
                src = curr_id
                dest = edge
                weight = out_edges.get(edge)
                # change the format into a json format
                curr_edge = {"src": src, "w": weight, "dest": dest}
                Edges.append(curr_edge)
            pos = curr_node_data.get_pos()
            X = str(pos[0])
            Y = str(pos[1])
            Z = str(pos[2])
            # change the format into a json format
            curr_node_data = {"pos": (X + "," + Y + "," + Z), "id": curr_id}
            Nodes.append(curr_node_data)
        json_dict = {"Edges": Edges, "Nodes": Nodes}  # Add all to main dict
        # print("DICT:\n")
        # print(json_dict)
        return json_dict


g = GraphAlgo()
g.load_from_json('T1.json')
print(g.graph)
g.save_to_json('newT1.json')




