from xml.sax import parse

import pygame
pygame .init()
dis=pygame.display.set_mode((500,400))
pygame.display.update()
dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(event)
            pygame.quit()

    pygame.display.update()
quit()

