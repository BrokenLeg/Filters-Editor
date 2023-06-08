from Window import *
from FilterNode import *
import shutil
import os

path = './temp'
save_path = './results'
try:
    os.mkdir(path)
    os.mkdir(save_path)
except:
    pass

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720

dpg.create_context()
dpg.create_viewport(title="Filter Editor", width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

w = Window(SCREEN_WIDTH, SCREEN_HEIGHT)

dpg.set_primary_window(w.id, True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

shutil.rmtree(path)
