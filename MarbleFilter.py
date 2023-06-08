from FilterNode import *

class MarbleFilter(FilterNode):

    def __init__(self, parent, position, label):
        self.next_nodes = []
        self.in_image_id = [-1, null_image_src]
        self.out_image_id = [-1, null_image_src]

        self.parent = parent
        self.position = position
        self.label = label

    def build(self):
        self.id = dpg.add_node(parent=self.parent, label=self.label, pos=self.position)
        node_builder = NodeBuilder(self.id)

        with dpg.node_attribute(attribute_type=in_attrib, parent=self.id) as self.in_id:
            self.type = dpg.add_radio_button(items=["Grey", "Edges", "Marble"])

        self.out_id = node_builder.add_button(label="run", callback=self.update_image,
                                              width=100, height=30, attrib=out_attrib)[1]

    def do_filter(self):
        with Image.open(self.in_image_id[1]) as img:
            img.load()

        tp = dpg.get_value(self.type)

        if tp == "Grey":
            return img.convert("L")
        elif tp == "Marble":
            img_gray = img.convert("L")
            return img_gray.filter(ImageFilter.SMOOTH).filter(ImageFilter.EMBOSS)
        elif tp == "Edges":
            img_gray = img.convert("L")
            return img_gray.filter(ImageFilter.SMOOTH).filter(ImageFilter.FIND_EDGES)
        else:
            return -1

