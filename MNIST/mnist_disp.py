import numpy as np
import pygame

def convert (line):
    x = np.zeros(784)
    i = -1
    n = 0
    for c in line:
        if i == -1:
            y = c
            i += 1
        elif c == ",":
            x[i] = n
            n = 0
            i += 1
        else:
            n *= 10
            n += int(c)
    return x, y

def redraw (x, y, n):
    pygame.display.set_caption(str(int(y[n])))
    for i in range(784):
        pygame.draw.rect(screen, (255-x[n][i], 255-x[n][i], 255-x[n][i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
    pygame.display.flip()

read = open("train.csv")
size = 100 #60000
x = np.zeros([size, 784])
y = np.zeros(size)
i = 0
for line in read:
    if i < size:
        x[i], y[i] = convert(line[:-1])
        i += 1
read.close()

pygame.init()
screen = pygame.display.set_mode((280, 280))

redraw(x, y, 0)

done = False
while not done:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            redraw(x, y, np.random.randint(size))
pygame.quit()

    

