class ClassHandler:
    def __init__(self):
        pass

    def generate_class_def(self, class_name: str, attrs: dict, superclass_name: str, superclass_args: list):
        if superclass_args is None:
            superclass_args = []
        constructor_args = []
        constructor_def = ""
        has_attributes = False

        class_template = f"class {class_name}"

        if superclass_name:
            class_template += f"({superclass_name})"

        class_template += ":\n"

        for attr_name, attr_val in attrs.items():
            if attr_name != "subclasses":
                has_attributes = True
                constructor_args.append(attr_name)
                constructor_def += f"\n\t\tself.{attr_name} = {attr_name}"

        if has_attributes:
            constructor_template = f"\tdef __init__(self, {', '.join(constructor_args + superclass_args)}):"

            if len(superclass_args) > 0:
                constructor_template += f"\n\t\tsuper().__init__({', '.join(superclass_args)})"

            constructor_template += constructor_def

        else:
            if len(superclass_args) > 0:
                constructor_template = f"\tdef __init__(self, {', '.join(superclass_args)}):"
                constructor_template += f"\n\t\tsuper().__init__({', '.join(superclass_args)})"

            else:
                constructor_template = "\tpass"

        return class_template + constructor_template + "\n\n"

    def generate_class_hierarchy(self, json_dict: dict, superclass_name: str = None, superclass_args: list = []):
        class_defs = ""

        for class_name, class_attrs in json_dict.items():

            class_def = self.generate_class_def(class_name, class_attrs, superclass_name, superclass_args)
            class_defs += class_def

            if "subclasses" in class_attrs:
                super_attr = (list(class_attrs.keys()) + superclass_args)
                super_attr.remove("subclasses")
                subclass_defs = self.generate_class_hierarchy(class_attrs["subclasses"], class_name, super_attr)
                class_defs += subclass_defs
        print(class_defs)
        return class_defs
