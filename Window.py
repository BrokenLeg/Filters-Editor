from FilterUtils import *
from NodesManager import NodesManager
from FiltersFactory import  *

class Window:
    def __init__(self, width, height):
        self.nodes = []
        self.images = []
        self.null_image = 0
        self.manager = NodesManager(self)

        self.marble_factory = MarbleFactory(self)
        self.blur_factory = BlurFactory(self)
        self.rotate_factory = RotateFactory(self)
        self.color_blend_factory = ColorBlendFactory(self)
        self.image_blend_factory = ImageBlendFactory(self)
        self.output_factory = OutputFactory(self)
        self.input_factory = InputFactory(self)

        self.build_window(width=width, height=height)
        self.build_popup()
        self.register_callbacks()

        self.null_image = load_image("grey.jpg")[0]

    def build_window(self, width, height):
        with dpg.window(width=width, height=height, pos=[0, 0], no_title_bar=True) as self.id:
            self.node_editor_id = dpg.add_node_editor(tag="NEW", callback=self.manager.link_callback,
                                                      delink_callback=self.manager.delink_callback)

    def register_callbacks(self):
        with dpg.handler_registry():
            dpg.add_mouse_click_handler(button=dpg.mvMouseButton_Right,
                                        callback=lambda: dpg.configure_item(self.popup_id, show=True))
            dpg.add_key_down_handler(key=dpg.mvKey_Delete, callback=self.manager.delete_node)

    def build_popup(self):
        with dpg.window(autosize=True, modal=False, popup=True, no_title_bar=True,
                        show=False, pos=[100, 100]) as self.popup_id:
            with dpg.menu(label="Filters"):
                dpg.add_button(label="Marble", width=75, callback=self.add_node, user_data=self.marble_factory)
                dpg.add_button(label="Blur", width=75, callback=self.add_node, user_data=self.blur_factory)
                dpg.add_button(label="Rotate", width=75, callback=self.add_node, user_data=self.rotate_factory)

                dpg.add_spacer()
                dpg.add_separator()
                with dpg.menu(label="Blending"):
                    dpg.add_button(label="Color", width=75, callback=self.add_node, user_data=self.color_blend_factory)
                    dpg.add_button(label="Image", width=75, callback=self.add_node, user_data=self.image_blend_factory)

            dpg.add_separator()
            dpg.add_spacer()
            dpg.add_button(label="Input", width=75, callback=self.add_node, user_data=self.input_factory)
            dpg.add_button(label="Output", width=75, callback=self.add_node, user_data=self.output_factory)

    def add_node(self, sender, app_data, factory):
        new_node = factory.add_node()
        new_node.build()
        self.nodes.append(new_node)

        dpg.configure_item(self.popup_id, show=False)

