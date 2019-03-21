import numpy as np
import cv2
import matplotlib.pyplot as plt
import pygame
pygame.init()

def label_image(name):
    file = "data/forms/" + name + ".png" 
    img = pygame.image.load(file)
    img = pygame.transform.scale(img, (600, 700))
    screen = pygame.display.set_mode((600, 700))
    pygame.display.set_caption("Line Labeler")
    lines = []
    done = False
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                lines += [pygame.mouse.get_pos()[1]]
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if len(lines) > 0:
                        lines.pop()
        screen.fill((255, 255, 255))
        screen.blit(img, [0, 0])
        for line in lines:
            pygame.draw.line(screen, (0, 0, 0), [0, line], [600, line], 1)
        pygame.display.flip()
    pygame.quit()
    file = open("line_labels/"+ name +".txt", "w")
    file.write("600")
    for line in lines:
        file.write("\n")
        file.write(str(line))
    file.close()


name =  "a01-000x"
label_image(name)
