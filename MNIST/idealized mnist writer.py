import numpy as np

def write(data):
    write = open("", "w")    
    for line in data:
        for n in line:
            write.write(str(int(n)))
            write.write(", ")
        write.write("\n")
    write.close()

base = np.zeros([1, 28, 28])
one = np.zeros([28, 28])
for i in range(7, 20)
