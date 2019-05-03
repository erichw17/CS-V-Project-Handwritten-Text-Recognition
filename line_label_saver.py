import numpy as np
import cv2
import os
from IAM_Line_Sep import cutAndSeparate as sep

def processImg(key):
    file_name = "data/forms/" + key + ".png"
    img = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
    edges, halves, data = sep(img, data=True)
    data = data[:, edges[0]:edges[1]]
    for i in range(len(halves)):
        halves[i] -= edges[0]
    np.save("line_labels/"+key, halves)
    np.save("line_data/"+key, data)


print(len(os.listdir("data/forms/")))
i = 0 
for form in sorted(os.listdir("data/forms/")):
    print(form)
    print(i)
    processImg(form[:-4])
    i += 1
