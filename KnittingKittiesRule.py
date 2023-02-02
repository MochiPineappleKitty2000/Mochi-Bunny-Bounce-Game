import pygame
pygame.init()
sw = 400
sh = 600
#in pixels screenwidth and screenheight
screen = pygame.display.set_mode((sw,sh))
white = (255, 255, 255)
black = (0,0,0)
pygame.display.set_caption("Mochi Bunny Bounce Game")
bgpic = pygame.image.load("sky_with_clouds.jpg").convert_alpha()
bunny = pygame.image.load("bunnyjumping.png").convert_alpha()
#this is the background and player image.
#Class: It is a way for us to store functions 
#that are for a specific purpose. They are like folders.
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(bunny, 45, 45)
        self.height = 25
        self.width = 40
        self.rect = pygame
        self.rect.center = (x, y)
        
    def draw(self):
        screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))
        pygame.draw.rect(screen, white, self.rect, 2)
run = True
#cruella de vil! cruella de vil! doo doo doo doo doo doo doo doo cruella de vil! ️(this does not do anything. do not pay attention to it.)
while run:
    screen.blit(bgpic,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
