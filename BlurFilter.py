from FilterNode import *

class BlurFilter(FilterNode):

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
        self.blur_value, self.in_id = node_builder.add_slider("blur", 100, 30, in_attrib)
        self.out_id = node_builder.add_button(label="run", callback=self.update_image,
                                              width=100, height=30, attrib=out_attrib)[1]

    def do_filter(self):
        with Image.open(self.in_image_id[1]) as img:
            img.load()

        return img.filter(ImageFilter.GaussianBlur(dpg.get_value(self.blur_value)))