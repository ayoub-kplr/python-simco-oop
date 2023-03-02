import treelib


class TreeHandler:
    def __init__(self):
        self.tree = treelib.Tree()

    def generate_tree_hierarchy(self, json_dict):
        # define the tree

        # define the root node
        root_node_id = "root"
        root_node_name = "Product Classes Hierarchy"
        self.tree.create_node(root_node_name, root_node_id)

        # traverse json data and creathe other node
        self.recursive_tree_from_json(json_dict, root_node_id)

        return self.tree

    def recursive_tree_from_json(self, json_dict, parent_node_id):
        for class_name, class_attrs in json_dict.items():
            class_node_id = class_name
            class_node_name = class_name

            # Add the class node to the tree
            self.tree.create_node(class_node_name, class_node_id, parent=parent_node_id)

            # Traverse any subclasses
            if "subclasses" in class_attrs:
                self.recursive_tree_from_json(class_attrs["subclasses"], class_node_id)
