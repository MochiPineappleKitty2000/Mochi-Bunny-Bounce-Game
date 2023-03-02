import pygame

#initialise pygame
pygame.init()

#game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mochi Bunny Bounce Game')

#define colours
WHITE = (255, 255, 255)

#load images
bunny_image = pygame.image.load('bunnyjumping.png').convert_alpha()
bg_image = pygame.image.load('sky_with_clouds.jpg').convert_alpha()


#player class
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(bunny_image, (70, 70))
	    self.width = 45
	    self.height = 55
	    self.rect = pygame.Rect(0, 0, self.width, self.height)
	    self.rect.center = (x, y)

    def draw(self):
	screen.blit(self.image, (self.rect.x - 12, self.rect.y - 5))
		pygame.draw.rect(screen, WHITE, self.rect, 2)
		
    def move(self):
        dx = 0
        dy = 0
        #process keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx = -10
            self.flip = True
        if key[pygame.K_a]:
            dx = 10
            self.flip = False
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

bunny = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

#game loop
run = True
while run:
    #draw background
    screen.blit(bg_image, (0, 0))
	
    #draw sprites
    bunny.draw()


    #event handler
    for event in pygame.event.get():
	if event.type == pygame.QUIT:
	    run = False


    #update display window
    pygame.display.update()



pygame.quit()
