import dearpygui.dearpygui as dpg

null_image_src = "grey.jpg"

out_attrib = dpg.mvNode_Attr_Output
in_attrib = dpg.mvNode_Attr_Input

def load_image(image_src):
    width, height, channels, data = dpg.load_image(image_src)

    with dpg.texture_registry(show=False):
        image_id = dpg.add_static_texture(width=width, height=height, default_value=data)

    return [image_id, image_src]