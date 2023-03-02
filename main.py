from handlers import *


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

write_content(class_hierarchy_code, "product_classes.py")

tree_handler.generate_tree_hierarchy(json_dict).show()
