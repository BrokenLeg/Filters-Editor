from FilterUtils import *
from PIL import Image
from NodeBuilder import *

class ImageNodeOut:

    def __init__(self, parent, position, label, image_id):

        self.next_nodes = []
        self.out_image_id = [image_id, "grey.jpg"]
        self.in_id = -1


        self.parent = parent
        self.position = position
        self.label = label
        self.image_id = image_id

    def build(self):
        self.id = dpg.add_node(parent=self.parent, label=self.label, pos=self.position)
        node_builder = NodeBuilder(self.id)
        self.image_widget_id, self.out_id = node_builder.add_image(width=200, height=200, image=self.image_id,
                                                                   attrib=out_attrib)
        self.image_picker_id = node_builder.add_file_loader(width=500, height=400, callback=self.load_image_to_node)[0]
        node_builder.add_button(label="load", width=200, height=30,
                                callback=lambda: dpg.configure_item(self.image_picker_id, show=True))

    def load_image_to_node(self, sender, app_data):
        image_id, image_src = load_image(*app_data['selections'])
        self.out_image_id = [image_id, image_src]
        self.update_image()

    def update_image(self):
        dpg.configure_item(self.image_widget_id, texture_tag=self.out_image_id[0])

        for node in self.next_nodes:
            if (dpg.does_item_exist(node.id)):
                node.in_image_id = self.out_image_id
                node.update_image()

class ImageNodeIn:

    def __init__(self, parent, position, label, image_id):

        self.in_image_id = [image_id, "grey.jpg"]
        self.out_id = []
        self.save_count = 0

        self.parent = parent
        self.position = position
        self.label = label
        self.image_id = image_id

    def build(self):
        self.id = dpg.add_node(parent=self.parent, label=self.label, pos=self.position);
        node_builder = NodeBuilder(self.id)
        self.image_widget_id, self.in_id = node_builder.add_image(width=200, height=200, image=self.image_id,
                                                                  attrib=in_attrib)
        self.save_filename = node_builder.add_input_text(label="savename", width=130, default_value="save")[0]
        node_builder.add_button(label="save", width=200, height=30, callback=self.save_image)

    def save_image(self):
        with Image.open(self.in_image_id[1]) as img:
            img.load()

        img.save(f"results/" + dpg.get_value(self.save_filename) + ".png", "PNG");
        self.save_count += 1

    def update_image(self):
        dpg.configure_item(self.image_widget_id, texture_tag=self.in_image_id[0])

