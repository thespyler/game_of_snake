import pygame
from pygame.locals import *
import random
import time
pygame.init()
#   height and width
HEIGHT = 800
WIDTH = 600

#   colors

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# CLOCK TO  set FPS(FRAMES PER SECOND)
CLOCK = pygame.time.Clock()

#   create a new text file named as new_High (will be created automatically)
High = open('new_High.txt', 'a')
HighScore_Open = open('new_High.txt')
head = pygame.image.load('head.png')

class App:
    def __init__(self):
        display = pygame.display.set_mode((HEIGHT, WIDTH))
        self.display = display
        pygame.display.set_caption('Snake')
        leadx = HEIGHT // 2
        leady = WIDTH // 2
        leadychange = 0
        leadxchange = 0
        foodx = round(random.randrange(100, HEIGHT) // 10) * 10
        foody = round(random.randrange(100, WIDTH) // 10) * 10
        self.foodx = foodx
        self.foody = foody
        self.leadx = leadx
        self.leady = leady
        self.leadxchange = leadxchange
        self.leadychange = leadychange
        SnakeList = []
        self.SnakeList = SnakeList
        snakelen = 1
        self.snakelen = snakelen
        score = 0
        self.score = score
        self.Scores = []
        for scores in HighScore_Open:
            self.Scores.append(int(scores.replace('\n', '')))
        self.Scores.sort(reverse=True)
        try:
            self.score = self.Scores[0]
        except:
            print('no highscore')

    def drawgrid(self):
        #draw the grid using for loop
        
        for i in range(30):
            pygame.draw.line(self.display, WHITE, (0, i * 30 + i), (HEIGHT, i * 30 + i), 1)
            pygame.draw.line(self.display, WHITE, (i * 30 + i, 0), (i * 30 + i, HEIGHT), 1)

    def gameover(self):
        
        leadx = HEIGHT // 3
        leady =  WIDTH// 2
        x = 30
        y = 100
        while True:
            mouse = pygame.mouse.get_pos()
            display.fill((14, 15, 34))
            self.message('Score = ' + str((self.snakelen - 1) * 5), HEIGHT // 8, WIDTH // 6, 30, (0, 255, 0))
            self.message("Welcome !", HEIGHT // 4, WIDTH // 4, 100, RED)
            self.message('Highscore= ' + str(self.Scores[0]), HEIGHT // 2, WIDTH // 11, 30, (122, 2, 122))
            display.fill((0, 122, 0), rect=[leadx, leady - 5, y, x])
            display.fill((0, 122, 0), rect=[leadx, leady - 5 + y, y, x])
            self.message('Credits', leadx, leady - 10 + y, x - 2, BLACK)
            self.message('Restart', leadx, leady - 10, x - 2, BLACK)
            pygame.display.update()
            for event in pygame.event.get():
                if mouse[0] >= leadx and mouse[0] < leadx + y or\
                        leadx >= mouse[0] and leadx < mouse[0] + y:
                    if mouse[1] >= leady and mouse[1] < leady + x or\
                            leady > mouse[1] and leady <= mouse[1] + x:
                        display.fill((0, 255, 0), rect=[leadx, leady - 5, y, x])

                        if event.type == MOUSEBUTTONDOWN:
                            High.write(str((self.snakelen - 1) * 5) + '\n')
                            self.maybe_i_dont_know()
                            self.snakelen = 1
                            self.leadx = HEIGHT // 2
                            self.leady == WIDTH // 2
                            self.leadxchange = 0
                            self.leadychange = 0
                            main()
                        self.message('Restart', leadx, leady - 10, x - 2, BLACK)
                        pygame.display.update()

                if event.type == QUIT:

                    High.write(str((self.snakelen - 1) * 5) + '\n')
                    High.close()
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == K_c:
                        High.write(str((self.snakelen - 1) * 5) + '\n')
                        self.maybe_i_dont_know()
                        self.snakelen = 1
                        self.leadx = HEIGHT // 2
                        self.leady == WIDTH // 2
                        self.leadxchange = 0
                        self.leadychange = 0
                        main()
                    if event.key == K_q:
                        High.write(str((self.snakelen - 1) * 5) + '\n')
                        High.close()
                        pygame.quit()
                        quit()

    def player(self):
        SnakeHead = []
        SnakeHead.append(self.leadx)
        SnakeHead.append(self.leady)
        self.SnakeList.append(SnakeHead)
        Headx = self.leadx
        Heady = self.leady

        for XnY in self.SnakeList:
            display.fill(WHITE, rect=[XnY[0], XnY[1], 30, 30])
            if len(self.SnakeList) > self.snakelen:
                del (self.SnakeList[0])
        for eachSegment in self.SnakeList[:-1]:
            if eachSegment == SnakeHead:
                self.gameover()

    def food_change(self):
        self.foodx = round(random.randrange(100, HEIGHT) // 30) * 30
        self.foody = round(random.randrange(100, WIDTH) // 10) * 10

    def check_collision(self):
        if self.leadx >= self.foodx and self.leadx <= self.foodx + 30 \
                or self.foodx >= self.leadx and self.foodx < self.leadx + 30:
            if self.leady >= self.foody and self.leady <= self.foody + 30 \
                    or self.foody >= self.leady and self.foody < self.leady + 30:
                self.food_change()
                self.snakelen += 1
        if self.leadx >= HEIGHT:
            self.leadx = 10
        elif self.leadx <= 0:
            self.leadx = HEIGHT - 10
        elif self.leady >= WIDTH:
            self.leady = 10
        elif self.leady <= 0:
            self.leady = WIDTH - 10
  

    def message(self, msg, x, y, sizer, color):
        FONT = pygame.font.SysFont('Comic Sans MS', sizer)
        text = FONT.render(msg, True, color)
        display.blit(text, [x, y])

    def maybe_i_dont_know(self):
        for each_line in HighScore_Open:
            self.Scores.append[int(each_line.replace('\n', ''))]

            print(self.Scores)
            HighScore_Open.close()
            if (self.snakelen - 1) * 5 > self.Scores[0]:
                self.Scoress[0] = (self.snakelen - 1) * 5
  

game = App()
game.maybe_i_dont_know()


def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    game.leadychange = -10
                    game.leadxchange = 0

                elif event.key == K_DOWN or event.key == K_s:
                    game.leadychange = 10
                    game.leadxchange = 0
                    pygame.transform.flip(head, True, True)
                    pygame.display.update()
                elif event.key == K_LEFT or event.key == K_a:
                    game.leadxchange = -10
                    game.leadychange = 0
                	#x = pygame.transform.flip(head, True, False)

                elif event.key == K_RIGHT or event.key == K_d:
                    game.leadxchange = 10
                    game.leadychange = 0


        game.check_collision()
        game.leadx += game.leadxchange
        game.leady += game.leadychange
        display.fill(BLACK)
        game.player()
        game.drawgrid()
        game.check_collision()
        display.fill(RED, rect=[game.foodx, game.foody, 30, 30])
        print(game.score)
        game.message('Score = ' + str((game.snakelen - 1) * 5), HEIGHT // 10, WIDTH // 11, 30, (0, 255, 0))
        try:
            game.message('Highscore= ' + str(game.Scores[0]), HEIGHT // 10, WIDTH // 22, 30, (2, 255, 223))
        except:
            print('game_error')
        pygame.display.update()
        CLOCK.tick(30)


if __name__ == '__main__':
    main()
