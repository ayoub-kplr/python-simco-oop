from handlers.class_handler import ClassHandler
from handlers.file_hanlder import *
from handlers.tree_hanlder import TreeHandler


def sep():
    print("====================\n")


# Handlers
class_handler = ClassHandler()
tree_handler = TreeHandler()

# Loading json file
json_dict = load_json_file()

sep()
class_hierarchy_code = class_handler.generate_class_hierarchy(json_dict)
sep()

#########


write_content(class_hierarchy_code, "product_classes.py")

print(class_hierarchy_code)

#########

tree_handler.generate_tree_hierarchy(json_dict).show()
