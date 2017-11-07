import global_parameters
from pico2d import *

class tile:
    size_x, size_y = global_parameters.tile_size_x, global_parameters.tile_size_y
    move_x, move_y = 0, 0

    def __init__(self, name, state, x_local, y_local):
        if(state):
            self.img = load_image(name)
        self.state = state
        self.m_x = x_local
        self.m_y = y_local

    def draw(self):
        self.img.draw(self.m_x, self.m_y
                      , tile.size_x, tile.size_y)
        pass

    def update(self, camera_x, camera_y):
        self.m_x += camera_x
        self.m_y += camera_y
        pass
