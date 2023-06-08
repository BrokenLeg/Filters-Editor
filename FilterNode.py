from PIL import Image, ImageFilter
from NodeBuilder import *
from FilterUtils import *

class FilterNode:

    def do_filter(self) -> Image.Image:
        pass

    def build(self) -> None:
        pass

    def update_image(self) -> None:
        out_img = self.do_filter()
        if out_img != -1:
            out_img.save(f"temp/out{self.id}.png", "PNG")
            image_id, image_src = load_image(f"temp/out{self.id}.png")
            self.out_image_id = [image_id, image_src]
        else:
            self.out_image_id = self.in_image_id

        if (self.out_image_id[0] != -1):
            for node in self.next_nodes:
                if (dpg.does_item_exist(node.id)):
                    node.in_image_id = self.out_image_id
                    node.update_image()


