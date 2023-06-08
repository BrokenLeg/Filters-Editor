import dearpygui.dearpygui as dpg

class NodeBuilder:

    def __init__(self, node_id):
        self.node_id = node_id

    def deduce_shape(self, attrib):
        if (attrib == dpg.mvNode_Attr_Input):
            return dpg.mvNode_PinShape_QuadFilled
        else:
            return dpg.mvNode_PinShape_TriangleFilled

    def add_slider(self, label, width,  max_value, attrib=dpg.mvNode_Attr_Static):
        with dpg.node_attribute(parent=self.node_id, attribute_type=attrib, shape=self.deduce_shape(attrib)) as pin_id:
            return [dpg.add_slider_float(label=label, width=width, max_value=max_value), pin_id]

    def add_button(self, label, callback, width, height, attrib=dpg.mvNode_Attr_Static, user_data=[]):
        with dpg.node_attribute(parent=self.node_id, attribute_type=attrib, shape=self.deduce_shape(attrib)) as pin_id:
            return [dpg.add_button(label=label, width=width, height=height, callback=callback, user_data=user_data), pin_id]

    def add_color_picker(self, width, attrib=dpg.mvNode_Attr_Static):
        with dpg.node_attribute(parent=self.node_id, attribute_type=attrib, shape=self.deduce_shape(attrib)) as pin_id:
            return [dpg.add_color_picker(width=width, no_alpha=True, no_side_preview=False, no_inputs=True), pin_id]

    def add_file_loader(self, width, height, callback, attrib=dpg.mvNode_Attr_Static):
        with dpg.node_attribute(parent=self.node_id, attribute_type=attrib, shape=self.deduce_shape(attrib)) as pin_id:
            with dpg.file_dialog(directory_selector=False, show=False, callback=callback,
                                 width=width, height=height, modal=True) as image_picker_id:
                dpg.add_file_extension(".*")
                dpg.add_file_extension(".jpg")
                dpg.add_file_extension(".png")

        return [image_picker_id, pin_id]

    def add_image(self, width, height, image, attrib=dpg.mvNode_Attr_Static):
        with dpg.node_attribute(parent=self.node_id, attribute_type=attrib, shape=self.deduce_shape(attrib)) as pin_id:
            return [dpg.add_image(width=width, height=height, texture_tag=image), pin_id]

    def add_input_text(self, label, width, default_value, attrib=dpg.mvNode_Attr_Static):
        with dpg.node_attribute(parent=self.node_id, attribute_type=attrib, shape=self.deduce_shape(attrib)) as pin_id:
            return [dpg.add_input_text(label=label, width=width, default_value=default_value), pin_id]

