from FilterNode import *

class ColorBlendFilter(FilterNode):

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
        self.color_value, self.in_id = node_builder.add_color_picker(150, attrib=in_attrib)
        self.blending_value = node_builder.add_slider(label="blend", width=100, max_value=1.0)[0]
        self.out_id = node_builder.add_button(label="run", callback=self.update_image, width=100, height=30,
                                              attrib=out_attrib)[1]

    def do_filter(self):
        with Image.open(self.in_image_id[1]) as img:
            img.load()

        color = dpg.get_value(self.color_value)
        blend_color = (int(color[0]), int(color[1]), int(color[2]))

        blend_img = Image.new("RGBA", img.size, color=blend_color)
        return Image.blend(img.convert("RGBA"), blend_img, dpg.get_value(self.blending_value))