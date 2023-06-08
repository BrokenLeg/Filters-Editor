import dearpygui.dearpygui as dpg
from ImageNode import ImageNodeIn, ImageNodeOut
from BlurFilter import  BlurFilter
from RotateFilter import  RotateFilter
from ColorBlendFilter import  ColorBlendFilter
from ImageBlendFilter import  ImageBlendFilter
from MarbleFilter import MarbleFilter

class FiltersFactory:

    def __init__(self, window):
        self.window = window

    def add_node(self):
        pass

class BlurFactory(FiltersFactory):

    def add_node(self):
        window = self.window
        node_editor_id = window.node_editor_id
        null_image = window.null_image
        pos = dpg.get_item_pos(window.popup_id)

        return BlurFilter(node_editor_id, pos, "Blur")

class RotateFactory(FiltersFactory):

    def add_node(self):
        window = self.window
        node_editor_id = window.node_editor_id
        null_image = window.null_image
        pos = dpg.get_item_pos(window.popup_id)

        return RotateFilter(node_editor_id, pos, "Rotate")

class ColorBlendFactory(FiltersFactory):

    def add_node(self):
        window = self.window
        node_editor_id = window.node_editor_id
        null_image = window.null_image
        pos = dpg.get_item_pos(window.popup_id)

        return ColorBlendFilter(node_editor_id, pos, "Blend")

class ImageBlendFactory(FiltersFactory):

    def add_node(self):
         window = self.window
         node_editor_id = window.node_editor_id
         null_image = window.null_image
         pos = dpg.get_item_pos(window.popup_id)

         return ImageBlendFilter(node_editor_id, pos, "Blend", null_image)

class OutputFactory(FiltersFactory):

    def add_node(self):
        window = self.window
        node_editor_id = window.node_editor_id
        null_image = window.null_image
        pos = dpg.get_item_pos(window.popup_id)

        return ImageNodeIn(node_editor_id, pos, "Output", null_image)

class InputFactory(FiltersFactory):

    def add_node(self):
        window = self.window
        node_editor_id = window.node_editor_id
        null_image = window.null_image
        pos = dpg.get_item_pos(window.popup_id)

        return ImageNodeOut(node_editor_id, pos, "Input", null_image)

class MarbleFactory(FiltersFactory):

    def add_node(self):
        window = self.window
        node_editor_id = window.node_editor_id
        null_image = window.null_image
        pos = dpg.get_item_pos(window.popup_id)

        return MarbleFilter(node_editor_id, pos, "Marble")
