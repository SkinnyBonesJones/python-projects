import math, pygame

class Paddle:
    def __init__(self, color, x, y, width, height, score, screen):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.score = 0
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def enemyAI(self, speed, Ball, width, height):
        if(self.y <= 0):
            self.y += 1
        if(self.y >= height - self.height):
            self.y -= 1
        if(Ball.x >= width/4 and self.y > 0 and self.y < height - (self.height) ):
            #print(self.y)
            #print(f"Ball X: {Ball.x} and Ball Y: {Ball.y}")
            if(Ball.y > self.y + self.height / 2):
                self.y +=speed/2.5

            if(Ball.y < self.y + self.height/2):
                self.y -= speed/2.5