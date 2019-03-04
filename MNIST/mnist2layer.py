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

def step (w1, b1, w2, b2, x, y, rate):
    size = x.shape[0]
    scores1 = np.dot(x, w1) + b1
    scores1[scores1 < 0] = 0
    scores2 = np.dot(scores1, w2) + b2
    correct_vals = scores2[np.arange(size), y]
    scores2 = (scores2.transpose() - correct_vals + 1).transpose()
    scores2[np.arange(size), y] = 0
    scores2[scores2 < 0] = 0
    loss = np.sum(scores2)/size
    scores2[scores2 > 0] = 1
    correct_grads = np.sum(scores2, axis = 1)
    scores2[np.arange(size), y] = -correct_grads
    db2 = scores2
    dw2 = (db2[:, :, np.newaxis]*scores1[:, np.newaxis])
    relu_grads = np.dot(db2[:, np.newaxis], w2.transpose()).transpose()
    scores1[scores1 > 0] = 1
    relu_grads= relu_grads*scores1.transpose()[:, np.newaxis]
    db1 = relu_grads
    dw1 = (db1*x.transpose()).transpose()
    db1 = np.sum(db1, axis = 2).squeeze()/size
    dw1 = np.sum(dw1, axis = 0)/size
    db2 = np.sum(db2, axis = 0)/size
    dw2 = np.sum(dw2, axis = 0).transpose()/size
    w1 -= dw1*rate
    b1 -= db1*rate
    w2 -= dw2*rate
    b2 -= db2*rate
    return w1, b1, w2, b2, loss

def step_finn (w1, b1, w2, b2, x, y, rate):
    size = x.shape[0]
    scores1 = np.dot(x, w1) + b1
    scores1[scores1 < 0] = 0
    scores1[scores1 > 0] = 1
    scores2 = np.dot(scores1, w2) + b2
    correct_vals = scores2[np.arange(size), y]
    scores2 = (scores2.transpose() - correct_vals + 1).transpose()
    scores2[np.arange(size), y] = 0
    scores2[scores2 < 0] = 0
    loss = np.sum(scores2)/size
    scores2[scores2 > 0] = 1
    correct_grads = np.sum(scores2, axis = 1)
    scores2[np.arange(size), y] = -correct_grads
    db2 = scores2
    dw2 = (db2[:, :, np.newaxis]*scores1[:, np.newaxis])
    db1 = np.dot(db2[:, np.newaxis], w2.transpose()).transpose()
    dw1 = (db1*x.transpose()).transpose()
    db1 = np.sum(db1, axis = 2).squeeze()/size
    dw1 = np.sum(dw1, axis = 0)/size
    db2 = np.sum(db2, axis = 0)/size
    dw2 = np.sum(dw2, axis = 0).transpose()/size
    w1 -= dw1*rate
    b1 -= db1*rate
    w2 -= dw2*rate
    b2 -= db2*rate
    return w1, b1, w2, b2, loss

def predict(w1, b1, w2, b2, x):
    scores = np.dot(x, w1) + b1
    scores[scores < 0] = 0
    #scores[scores > 0] = 1
    return np.argmax(np.dot(scores, w2) + b2)

def accuracy (w1, b1, w2, b2, x, y):
    size = x.shape[0]
    scores = np.dot(x, w1) + b1
    scores[scores < 0] = 0
    #scores[scores > 0] = 1
    scores = np.dot(scores, w2) + b2
    predicted = np.argmax(scores, axis = 1)
    accuracy = (np.sum(predicted == y)/size)
    return accuracy

def redraw (x, y, screen):
    pygame.display.set_caption(str(int(y)))
    for i in range(784):
        pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
    pygame.display.flip()

def test_examples (w1, b1, w2, b2, x, y):
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
                redraw(x_test[r], predict(w1, b1, w2, b2, x_test[r]), screen)
    pygame.quit()

def interactive (w1, b1, w2, b2):
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
        a, b = pygame.mouse.get_pos()
        x[28*int(b/10)+int(a/10)] = 255
        redraw(x, predict(w1, b1, w2, b2, x), screen)
    pygame.quit()

size = 2000 #60000
train_size = 1500
x, y = data(size)
x_train = x[:train_size]
y_train = y[:train_size]
x_test = x[train_size:]
y_test = y[train_size:]
batch_size = 100
rate = .002
decay = .92
norm = 1
layer = 1000
epochs = 18
print(size, train_size, batch_size, rate, decay, norm, layer, epochs)

w1 = np.random.randn(784, layer) *.01
b1 = np.zeros([layer])
w2 = np.random.randn(layer, 10) *.01
b2 = np.zeros([10])

for epoch in range(epochs):
    loss = 0
    for i in range(int(train_size/batch_size)):
        batch_x = x_train[i*batch_size:(i+1)*batch_size]
        batch_y = y_train[i*batch_size:(i+1)*batch_size]
        w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
        loss += l
    w1 *= norm
    b1 *= norm
    w2 *= norm
    b2 *= norm
    rate *= decay
    loss /= int(train_size/batch_size)
    print(loss)
print(accuracy(w1, b1, w2, b2, x_train, y_train))
print(accuracy(w1, b1, w2, b2, x_test, y_test))


while True:
    test_examples(w1, b1, w2, b2, x_test, y_test)
    interactive(w1, b1, w2, b2)



