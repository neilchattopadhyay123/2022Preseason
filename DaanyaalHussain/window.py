import pygame
size = [500,500]
print("works")
screen = pygame.display.set_mode((size),pygame.RESIZABLE)
pygame.display.flip()
pygame.display.set_caption("Interface")
pygame.font.init()
font = pygame.font.SysFont('aerial', 40)

screen.blit(font.render('Daanyaal Hussain', True, (250,250,0)), (0,0))
screen.blit(font.render('Grade 9.', True, (0,250,0)), (0,30))
screen.blit(font.render('Daanyaal Hussain is a Freshman.', True, (0,0,250)), (0,60))
pygame.display.update()

while True:
  pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
