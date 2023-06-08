from FilterNode import *

class ImageBlendFilter(FilterNode):

    def __init__(self, parent, position, label, image_id):
        self.next_nodes = []
        self.in_image_id = [image_id, null_image_src]
        self.out_image_id = [image_id, null_image_src]
        self.blend_image = [image_id, null_image_src]

        self.parent = parent
        self.position = position
        self.label = label
        self.image_id = image_id

    def build(self):
        self.id = dpg.add_node(parent=self.parent, label=self.label, pos=self.position)
        node_builder = NodeBuilder(self.id)
        self.image_widget_id, self.in_id = node_builder.add_image(width=100, height=100,
                                                                  image=self.image_id, attrib=in_attrib)
        self.image_picker_id, pin = node_builder.add_file_loader(width=500, height=400,
                                                                 callback=self.load_blend_image_to_node)
        self.blending_value = node_builder.add_slider(label="blend", max_value=1.0, width=100)[0]
        node_builder.add_button(label="load", width=100, height=30, callback=lambda : dpg.configure_item(self.image_picker_id, show=True))
        self.out_id = node_builder.add_button(label="run", callback=self.update_image, width=100, height=30,
                                              attrib=out_attrib)[1]

    def load_blend_image_to_node(self, sender, app_data):
        image_id, image_src = load_image(*app_data['selections'])
        self.blend_image = [image_id, image_src]
        self.update_blend_image()

    def update_blend_image(self):
        dpg.configure_item(self.image_widget_id, texture_tag=self.blend_image[0])

    def do_filter(self):
        with Image.open(self.in_image_id[1]) as img:
            img.load()

        with Image.open(self.blend_image[1]) as blend_img:
            blend_img.load()

        print(self.in_image_id, self.out_image_id)

        if (blend_img.size == img.size):
            try:
                out = Image.blend(img.convert("RGB"), blend_img.convert("RGB"), dpg.get_value(self.blending_value))
                return out
            except:
                pass
        else:
            print("bebe")
            return -1
