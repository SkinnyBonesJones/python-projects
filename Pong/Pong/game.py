import pygame, time, random
from Paddle import *
from Ball import *


class Pong:
    pygame.init()
    playerScore = 0
    enemyScore = 0
    def __init__(self):
        self.width = 900
        self.height = 600

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("This is fucking dumb")
        self.clock = pygame.time.Clock()
        self.icon = pygame.image.load("start.png")
        pygame.display.set_icon(self.icon)

        self.font = pygame.font.Font("bit5x3.ttf", 30)


        self.ball1 = Ball(int(self.width/2), int(self.height/2), 10, (255, 0, 0), 2, 45, self.screen)
        self.player = Paddle((255, 255,255), 25, 0, 15, self.height * 0.25, 0, self.screen)
        self.enemy = Paddle((255, 255,255), self.width - 30, int(self.height/2), 15, self.height * 0.25, 0, self.screen)

    def onScore(self, whoScored):
        score = True
        if whoScored == 0:
            self.playerScore += 1
            text = self.font.render("YOU SCORED!", True,(255, 255, 255), (0, 0, 0))
        elif whoScored == 1:
            self.enemyScore += 1
            text = self.font.render("OPPONENT SCORED!", True, (255, 255, 255), (0, 0, 0))

        t_end = time.time() + 2
        while time.time() < t_end and score == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.screen.blit(text, (self.width/2 - 110, 100))

            newFont = pygame.font.Font("bit5x3.ttf", 40)

            playerScore = newFont.render(str(self.playerScore), True, (255, 255, 255), (0, 0, 0))
            enemyScore = newFont.render(str(self.enemyScore), True, (255, 255, 255), (0, 0, 0))
            self.screen.blit(enemyScore, (self.width / 2 + 50, 50))
            self.screen.blit(playerScore, (self.width / 2 - 60, 50))

            pygame.display.update()
        text = self.font.render("OPPONENT SCORED!", True ,(0, 0, 0), (0, 0, 0))
        self.screen.blit(text, (self.width/2 - 110, 100))


    def readyStart(self):
        t_end = time.time() + 2
        ready = self.font.render("READY?", True, (255, 255, 255), (0, 0, 0))
        while time.time() < t_end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.blit(ready, (self.width/2 - 50, 100))

            pygame.display.update()

    def gameOver(self):
        gameOver = True
        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameOver = False
                        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.height))
                        pygame.display.update()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

            if(self.playerScore >= 10):
                textEnd = self.font.render("You Won!", True, (255, 255, 255), (0, 0, 0) )
            elif(self.enemyScore >= 10):
                textEnd = self.font.render("You Lost!", True, (255, 255, 255), (0, 0, 0) )

            self.playerScore = 0
            self.enemyScore = 0
            playAgain = self.font.render("Press SPACE to play again or ESC to quit", True, (255, 255, 255), (0, 0, 0) )

            self.screen.blit(textEnd, (self.width/2 - 65, self.height/2))
            self.screen.blit(playAgain, (self.width/2 - 300, self.height/2 + 50))


            pygame.display.update()

    def pause(self):
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        pause = False
            text = self.font.render("FUCK YOU", True, (255, 255, 255), (0, 0, 0))
            unpause = self.font.render("press P to unpause", True, (255, 255, 255), (0, 0, 0))

            self.screen.blit(text, (self.width/2 - 50, self.height/2))
            self.screen.blit(unpause, (self.width/2 - 125, self.height/2 + 50) )

            pygame.display.update()




    def playGame(self):
        randomDir = random.choice([45, 135, 225, 315])
        self.ball1 = Ball(int(self.width / 2), int(self.height / 2), 10, (255, 0, 0), 2, randomDir, self.screen)
        self.enemy = Paddle((255, 255, 255), 25, int(self.height/2 - self.player.height/2), 15, self.height * 0.25, self.playerScore, self.screen)
        self.player = Paddle((255, 255, 255), self.width - 30, int(self.height /2 - self.player.height/2), 15, self.height * 0.25, self.enemyScore,self.screen)

        self.screen.fill((0, 0, 0))
        pygame.display.update()
        self.readyStart()
        started = 0
        game = True
        while game:
            #clicking X button
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause()

            self.screen.fill((0,0,0))

            pygame.time.delay(1)

            for x in range(0, self.height, 40):
                #print("fuck")
                pygame.draw.rect(self.screen, (255, 255, 255), (self.width/2 - 6, x, 12, 20))
            self.player.draw()
            self.ball1.draw()
            self.enemy.draw()



            if started == 1:
                time.sleep(1)
                started = 2
            if(started == 0):
                started = 1



            newFont = pygame.font.Font("bit5x3.ttf", 40)

            playerScore = newFont.render(str(self.playerScore), True, (255, 255, 255), (0, 0, 0))
            enemyScore = newFont.render(str(self.enemyScore), True, (255, 255, 255), (0, 0, 0))

            self.screen.blit(playerScore, (self.width/2 - 60, 50))
            self.screen.blit(enemyScore, (self.width/2 + 50, 50))


            self.enemy.enemyAI(2, self.ball1, self.width, self.height)
            self.ball1.move(self.height, self.width)

            self.ball1.collisions(self.player)
            self.ball1.collisions(self.enemy)

            mx, my = pygame.mouse.get_pos()
            m = pygame.mouse.get_pressed()

            if(my > self.player.height/2 and my < self.height - (self.player.height / 2)):
                self.player.y = my - self.player.height/2

            if(self.ball1.x < -self.ball1.radius * 2):
                game = False
                self.onScore(1)
                if (self.playerScore >= 10 or self.enemyScore >= 10):
                    self.gameOver()
                    self.playGame()
                else:
                    self.playGame()
            elif(self.ball1.x > self.width + (self.ball1.radius * 2)):
                game = False
                self.onScore(0)
                if (self.playerScore >= 10 or self.enemyScore >= 10):
                    self.gameOver()
                    self.playGame()
                else:
                    self.playGame()



            pygame.display.update()

game = Pong()
game.playGame()