import numpy as np
import pygame
import time

def convert(line):
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

def data(size):
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
    return x, np.array(y)

def step(w, b, x, y, rate, margin):
    size = x.shape[0]
    scores = x
    relu = [None]*(len(w)-1)
    
    for i in range(len(w)-1):
        scores = np.dot(scores, w[i]) + b[i]
        scores[scores < 0] = 0
        relu[i] = scores*1
    
    final = np.dot(scores, w[-1]) + b[-1]
    correct_vals = final[np.arange(size), y]
    final_grad = (final.transpose() - correct_vals + 1).transpose()
    final_grad[np.arange(size), y] = 0
    
    final_grad[final_grad < 0] = 0
    loss = np.sum(final_grad)/size
    
    final_grad[final_grad > 0] = 1
    correct_grads = np.sum(final_grad, axis = 1)
    final_grad[np.arange(size), y] = -correct_grads
    final_grad = final_grad

    dw = [None]*len(w)
    db = [None]*len(w)

    grad = final_grad.transpose()

    for i in range(len(w)-1, 0, -1):
        db[i] = grad
        dw[i] = db[i]*relu[i-1].transpose()[:, np.newaxis]
        relu_grad = np.dot(w[i], grad).transpose()
        relu[i-1][relu[i-1] > 0] = 1
        grad = (relu_grad*relu[i-1]).transpose()

    db[0] = grad
    dw[0] = grad*x.transpose()[:, np.newaxis]
        
    
    for i in range(len(w)):
        db[i] = np.sum(db[i], axis = -1)/size
        dw[i] = np.sum(dw[i], axis = -1)/size

    for i in range(len(w)): 
        w[i] -= dw[i]*rate
        b[i] -= db[i]*rate
    return w, b, loss

def predict(w, b, x):
    scores = x
    for i in range(len(w)-1):
        scores = np.dot(scores, w[i]) + b[i]
        scores[scores < 0] = 0
    return np.argmax(np.dot(scores, w[-1]) + b[-1])

def accuracy(w, b, x, y):
    size = x.shape[0]
    scores = x
    for i in range(len(w)-1):
        scores = np.dot(scores, w[i]) + b[i]
        scores[scores < 0] = 0
    predicted = np.argmax(np.dot(scores, w[-1]) + b[-1], axis = 1)
    return np.sum(predicted == y)/size

def redraw(x, y, screen):
    pygame.display.set_caption(str(int(y)))
    for i in range(784):
        pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
    pygame.display.flip()

def test_examples(w, b, x, y):
    pygame.init()
    screen = pygame.display.set_mode((280, 280))

    r = np.random.randint(size-train_size)
    redraw(x[r], predict(w, b, x[r]), screen)

    done = False
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                r = np.random.randint(size-train_size)
                redraw(x[r], predict(w, b, x[r]), screen)
    pygame.quit()

def interactive(w, b):
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
        c, d = pygame.mouse.get_pos()
        x[28*int(d/10)+int(c/10)] = 255
        redraw(x, predict(w, b, x), screen)
    pygame.quit()

def net(x, x_conv, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=False, timing=False):
    if display:
        print("hardwired convolution deep layer fully connected relu activation")
        print("data size:", size)
        print("training size:", train_size)
        print("batch size:", batch_size)
        print("learning rate:", rate)
        print("learning rate decay:", decay)
        print("decay normalization:", norm)
        print("hidden layers:", layers)
        print("epochs:", epochs)
        print("weight initialization:", w_init)
        print("loss margin:", margin)
    x_train = x_conv[:train_size]
    y_train = y[:train_size]
    x_test = x_conv[train_size:]
    y_test = y[train_size:]
    layers = [676] + layers + [10]
    w = []
    b = []
    for i in range(len(layers)-1):
        w += [np.random.randn(layers[i], layers[i+1]) * w_init]
        b += [np.zeros(layers[i+1])]

    last_time = time.time()
    
    for epoch in range(epochs):
        loss = 0
        for i in range(int(train_size/batch_size)):
            batch_x = x_train[i*batch_size:(i+1)*batch_size]
            batch_y = y_train[i*batch_size:(i+1)*batch_size]
            w, b, l = step(w, b, batch_x, batch_y, rate, margin)
            loss += l
            if display and i%50 == 0:
                pass#print("batch", i)
            for i in range(len(w)):
                w[i] *= norm
                b[i] *= norm
        rate *= decay
        loss /= int(train_size/batch_size)
        if display:
            print("epoch", epoch, "loss:", loss)
        if timing:
            print("epoch", epoch, "time:", time.time()-last_time)
            last_time = time.time()
        #print("training accuracy:", accuracy(w, b, x_train, y_train))
        #print("test accuracy:", accuracy(w, b, x_test, y_test))
    test_accuracy = accuracy(w, b, x_test, y_test)
    if display:
        print("training accuracy:", accuracy(w, b, x_train, y_train))
        print("test accuracy:", test_accuracy)

        while True:
            test_examples(w, b, x_test, y_test)
            interactive(w, b)
    return test_accuracy

def process(x):
    new = []
    for image in x:
        image = np.reshape(image, [28, 28])
        sub = (3, 3)
        view = tuple(np.subtract(image.shape, sub)+1)+sub
        strides = image.strides*2
        subs = np.lib.stride_tricks.as_strided(image, view, strides)
        conv = np.array([[2, 1, 0], [1, 0,-1], [0, -1, -2]])
        add = np.reshape(np.einsum("ij,ijkl->kl", conv, subs.transpose()), -1)
        add[add < 0] = 0
        new += [add]
    return np.array(new)
        

start_time = time.time()
size = 6000 #60000
train_size = 5000
x, y = data(size)
p = np.random.permutation(size)
x = x[p]
x_conv = process(x)
y = y[p]
#print("reading time:", time.time()-start_time)

batch_size = 15
rate = .002
decay = .97
norm = 1
layers = [1000, 1000, 1000]
epochs = 10
w_init = .01
margin = 0

print(net(x, x_conv, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True))
