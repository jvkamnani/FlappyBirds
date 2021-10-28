from Pipe import Pipe

GAP_HEIGHT = 90

class PipePair:
    def __init__(self, display_width, display_height, y_upper):
        self.lower_pipe = Pipe(display_width, display_height)
        self.upper_pipe = Pipe(display_width, display_height)
        self.upper_pipe.flip_vertically()
        self.upper_pipe.set_y(y_upper)
        self.lower_pipe.set_y(GAP_HEIGHT + y_upper + self.lower_pipe.height)
        
    def render(self, gameDisplay):
        self.lower_pipe.render(gameDisplay)
        self.upper_pipe.render(gameDisplay)
    
    def update(self, dt):
        self.lower_pipe.update(dt)
        self.upper_pipe.x = self.lower_pipe.x

    def check_out_of_bounds(self):
        if self.lower_pipe.check_out_of_bounds() and self.upper_pipe.check_out_of_bounds():
            return True
        else:
            False


