import numpy as np
import pygame

def convert (line):
    x = np.zeros(784)
    i = -1
    n = 0
    for c in line:
        if i == -1:
            y = int(c)
            i += 1
        elif c == ",":
            x[i] = n
            n = 0
            i += 1
        else:
            n *= 10
            n += int(c)
    return x, y

def data (size):
    read = open("train.csv")
    x = np.zeros([size, 784])
    y = []
    i = 0
    for line in read:
        if i < size:
            x[i], yn = convert(line[:-1])
            y += [yn]
            i += 1    
    read.close()
    return x, y

def step (w, b, x, y, rate):
    size = x.shape[0]
    scores = np.dot(x, w) + b
    correct_vals = scores[np.arange(size), y]
    scores = (scores.transpose() - correct_vals + 1).transpose()
    scores[np.arange(size), y] = 0
    scores[scores < 0] = 0
    loss = np.sum(scores)/size
    scores[scores > 0] = 1
    correct_grads = np.sum(scores, axis = 1)
    scores[np.arange(size), y] = -correct_grads
    db = scores
    dw = (db[:, :, np.newaxis]*x[:, np.newaxis]).transpose()
    db = np.sum(db, axis = 0)/size
    dw = np.sum(dw, axis = 2)/size
    w -= dw*rate
    b -= db*rate
    return w, b, loss

def predict(w, b, x):
    return np.argmax(np.dot(x, w) + b)

def accuracy (w, b, x, y):
    size = x.shape[0]
    scores = np.dot(x, w) + b
    predicted = np.argmax(scores, axis = 1)
    accuracy = (np.sum(predicted == y)/size)
    return accuracy

def redraw (x, y, screen):
    pygame.display.set_caption(str(int(y)))
    for i in range(784):
        pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
    pygame.display.flip()

def test_examples (w, b, x, y):
    pygame.init()
    screen = pygame.display.set_mode((280, 280))

    r = np.random.randint(size-train_size)
    redraw(x_test[r], y_test[r], screen)

    done = False
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                r = np.random.randint(size-train_size)
                redraw(x_test[r], predict(w, b, x_test[r]), screen)
    pygame.quit()

def interactive (w, b):
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    x = np.zeros(784)

    done = False
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                x = np.zeros(784)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button <= 3:
                    c = [int(event.pos[0]/10), int(event.pos[1]/10)]
                    for xx in range(c[0]-1, c[0]+2):
                        for yy in range(c[1]-1, c[1]+2):
                            if 28*yy+xx < 784:
                                x[28*yy+xx] = 255
        redraw(x, predict(w, b, x), screen)
    pygame.quit()

def weight_display (w):
    w = w.transpose()
    w -= np.sum(w, axis = 0)/10
    pygame.init()
    screen = pygame.display.set_mode((280, 280))
    i = 0
    for j in range(10):
        w[j] = w[j]
        w[j] -= np.min(w[j])
        w[j] /= np.max(w[j])
        w[j] *= 255
    redraw(w[i], i, screen)
    done = False
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                i = (i+1)%10
                redraw(w[i], i, screen)
    pygame.quit()

size = 10000 #60000
train_size = 7500
x, y = data(size)
x_train = x[:train_size]
y_train = y[:train_size]
x_test = x[train_size:]
y_test = y[train_size:]
batch_size = 50
rate = .00001
epochs = 30

w = np.zeros([784, 10])
b = np.zeros([10])

for epoch in range(epochs):
    loss = 0
    for i in range(int(train_size/batch_size)):
        batch_x = x_train[i*batch_size:(i+1)*batch_size]
        batch_y = y_train[i*batch_size:(i+1)*batch_size]
        w, b, l = step(w, b, batch_x, batch_y, rate)
        loss += l
    loss /= int(train_size/batch_size)
    print(loss)
print(accuracy(w, b, x_train, y_train))
print(accuracy(w, b, x_test, y_test))


test_examples(w, b, x_test, y_test)
interactive(w, b)
weight_display(w)
















