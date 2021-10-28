import pygame
class Bird:
    def __init__(self, disaplay_width, display_height):
        self.image = pygame.image.load('D:/Flappy Birds/assets/sprites/bird.png')
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]

        self.x = disaplay_width / 2 - (self.width / 2)
        self.y = display_height / 2 - (self.height / 2)
        self.g = 20
        self.dy = 0
    def render(self, gameDisplay):
        gameDisplay.blit(self.image, (self.x, self.y))
    
    def update(self, dt):
        self.dy = self.dy + self.g * dt
        self.y = self.y + self.dy
    def jump(self):
        self.dy = -5


        