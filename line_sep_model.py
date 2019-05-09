from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras import datasets, layers, models, regularizers
import os
import numpy as np
import matplotlib.pyplot as plt

def get_Data():
    data = []
    labels = []
    for key in sorted(os.listdir("line_data/")):
        info = np.load("line_data/"+key)
        data += [info]
        cuts = np.load("line_labels/"+key)
        labels += [cuts]
    new_data = []
    new_labels = []
    for i in range(len(labels)):
        last = 0
        for cut in labels[i]:
            cut = int(cut)
            img = data[i][:, last:]
            partial_img = np.zeros([4, 2500])
            partial_img[:, :img.shape[1]] = img
            new_data += [partial_img.flatten()]
            new_labels += [cut-last]
            last = cut
    new_data = np.array(new_data)
    new_labels = np.array(new_labels)
    new_data = new_data[:, :, np.newaxis]
    return new_data, new_labels
                

data, labels = get_Data()
print(data.shape, labels.shape)
#x = np.arange(10000)
#plt.plot(x, data[5])
#print(labels[5])
#plt.show()

model = models.Sequential()
model.add(layers.MaxPooling1D(5, input_shape=(10000, 1)))
model.add(layers.Flatten())
model.add(layers.Dense(1000, activation='relu'))
model.add(layers.Dense(600, activation='relu'))
model.add(layers.Dense(1))

model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.Adam(lr=.0007, decay=.01),
              metrics=['mean_absolute_error'])

print(model.summary())

history = model.fit(data, labels, batch_size=400, epochs=40, validation_split=0.2, verbose=1)

model.save('sep_model.h5')

plt.plot(history.history['mean_absolute_error'][2:])
plt.plot(history.history['val_mean_absolute_error'][2:])
plt.show()


