import math, pygame


class Ball:
    def __init__(self, x, y, radius, color, speed, dir, screen):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.dir = dir
        self.screen = screen
        self.MAXBOUNCEANGLE = 140
        self.MINBOUNCEANGLE = 5

    def draw(self,):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), self.radius)

    def move(self, height, width):
        moveTo = (math.sin(math.radians((self.dir))), math.cos(math.radians((self.dir))))
        self.x += moveTo[0] * self.speed
        self.y += moveTo[1] * self.speed

        # bouncing off walls
        if self.y >= height or self.y <= 0:
            newDir = 180 - self.dir
            if(newDir < 0):
                newDir = 360 + newDir
                self.dir = newDir
            else:
               self.dir = 180 - self.dir
        # if self.x >= width or self.x <= 0:
        #     #print(f" WALLS direction before: {self.dir}")
        #     newDir = 360 - self.dir
        #     if(newDir < 0):
        #         newDir = 360 + newDir
        #         self.dir= newDir
        #     else:
        #         self.dir = 360 - self.dir
        #     #print(f"WALLS direction after: {self.dir}")

    def collisions(self, Paddle):
        # bouncing off paddles
        if (self.x >= Paddle.x and self.x <= Paddle.x + Paddle.width and self.y >= Paddle.y and self.y <= Paddle.y + Paddle.height):
            #print(self.dir)
            relativeIntersect = (Paddle.y + Paddle.height / 2) - self.y

            relativeIntersectNormalized = relativeIntersect / Paddle.height / 2

            bounceAngle = relativeIntersectNormalized * self.MAXBOUNCEANGLE
            self.speed = math.fabs(relativeIntersectNormalized) + 1.5

            if (self.dir > 180):
                self.x += Paddle.width + 5
                self.dir = 90 + bounceAngle + self.MINBOUNCEANGLE
            elif (self.dir < 180):
                self.x -= Paddle.width + 5
                self.dir = 270 - bounceAngle - self.MINBOUNCEANGLE
