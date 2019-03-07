Python 3.5.1 (default, Dec 27 2015, 02:23:23) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 1, in <module>
    read = open("trainimages")
FileNotFoundError: [Errno 2] No such file or directory: 'trainimages'
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 2, in <module>
    for line in read:
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0x8b in position 1: ordinal not in range(128)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 1, in <module>
    import cPickle, gzip, numpy
ImportError: No module named 'cPickle'
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 5, in <module>
    train_set, valid_set, test_set = cPickle.load(f)
NameError: name 'cPickle' is not defined
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 5, in <module>
    train_set, valid_set, test_set = pickle.load(f)
UnicodeDecodeError: 'ascii' codec can't decode byte 0x90 in position 614: ordinal not in range(128)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
!
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 3, in <module>
    print("!")
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,18,18,18,126,136,175,26,166,255,247,127,0,0,0,0,0,0,0,0,0,0,0,0,30,36,94,154,170,253,253,253,253,253,225,172,253,242,195,64,0,0,0,0,0,0,0,0,0,0,0,49,238,253,253,253,253,253,253,253,253,251,93,82,82,56,39,0,0,0,0,0,0,0,0,0,0,0,0,18,219,253,253,253,253,253,198,182,247,241,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,80,156,107,253,253,205,11,0,43,154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,1,154,253,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,139,253,190,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,190,253,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,35,241,225,160,108,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,81,240,253,253,119,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,186,253,253,150,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,93,252,253,187,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,249,253,249,64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,46,130,183,253,253,207,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,39,148,229,253,253,253,250,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,114,221,253,253,253,253,201,78,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,23,66,213,253,253,253,253,198,81,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,171,219,253,253,253,253,195,80,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,172,226,253,253,253,253,244,133,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,136,253,253,253,212,135,132,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,51,159,253,159,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48,238,252,252,252,237,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,54,227,253,252,239,233,252,57,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,60,224,252,253,252,202,84,252,253,122,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,163,252,252,252,253,252,252,96,189,253,167,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,51,238,253,253,190,114,253,228,47,79,255,168,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48,238,252,252,179,12,75,121,21,0,0,253,243,50,0,0,0,0,0,0,0,0,0,0,0,0,0,38,165,253,233,208,84,0,0,0,0,0,0,253,252,165,0,0,0,0,0,0,0,0,0,0,0,0,7,178,252,240,71,19,28,0,0,0,0,0,0,253,252,195,0,0,0,0,0,0,0,0,0,0,0,0,57,252,252,63,0,0,0,0,0,0,0,0,0,253,252,195,0,0,0,0,0,0,0,0,0,0,0,0,198,253,190,0,0,0,0,0,0,0,0,0,0,255,253,196,0,0,0,0,0,0,0,0,0,0,0,76,246,252,112,0,0,0,0,0,0,0,0,0,0,253,252,148,0,0,0,0,0,0,0,0,0,0,0,85,252,230,25,0,0,0,0,0,0,0,0,7,135,253,186,12,0,0,0,0,0,0,0,0,0,0,0,85,252,223,0,0,0,0,0,0,0,0,7,131,252,225,71,0,0,0,0,0,0,0,0,0,0,0,0,85,252,145,0,0,0,0,0,0,0,48,165,252,173,0,0,0,0,0,0,0,0,0,0,0,0,0,0,86,253,225,0,0,0,0,0,0,114,238,253,162,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,85,252,249,146,48,29,85,178,225,253,223,167,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,85,252,252,252,229,215,252,252,252,196,130,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,28,199,252,252,253,252,252,233,145,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,128,252,253,252,141,37,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,232,39,0,0,0,0,0,0,0,0,0,62,81,0,0,0,0,0,0,0,0,0,0,0,0,0,0,120,180,39,0,0,0,0,0,0,0,0,0,126,163,0,0,0,0,0,0,0,0,0,0,0,0,0,2,153,210,40,0,0,0,0,0,0,0,0,0,220,163,0,0,0,0,0,0,0,0,0,0,0,0,0,27,254,162,0,0,0,0,0,0,0,0,0,0,222,163,0,0,0,0,0,0,0,0,0,0,0,0,0,183,254,125,0,0,0,0,0,0,0,0,0,46,245,163,0,0,0,0,0,0,0,0,0,0,0,0,0,198,254,56,0,0,0,0,0,0,0,0,0,120,254,163,0,0,0,0,0,0,0,0,0,0,0,0,23,231,254,29,0,0,0,0,0,0,0,0,0,159,254,120,0,0,0,0,0,0,0,0,0,0,0,0,163,254,216,16,0,0,0,0,0,0,0,0,0,159,254,67,0,0,0,0,0,0,0,0,0,14,86,178,248,254,91,0,0,0,0,0,0,0,0,0,0,159,254,85,0,0,0,47,49,116,144,150,241,243,234,179,241,252,40,0,0,0,0,0,0,0,0,0,0,150,253,237,207,207,207,253,254,250,240,198,143,91,28,5,233,250,0,0,0,0,0,0,0,0,0,0,0,0,119,177,177,177,177,177,98,56,0,0,0,0,0,102,254,220,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,254,137,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,254,57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,254,57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,255,94,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,254,96,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,254,153,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,169,255,153,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,254,153,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,124,253,255,63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,244,251,253,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,127,251,251,253,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,68,236,251,211,31,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,60,228,251,251,94,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,155,253,253,189,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,253,251,235,66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,205,253,251,126,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,104,251,253,184,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,80,240,251,193,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,253,253,253,159,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,151,251,251,251,39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48,221,251,251,172,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,234,251,251,196,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,251,251,89,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,159,255,253,253,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48,228,253,247,140,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,251,253,220,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,251,253,220,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,193,253,220,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,148,210,253,253,113,87,148,55,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,87,232,252,253,189,210,252,252,253,168,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,57,242,252,190,65,5,12,182,252,253,116,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,252,252,183,14,0,0,92,252,252,225,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,132,253,252,146,14,0,0,0,215,252,252,79,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,126,253,247,176,9,0,0,8,78,245,253,129,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,232,252,176,0,0,0,36,201,252,252,169,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,22,252,252,30,22,119,197,241,253,252,251,77,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,231,252,253,252,252,252,226,227,252,231,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,235,253,217,138,42,24,192,252,143,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,62,255,253,109,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,71,253,252,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,252,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,71,253,252,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,106,253,252,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,255,253,21,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,218,252,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,252,189,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,184,252,170,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,147,252,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,25,100,122,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,33,151,208,252,252,252,146,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,152,244,252,253,224,211,252,232,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,152,239,252,252,252,216,31,37,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,252,252,252,252,217,29,0,37,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,181,252,252,220,167,30,0,0,77,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,128,58,22,0,0,0,0,100,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,157,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,110,121,122,121,202,252,194,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,53,179,253,253,255,253,253,228,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,54,227,252,243,228,170,242,252,252,231,117,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,78,252,252,125,59,0,18,208,252,252,252,252,87,7,0,0,0,0,0,0,0,0,0,0,0,0,5,135,252,252,180,16,0,21,203,253,247,129,173,252,252,184,66,49,49,0,0,0,0,0,0,0,0,3,136,252,241,106,17,0,53,200,252,216,65,0,14,72,163,241,252,252,223,0,0,0,0,0,0,0,0,105,252,242,88,18,73,170,244,252,126,29,0,0,0,0,0,89,180,180,37,0,0,0,0,0,0,0,0,231,252,245,205,216,252,252,252,124,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,207,252,252,252,252,178,116,36,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,93,143,121,23,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,145,255,211,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,237,253,252,71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,175,253,252,71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,144,253,252,71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,191,253,252,71,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,221,253,252,124,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,253,252,252,108,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,252,252,108,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,253,253,108,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,252,252,108,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,252,252,108,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,252,252,108,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,255,253,253,170,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,252,252,252,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,149,252,252,252,144,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,109,252,252,252,144,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,218,253,253,255,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,175,252,252,253,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,73,252,252,253,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,211,252,253,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,38,43,105,255,253,253,253,253,253,174,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,43,139,224,226,252,253,252,252,252,252,252,252,158,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,178,252,252,252,252,253,252,252,252,252,252,252,252,59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,109,252,252,230,132,133,132,132,189,252,252,252,252,59,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,29,29,24,0,0,0,0,14,226,252,252,172,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,85,243,252,252,144,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,88,189,252,252,252,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,91,212,247,252,252,252,204,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,125,193,193,193,253,252,252,252,238,102,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,222,252,252,252,252,253,252,252,252,177,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,223,253,253,253,253,255,253,253,253,253,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,123,52,44,44,44,44,143,252,252,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,252,252,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,86,252,252,74,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,75,9,0,0,0,0,0,0,98,242,252,252,74,0,0,0,0,0,0,0,0,0,0,0,0,0,61,183,252,29,0,0,0,0,18,92,239,252,252,243,65,0,0,0,0,0,0,0,0,0,0,0,0,0,208,252,252,147,134,134,134,134,203,253,252,252,188,83,0,0,0,0,0,0,0,0,0,0,0,0,0,0,208,252,252,252,252,252,252,252,252,253,230,153,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,49,157,252,252,252,252,252,217,207,146,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,103,235,252,172,103,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0

1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,63,197,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,254,230,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,254,254,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,254,255,48,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,254,254,57,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,254,254,108,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,239,254,143,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,178,254,143,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,178,254,143,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,178,254,162,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,178,254,240,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,113,254,240,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,83,254,245,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,79,254,246,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,214,254,150,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,144,241,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,144,240,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,144,254,82,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,230,247,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,168,209,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 3, in <module>
    print(line)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
60000
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
60000
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 22, in <module>
    x = np.zeros([60000, 784])
NameError: name 'np' is not defined
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 26, in <module>
    x[i], [i] = convert(line)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 17, in convert
    n += int(c)
ValueError: invalid literal for int() with base 10: '\n'
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 27, in <module>
    i += 1
TypeError: Can't convert 'int' object to str implicitly
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 26, in <module>
    x[i], y[i] = convert(line[:-1])
IndexError: index 784 is out of bounds for axis 0 with size 784
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[  0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   3.
  18.  18.  18. 126. 136. 175.  26. 166. 255. 247. 127.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.  30.  36.  94. 154. 170.
 253. 253. 253. 253. 253. 225. 172. 253. 242. 195.  64.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.  49. 238. 253. 253. 253. 253.
 253. 253. 253. 253. 251.  93.  82.  82.  56.  39.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.  18. 219. 253. 253. 253. 253.
 253. 198. 182. 247. 241.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.  80. 156. 107. 253. 253.
 205.  11.   0.  43. 154.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.  14.   1. 154. 253.
  90.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0. 139. 253.
 190.   2.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.  11. 190.
 253.  70.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.  35.
 241. 225. 160. 108.   1.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
  81. 240. 253. 253. 119.  25.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.  45. 186. 253. 253. 150.  27.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.  16.  93. 252. 253. 187.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0. 249. 253. 249.  64.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.  46. 130. 183. 253. 253. 207.   2.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.  39.
 148. 229. 253. 253. 253. 250. 182.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.  24. 114. 221.
 253. 253. 253. 253. 201.  78.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.  23.  66. 213. 253. 253.
 253. 253. 198.  81.   2.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.  18. 171. 219. 253. 253. 253. 253.
 195.  80.   9.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.  55. 172. 226. 253. 253. 253. 253. 244. 133.
  11.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0. 136. 253. 253. 253. 212. 135. 132.  16.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.
   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.   0.]
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 39, in <module>
    if event.type == pygame.QUIT:
NameError: name 'event' is not defined
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 39, in <module>
    for event in pygame.event.get():
pygame.error: video system not initialized
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============================== RESTART: Shell ===============================
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 36, in <module>
    pygame.draw.rect(screen, (256-x[0][i], 256-x[0][i], 256-x[0][i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
TypeError: invalid color argument
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist_disp.py", line 39, in <module>
    redraw(x, y, 0)
  File "/Users/Finn/Documents/MNIST/mnist_disp.py", line 22, in redraw
    pygame.display.set_caption(y[i])
UnboundLocalError: local variable 'i' referenced before assignment
>>> 
============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist_disp.py", line 39, in <module>
    redraw(x, y, 0)
  File "/Users/Finn/Documents/MNIST/mnist_disp.py", line 22, in redraw
    pygame.display.set_caption(y[n])
TypeError: must be str, not numpy.float64
>>> 
============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist_disp.py", line 50, in <module>
    redraw(x, y, random.randint(size))
NameError: name 'randint' is not defined
>>> 
============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
!
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
0
1
2
3
4
5
6
7
8
9
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 45, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
NameError: name 'step' is not defined
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 52, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 33, in step
    scores = np.dot(w)
TypeError: Required argument 'b' (pos 2) not found
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 52, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 33, in step
    scores = np.dot(w, x) + b
ValueError: operands could not be broadcast together with shapes (784,784) (10,) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
>>> 
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
(10, 10)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(10, 10)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(10, 10)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(15, 10)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 52, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 34, in step
    correct_vals = scores[y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 52, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 34, in step
    correct_vals = scores[:, y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 53, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 35, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 54, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 36, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 53, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 35, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 54, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 36, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
5
0
4
1
9
2
1
3
1
4
3
5
3
6
1
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 55, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 37, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 55, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 37, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
5.0
0.0
4.0
1.0
9.0
2.0
1.0
3.0
1.0
4.0
3.0
5.0
3.0
6.0
1.0
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 55, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 37, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
5
5.0
0
0.0
4
4.0
1
1.0
9
9.0
2
2.0
1
1.0
3
3.0
1
1.0
4
4.0
3
3.0
5
5.0
3
3.0
6
6.0
1
1.0
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 56, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 38, in step
    correct_vals = scores[np.arange(size), y]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[5. 0. 4. 1. 9. 2. 1. 3. 1. 4. 3. 5. 3. 6. 1.]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 54, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 36, in step
    correct_vals = scores[np.arange(size), int(y)]
TypeError: only size-1 arrays can be converted to Python scalars
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 53, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 35, in step
    correct_vals = scores[np.arange(size), np.int(y)]
TypeError: only size-1 arrays can be converted to Python scalars
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 53, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 35, in step
    correct_vals = scores[np.arange(size), y[:]]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 53, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 35, in step
    correct_vals = scores[np.arange(size), np.rint(y)]
IndexError: arrays used as indices must be of integer (or boolean) type
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 53, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 35, in step
    correct_vals = scores[np.arange(size), list(y)]
IndexError: only integers, slices (`:`), ellipsis (`...`), numpy.newaxis (`None`) and integer or boolean arrays are valid indices
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 54, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 34, in step
    size = y.shape[0]
AttributeError: 'list' object has no attribute 'shape'
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 55, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 37, in step
    scores -= correct_vals
ValueError: operands could not be broadcast together with shapes (15,10) (15,) (15,10) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 55, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 37, in step
    scores = scores - correct_vals
ValueError: operands could not be broadcast together with shapes (15,10) (15,) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[1. 1. 1. 1. 1. 0. 1. 1. 1. 1.]
 [0. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 0. 1. 1. 1. 1. 1.]
 [1. 0. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 0.]
 [1. 1. 0. 1. 1. 1. 1. 1. 1. 1.]
 [1. 0. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 0. 1. 1. 1. 1. 1. 1.]
 [1. 0. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 0. 1. 1. 1. 1. 1.]
 [1. 1. 1. 0. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 0. 1. 1. 1. 1.]
 [1. 1. 1. 0. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 0. 1. 1. 1.]
 [1. 0. 1. 1. 1. 1. 1. 1. 1. 1.]]
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 60, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 42, in step
    dw = db*x
ValueError: operands could not be broadcast together with shapes (15,10) (15,784) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 60, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 42, in step
    dw = db.transpose()*x
ValueError: operands could not be broadcast together with shapes (10,15) (15,784) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(15, 10)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 61, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 43, in step
    dw = db.transpose()*x
ValueError: operands could not be broadcast together with shapes (10,15) (15,784) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(15, 10)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 61, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 43, in step
    dw = db*x
ValueError: operands could not be broadcast together with shapes (15,10) (15,784) 
>>> np.array()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    np.array()
TypeError: Required argument 'object' (pos 1) not found
>>> 
>>> np.zeros([15, 10]) * np.zeros([15, 784])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    np.zeros([15, 10]) * np.zeros([15, 784])
ValueError: operands could not be broadcast together with shapes (15,10) (15,784) 
>>> np.zeros([15, 10]) * np.zeros([15, 1, 784])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    np.zeros([15, 10]) * np.zeros([15, 1, 784])
ValueError: operands could not be broadcast together with shapes (15,10) (15,1,784) 
>>> np.zeros([15, 10, 1]) * np.zeros([15, 1, 784])
array([[[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       ...,

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]]])
>>> (np.zeros([15, 10, 1]) * np.zeros([15, 1, 784])).shape
(15, 10, 784)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 60, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 42, in step
    dw = db[:, :, np.newaxis]*x
ValueError: operands could not be broadcast together with shapes (15,10,1) (15,784) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(10,)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(10, 784)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 63, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 45, in step
    w -= dw*rate
ValueError: operands could not be broadcast together with shapes (784,10) (10,784) (784,10) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 63, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 45, in step
    w -= dw*rate
ValueError: operands could not be broadcast together with shapes (784,10) (10,15) (784,10) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(784, 10, 15)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 64, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 46, in step
    w -= dw*rate
ValueError: operands could not be broadcast together with shapes (784,10) (10,15) (784,10) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 63, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 45, in step
    w -= dw*rate
ValueError: operands could not be broadcast together with shapes (784,10) (784,15) (784,10) 
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
38085.70155555556
2133105080.6460598
56293752151387.016
2.9220010030621133e+18
1.1741708126821746e+23
4.1307792777536815e+27
5.610795753959196e+31
4.2758433561255594e+36
1.1764263794753058e+41
6.701370578433855e+45
2.8801622374434876e+50
1.8887014444951944e+55
8.097320946965456e+59
5.561324271389226e+64
2.9423499084166346e+69
2.1324000506795683e+74
1.0532809279272155e+79
8.631185071542346e+83
4.141206707174948e+88
1.6298334066216644e+93
6.195943940547639e+97
4.049160257184607e+102
2.0325984436725514e+107
1.3327945974711653e+112
7.428520684290321e+116
4.429564659941531e+121
1.1203538127412603e+126
3.88967465436233e+130
2.202567395098074e+135
1.234367045311675e+140
5.563333006834822e+144
3.4161558483287447e+149
1.2904739985361072e+154
5.147117118734648e+158
3.301996953037013e+163
3.137433144611871e+168
1.4832371705104802e+173
7.390351444099335e+177
4.2816783613706e+182
2.0357895347676303e+187
9.793649279478436e+191
3.974042455509909e+196
2.126391946417649e+201
1.020532448593419e+206
5.1069940251333404e+210
4.113590966289643e+215
2.0029884394403059e+220
7.685252550912258e+224
5.826647791433214e+229
3.396274949591089e+234
2.503782137159114e+239
8.702026495208813e+243
4.245661466066051e+248
1.6573592560299692e+253
9.741049057594889e+257
8.074629857559211e+262
5.529949021501593e+267
3.384052250281316e+272
1.5607365900690277e+277
7.843830381625111e+281
5.402145228763747e+286
1.805557066023734e+291
1.6105462727476347e+296
6.356524016796062e+300

Warning (from warnings module):
  File "/usr/local/lib/python3.5/site-packages/numpy/core/_methods.py", line 32
    return umr_sum(a, axis, dtype, out, keepdims)
RuntimeWarning: overflow encountered in reduce
4.018625920734935e+305

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 39
    scores[scores < 0] = 0
RuntimeWarning: invalid value encountered in less

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 42
    dw = (db[:, :, np.newaxis]*x[:, np.newaxis]).transpose()
RuntimeWarning: overflow encountered in multiply
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
>>> 
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
765.4380311111116
854091.9130023348
449804603.0689133
466054231171.429
374465889009154.1
2.6283177084285274e+17
7.133777441132443e+19
1.0848601878567402e+23
5.964910279463297e+25
6.789524232800488e+28
5.843611965462918e+31
7.649090783193048e+34
6.543228577129929e+37
8.995364566248207e+40
9.49563537937338e+43
1.3764782002909737e+47
1.3572173754630375e+50
2.2274564706461438e+53
2.1267101027487926e+56
1.6739960907793382e+59
1.2682037313972599e+62
1.6597737905763066e+65
1.6602101092477267e+68
2.1772714134649897e+71
2.4270369335348084e+74
2.901155090954747e+77
1.4633539121712772e+80
1.015088239888377e+83
1.1444257868421646e+86
1.2855416835424362e+89
1.154639300017077e+92
1.4201599051550176e+95
1.0665108385897294e+98
8.518366406416248e+100
1.0865385409949615e+104
2.0700002876610015e+107
1.9530394846647274e+110
1.9454646893192294e+113
2.2424868319647856e+116
2.1390731632214053e+119
2.0497087251568064e+122
1.6636551376594992e+125
1.7724574294772696e+128
1.7023763584777243e+131
1.6969501753481928e+134
2.741078083270662e+137
2.665968374882078e+140
2.048119236756914e+143
3.089873102891443e+146
3.6051180116955335e+149
5.290515869833693e+152
3.6729640311337367e+155
3.5673812113524703e+158
2.782975110243883e+161
3.2618223272545066e+164
5.419949669181293e+167
7.39896306282254e+170
9.078782123075885e+173
8.348937060790805e+176
8.402092102430774e+179
1.1527805710880793e+183
7.678725779046976e+185
1.3626068764962797e+189
1.0764332773897503e+192
1.3571178038286938e+195
9.917529842222324e+197
1.2695017578154958e+201
9.874456760297002e+203
1.488353381203203e+207
1.2333511822209557e+210
1.2814584880110758e+213
8.123546423511632e+215
8.12256120837401e+218
7.745605149326144e+221
9.836179204602413e+224
1.018852660545381e+228
7.131155696411701e+230
6.414262752572501e+233
1.0910048810543083e+237
1.7458164336026118e+240
4.83752146839073e+243
9.005450051182955e+246
1.461577432503201e+250
3.4658379277244796e+253
5.6706347126505736e+256
1.1024581636245409e+260
2.5451748265235197e+263
3.215707106457108e+266
8.704454516513655e+269
1.309595423846769e+273
3.804358176548305e+276
4.697096367967686e+279
7.478780761676231e+282
5.065648860140063e+285
4.1407440363696433e+288
3.985986845392291e+291
4.014599213995353e+294
4.2059442433806836e+297
5.010125848942479e+300
>>> 
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[0.93333333 0.73333333 0.93333333 0.8        0.86666667 0.86666667
 0.93333333 1.         1.         0.93333333]
9.0
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[3.19022178e+01 1.59747796e+02 4.10292044e+01 3.33882404e+02
 5.90964267e+01 6.80746267e+01 3.32906578e+01 6.66666667e-02
 1.33333333e-01 3.82146978e+01]
765.4380311111116
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[ 92849.03549086  44715.0129746   87715.70395061      0.
  80036.21461397  73375.76470013  92897.45376681 146931.56063629
 146874.11167629  88697.05519277]
854091.9130023348
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[2.79479984e+07 8.71667346e+07 3.16680182e+07 1.57521544e+08
 3.92355612e+07 4.75950752e+07 2.79226473e+07 0.00000000e+00
 9.08783909e+03 3.07379365e+07]
449804603.0689133
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[4.60149814e+10 1.22072003e+10 4.21255432e+10 0.00000000e+00
 3.49535258e+10 3.03654768e+10 4.60584045e+10 1.05669184e+11
 1.05652282e+11 4.30076326e+10]
466054231171.429
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[2.51046709e+13 7.65392968e+13 2.88822559e+13 1.04748483e+14
 3.95472503e+13 4.67103160e+13 2.50785860e+13 0.00000000e+00
 4.23741084e+09 2.78507927e+13]
374465889009154.1
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[2.90554696e+16 4.20416836e+15 2.67251857e+16 0.00000000e+00
 1.99431161e+16 1.62190134e+16 2.90759154e+16 5.51284447e+16
 5.51231389e+16 2.73573188e+16]
2.6283177084285274e+17
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[3.41692056e+15 2.20347943e+19 1.24126872e+18 2.86383576e+19
 7.49550913e+18 1.11245022e+19 0.00000000e+00 0.00000000e+00
 0.00000000e+00 7.99925574e+17]
7.133777441132443e+19
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[1.59253855e+22 1.02622222e+21 1.42669812e+22 0.00000000e+00
 8.46051691e+21 6.27456729e+21 1.59318563e+22 1.58885544e+22
 1.58885627e+22 1.48233722e+22]
1.0848601878567402e+23
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[1.20071974e+21 1.82122624e+25 1.70800201e+24 1.97845028e+25
 8.06369034e+24 1.07399270e+25 0.00000000e+00 8.26950533e+21
 8.26412985e+21 1.12298400e+24]
5.964910279463297e+25
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[1.09728831e+28 3.00950340e+26 8.52451178e+27 0.00000000e+00
 3.40834176e+27 2.57707506e+27 1.09755439e+28 1.09578460e+28
 1.09578556e+28 9.22023473e+27]
6.789524232800488e+28
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[5.29179768e+26 1.62214130e+31 2.05146905e+30 1.70364397e+31
 1.02571451e+31 1.17027151e+31 0.00000000e+00 6.94058370e+27
 6.93636931e+27 1.15253152e+30]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 65, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 46, in step
    print(db)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[0.93333333 0.73333333 0.93333333 0.8        0.86666667 0.86666667
 0.93333333 1.         1.         0.93333333]
9.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
(10,)
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[0.93333333 0.73333333 0.93333333 0.8        0.86666667 0.86666667
 0.93333333 1.         1.         0.93333333]
9.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 67, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 42, in step
    scores[np.arange(size), y] = correct_grads
ValueError: shape mismatch: value array of shape (10,) could not be broadcast to indexing result of shape (15,)
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[1.53333333 3.13333333 1.53333333 2.6        2.06666667 2.06666667
 1.53333333 1.         1.         1.53333333]
9.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[ 0.33333333 -1.66666667  0.33333333 -1.         -0.33333333 -0.33333333
  0.33333333  1.          1.          0.33333333]
9.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[ 1.  1.  1.  1.  1. -9.  1.  1.  1.  1.]
9.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]
[ 0.33333333 -1.66666667  0.33333333 -1.         -0.33333333 -0.33333333
  0.33333333  1.          1.          0.33333333]
9.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
7620.180311111112
18381864.3205775
35180542788.5923
112013586256181.03
2.9668853474433446e+17
7.279592617937079e+20
1.6169236074886562e+24
4.7102012304527824e+27
1.0475409795132333e+31
2.8513434645985796e+34
6.160421586794128e+37
8.710211323765515e+40
2.0612998980478095e+44
5.86725079127821e+47
1.568658308002973e+51
2.4926450285056703e+54
4.81898154349178e+57
9.747269646004469e+60
2.9503737875287065e+64
7.217307279396452e+67
2.084823735595946e+71
4.658289388432255e+74
8.832256247803254e+77
1.78586524474103e+81
1.3066358204371997e+84
2.972434911391154e+87
8.811187084771479e+90
1.452674972904552e+94
2.9246889917545514e+97
7.439374192113256e+100
1.955404774286134e+104
2.5803165943310163e+107
4.9693134674538e+110
9.735623315838507e+113
2.7078286972706475e+117
8.757535059359047e+120
2.2879619404327654e+124
6.544944746061186e+127
1.6327729883917862e+131
4.5625738657786536e+134
1.350755261226625e+138
5.429910718374776e+141
1.383987093337857e+145
9.786215449834281e+148
2.589546446452582e+152
5.47706121215117e+155
1.2156164279168423e+159
3.8015280149279114e+162
8.181283086555803e+165
1.4574205535981368e+169
1.972807013243959e+172
7.13479642479135e+175
1.9663167874700427e+179
7.805179495547216e+182
2.6384459582146053e+186
2.9307205358528976e+189
3.4473459527534457e+192
1.550647276312123e+196
3.7499616913001795e+199
9.966357427352283e+202
3.541597094544484e+206
6.876533093232074e+209
1.4966166029871063e+213
4.3902109626038274e+216
1.1287788793951298e+220
2.946236773995384e+223
8.210497230834077e+226
1.496104861236884e+230
3.6729413943900335e+233
6.086848025613773e+236
1.1265089075548801e+240
2.3437111705133983e+243
5.150399571274718e+246
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    print(loss)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
80.01684666666667
1791.9564519905146
32573.893228669884
999646.8575706332
26030502.68034391
603477753.3409734
13280150739.911642
364487979181.97363
7768925610268.894
196511466534590.9
3974007313824050.0
5.4202330358558856e+16
1.2230460763134546e+18
3.218882196197014e+19
8.398628280160344e+20
1.3310764320158128e+22
2.416462189976804e+23
4.860619592639066e+24
1.50398090561271e+26
3.605678591717e+27
9.421569577393208e+28
2.03660348687932e+30
3.7122632446017503e+31
6.906713201190738e+32
5.148563803268295e+33
1.0026128256789766e+35
2.885479335277475e+36
4.62700874307647e+37
9.100520507415529e+38
2.1578768320744263e+40
5.462305747494584e+41
7.111165905845032e+42
1.2059222212218502e+44
2.0229893785180763e+45
5.60668987362466e+46
1.7675106815140015e+48
4.449737742886693e+49
1.1789241043529683e+51
2.8526016848407555e+52Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    print(loss)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
148.7848768888889
4683.105782295456
156567.4972646036
7973499.076245099
605608746.177166
25188380189.373898
3257871366261.558
126986610440154.05
112145555070309.53
7917697317517988.0
2.1006789283106275e+17
8.212134120795448e+18
5.8195700153721514e+20
1.8206513384562564e+22
9.573321537868664e+23
5.2418491719801204e+25
1.235060309038982e+27
8.046745274610434e+28
4.279720479120373e+30
1.8469057264183836e+31
1.9051422774642345e+33
1.5781041379925825e+34
3.8987408488486334e+35
6.783229698802048e+36
1.3366267304655605e+37
1.3059585873448163e+39
3.0159496459001295e+40
6.821804228672407e+41
1.2389167130402177e+43
6.0629533472897586e+44Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    print(loss)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
358.6023000000002
3964.459577336001
20599.076420765025
320858.9882786339
9695742.500004116
217751709.54504305
4918041426.021178
602600194656.0781
6060529119064.32
122448320477403.66
1300407532649798.8
6.573025494998953e+16
1.5669464186490276e+18
2.179160443002408e+19
2.0811416493817636e+20
4.563020909691607e+21
1.0848415811104603e+23
1.4548180779272926e+24
1.4258118041853875e+25
2.4715655357220465e+26
6.355256783161101e+27
1.3173084403744593e+29
2.0532740724536176e+30
0.0
5.844682816281092e+31
1.0576149663918168e+33
2.413854192452552e+34
1.616378614579102e+36
3.3611601604075963e+37
7.45080768558889e+38
1.6860688990877238e+40
1.7780560798207088e+41Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    print(loss)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
9.0
[-1.e-05 -1.e-05 -1.e-05 -1.e-05 -1.e-05  9.e-05 -1.e-05 -1.e-05 -1.e-05
 -1.e-05]
358.6023000000002
[ 3.576023e-03 -2.000000e-05 -2.000000e-05 -2.000000e-05 -2.000000e-05
 -3.416023e-03 -2.000000e-05 -2.000000e-05 -2.000000e-05 -2.000000e-05]
3964.459577336001
[-3.59985728e-02 -3.00000000e-05 -3.00000000e-05 -3.00000000e-05
  3.96245958e-02 -3.41602300e-03 -3.00000000e-05 -3.00000000e-05
 -3.00000000e-05 -3.00000000e-05]
20599.076420765025
[-3.59985728e-02  2.05960764e-01 -4.00000000e-05 -4.00000000e-05
 -1.66306168e-01 -3.41602300e-03 -4.00000000e-05 -4.00000000e-05
 -4.00000000e-05 -4.00000000e-05]
320858.9882786339
[-3.59985728e-02 -3.00257912e+00 -5.00000000e-05 -5.00000000e-05
 -1.66306168e-01 -3.41602300e-03 -5.00000000e-05 -5.00000000e-05
 -5.00000000e-05  3.20854988e+00]
9695742.500004116
[-3.59985728e-02 -3.00257912e+00  9.69573750e+01 -6.00000000e-05
 -1.66306168e-01 -3.41602300e-03 -6.00000000e-05 -6.00000000e-05
 -6.00000000e-05 -9.37488351e+01]
217751709.54504305
[  -64.75911072  2174.51451633 -1628.56675439   -64.90220419
   -62.9686652    -64.86233415   -64.90220419   -64.90220419
   -64.90220419   -93.74883512]
4918041426.021178
[   -67.86820342 -46960.06692845  -1628.56675439  49115.51205602
   -104.87738437    -65.67730771    -64.90221419    -64.90221419
    -64.90221419    -93.74883512]Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 63, in <module>
    print(b)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
1.0
9.0
350.6023000000002
358.6023000000002
3957.459577336001
3964.459577336001
20593.076420765025
20599.076420765025
320853.9882786339
320858.9882786339
9695738.500004116
9695742.500004116
172552412.93884686
217751709.54504305
4913458144.477968
4918041426.021178
125835441175.66016
602600194656.0781
6025499959951.76
6060529119064.32
116258043062349.44
122448320477403.66
1294637819498361.2
1300407532649798.8
1.8641892893604772e+16Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 46, in step
    print(np.max(db))
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
1.0
9.0
350.6023000000002
358.6023000000002
3957.459577336001
3964.459577336001
20593.076420765025
20599.076420765025
320853.9882786339
320858.9882786339
9695738.500004116
9695742.500004116
172552412.93884686
217751709.54504305
4913458144.477968
4918041426.021178
125835441175.66016
602600194656.0781
6025499959951.76
6060529119064.32
116258043062349.44
122448320477403.66
1294637819498361.2
1300407532649798.8
1.8641892893604772e+16
6.573025494998953e+16
1.4651198316383923e+18
1.5669464186490276e+18
2.1758305070692913e+19
2.179160443002408e+19
2.0806337640227583e+20
2.0811416493817636e+20
4.5589537563629715e+21
4.563020909691607e+21
1.0845631877527753e+23
1.0848415811104603e+23
1.454507220015294e+24
1.4548180779272926e+24
1.4257320742896486e+25
1.4258118041853875e+25
2.4715417349727555e+26
2.4715655357220465e+26
6.355088636683202e+27
6.355256783161101e+27
1.0090288976920012e+29
1.3173084403744593e+29
2.0482058367129262e+30
2.0532740724536176e+30
0.0
0.0
5.844450106270505e+31
5.844682816281092e+31
1.0575390697259989e+33
1.0576149663918168e+33
2.4138245463744473e+34
2.413854192452552e+34
1.5148112889286504e+36
1.616378614579102e+36
3.3557174131375146e+37
3.3611601604075963e+37
4.239995301415602e+38
7.45080768558889e+38
1.6539918366898089e+40
1.6860688990877238e+40
1.778043668766909e+41
1.7780560798207088e+41
1.989387162118113e+42
1.989387162118113e+42
6.371667843318116e+43Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 43, in step
    print(np.max(scores))
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
1.0
9.0
350.6023000000002
358.6023000000002
3957.459577336001
3964.459577336001
20593.076420765025
20599.076420765025
320853.9882786339
320858.9882786339
9695738.500004116
9695742.500004116
172552412.93884686
217751709.54504305
4913458144.477968
4918041426.021178
125835441175.66016
602600194656.0781
6025499959951.76
6060529119064.32
116258043062349.44
122448320477403.66
1294637819498361.2
1300407532649798.8
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 67, in <module>
    print(loss)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
1.0
350.6023000000002
3957.459577336001
20593.076420765025
320853.9882786339
9695738.500004116
172552412.93884686
4913458144.477968
125835441175.66016
6025499959951.76
116258043062349.44
1294637819498361.2
1.8641892893604772e+16
1.4651198316383923e+18
2.1758305070692913e+19
2.0806337640227583e+20
4.5589537563629715e+21
1.0845631877527753e+23
1.454507220015294e+24
1.4257320742896486e+25
2.4715417349727555e+26
6.355088636683202e+27
1.0090288976920012e+29
2.0482058367129262e+30
0.0
5.844450106270505e+31
1.0575390697259989e+33
2.4138245463744473e+34
1.5148112889286504e+36
3.3557174131375146e+37
4.239995301415602e+38
1.6539918366898089e+40
1.778043668766909e+41
1.989387162118113e+42
6.371667843318116e+43
1.3855739691060893e+45
2.4291880194267114e+46
1.0863114253232478e+48
2.927486675458953e+49
7.365857282049971e+50
1.7361716884586875e+52
3.4606032965522417e+53
6.0680766235314376e+54
1.0267214847301957e+56
1.236918230450848e+57
3.698043488923473e+58
4.677495251088009e+60
8.493456161825204e+61
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 40, in step
    print(np.max(scores))
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
0.0
314.64207000000016
3934.9393373360012
20556.357940765025
320782.84845863393
9695615.850134116
166062109.94526556
4770981699.990341
65575421709.95234
5466515575292.829
114179441024697.28
1284132929240912.0
1.2068867398605822e+16
1.3315160322739858e+18
2.165005154854374e+19
2.078752708305923e+20
4.55766436450143e+21
1.0843057386777432e+23
1.4543994546155548e+24
1.4256347664431845e+25
2.4715036544041022e+26
6.355025973706033e+27
9.644783800789328e+28Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in <module>
    w, b, loss = step(w, b, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 36, in step
    print(np.max(scores))
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
358.6023000000002
224.20239999999998
366.1848
710.3982
1225.4987
267.3571999999999
2070.6268999999998
0.0
189.68726
0.0
539.2329299999999
0.0
1773.6319000000003
1.3297599999999505
1983.7305000000001
80.26800999999992
2699.7099
0.0
329.78026
0.0
0.0
0.0
0.0
344.02896999999984
327.25168
471.7668900000001
56.925160000000034
0.0
158.46140000000014
190.3242800000001
175.1783399999999
0.0
141.7954400000001
71.53966000000003
270.22212000000013
62.23877999999998
0.0
221.52352999999988
17.309260000000023
0.0
57.094779999999986
0.0
0.0
0.0
0.0
76.52416999999997
0.2610600000000147
259.90984
0.0
7.207580000000021
0.0
0.0
390.86122999999986
0.0
43.50769000000008
0.0
0.0
0.0
15.194629999999933
35.425439999999966
0.0
65.27922999999979
0.0
60.80411000000002
0.0
0.0
0.0
13.458690000000026
0.0
201.95067999999998
0.0
0.0
0.0
0.0
0.0
390.45248000000004
0.0
0.0
0.0
156.97317000000004
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 67, in <module>
    print(loss)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
358.6023000000002
224.20239999999998
366.1848
710.3982
1225.4987
267.3571999999999
2070.6268999999998
0.0
189.68726
0.0
539.2329299999999
0.0
1773.6319000000003
1.3297599999999505
1983.7305000000001
80.26800999999992
2699.7099
0.0
329.78026
0.0
0.0
0.0
0.0
344.02896999999984
327.25168
471.7668900000001
56.925160000000034
0.0
158.46140000000014
190.3242800000001
175.1783399999999
0.0
141.7954400000001
71.53966000000003
270.22212000000013
62.23877999999998
0.0
221.52352999999988
17.309260000000023
0.0
57.094779999999986
0.0
0.0
0.0
0.0
76.52416999999997
0.2610600000000147
259.90984
0.0
7.207580000000021
0.0
0.0
390.86122999999986
0.0
43.50769000000008
0.0
0.0
0.0
15.194629999999933
35.425439999999966
0.0
65.27922999999979
0.0
60.80411000000002
0.0
0.0
0.0
13.458690000000026
0.0
201.95067999999998
0.0
0.0
0.0
0.0
0.0
390.45248000000004
0.0
0.0
0.0
156.97317000000004
0.0
0.0
0.0
29.528709999999947
0.0
144.55836000000005
32.359960000000086
0.0
0.0
0.0
0.0
0.0
0.0
15.175999999999888
0.0
50.70003000000004
0.0
0.0
0.0
243.27627000000015
0.0
0.0
0.0
0.0
0.0
33.746759999999966
0.0
44.16773999999998
313.60884999999985
69.98626999999986
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
14.531540000000177
47.82255999999997
0.0
0.0
128.90366999999998
21.397989999999965
0.0
0.0
0.0
0.0
0.0
276.3709900000001
30.552070000000015
611.34766
256.91234
0.0
2.663239999999945
75.21880999999982
58.26637000000011
51.489509999999974
0.0
0.0
7.033840000000069
311.18344
0.0
0.0
0.0
42.60200000000005
0.0
46.88155999999998
0.0
6.490450000000024
0.0
167.92235
0.0
0.0
6.892669999999953
93.29793
0.0
86.08366000000005
263.43366000000015
0.0
0.0
0.0
0.0
0.0
75.00387000000005
179.0817199999998
6.323190000000068
0.0
0.0
37.05327
0.0
0.0
0.0
0.0
75.35233
254.54770000000008
0.0
315.80877999999996
10.823750000000047
93.31876000000001
0.0
0.0
0.0
64.09397999999999
0.0
22.581410000000062
0.0
0.0
52.34872
0.0
0.0
20.728580000000036
14.468449999999976
24.492650000000026
0.0
245.69530000000012
0.0
0.0
114.14040000000008
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
50.273010000000006
0.0
0.0
0.0
121.41455
0.0
0.0
0.0
21.025910000000067
0.0
0.0
0.0
1206.3639200000002
184.8983599999999
178.06810000000002
0.0
108.86822000000006
0.0
0.0
0.0
15.919759999999982
0.0
0.0
20.973659999999967
0.0
16.881469999999894
0.0
0.0
19.434129999999968
159.32391999999996
0.0
0.0
874.8319999999998
103.85323000000014
46.99505999999998
151.97760000000005
39.1554000000001
0.0
96.62680999999998
0.0
116.86604000000005
0.0
144.9428999999999
0.0
595.9279599999996
0.0
0.0
0.0
0.0
0.0
346.88972
0.0
614.6999000000001
0.0
0.0
0.0
70.68274999999986
75.98017000000002
5.747369999999961
90.2969
58.90125000000003
0.0
151.95217999999988
0.0
0.0
0.0
200.06770000000006
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
28.23022000000003
0.0
0.0
0.0
0.0
13.881680000000244
0.0
0.0
0.0
0.0
0.0
0.0
26.426880000000025
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
26.31623000000009
0.11133000000002369
0.0
0.0
53.33166999999999
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
26.58447000000008
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
11.97959000000003
0.0
0.0
0.0
645.2188200000002
0.0
0.0
0.0
0.0
0.0
267.7205899999999
12.720020000000034
7.053439999999966
0.0
0.0
75.11782
58.84646000000028
0.0
191.7070799999999
5.1929499999998825
25.218849999999975
0.0
0.0
0.0
0.0
72.71118999999968
47.79872
0.0
5.2873500000000035
0.0
0.0
0.0
0.0
0.0
138.54569
0.0
0.0
0.0
0.0
0.0
35.76124999999997
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 67, in <module>
    print(loss)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
47.43723665333333
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
47.43723665333333
12.137066966666666
5.454624446666666
3.98464516
2.5957383
2.029366440000001
1.2895470266666686
1.1325093733333331
1.0691785333333335
0.6720650066666667
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
47.43723665333333
12.137066966666666
5.454624446666666
3.98464516
2.5957383
2.029366440000001
1.2895470266666686
1.1325093733333331
1.0691785333333335
0.6720650066666667
0.6707059933333336
0.4290706733333331
0.45525738000000027
0.31850719999999927
0.1913384799999999
0.23244561333333325
0.1431034400000004
0.14813151333333285
0.06149484666666676
0.13981260666666648
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
47.43723665333333
12.137066966666666
5.454624446666666
3.98464516
2.5957383
2.029366440000001
1.2895470266666686
1.1325093733333331
1.0691785333333335
0.6720650066666667
0.6707059933333336
0.4290706733333331
0.45525738000000027
0.31850719999999927
0.1913384799999999
0.23244561333333325
0.1431034400000004
0.14813151333333285
0.06149484666666676
0.13981260666666648
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
47.43723665333333
12.137066966666666
5.454624446666666
3.98464516
2.5957383
2.029366440000001
1.2895470266666686
1.1325093733333331
1.0691785333333335
0.6720650066666667
0.6707059933333336
0.4290706733333331
0.45525738000000027
0.31850719999999927
0.1913384799999999
0.23244561333333325
0.1431034400000004
0.14813151333333285
0.06149484666666676
0.13981260666666648
0.10996067333333329
0.01348999333333334
0.11561758666666712
0.08805292000000015
0.05144978000000011
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
47.43723665333333
12.137066966666666
5.454624446666666
3.98464516
2.5957383
2.029366440000001
1.2895470266666686
1.1325093733333331
1.0691785333333335
0.6720650066666667
0.6707059933333336
0.4290706733333331
0.45525738000000027
0.31850719999999927
0.1913384799999999
0.23244561333333325
0.1431034400000004
0.14813151333333285
0.06149484666666676
0.13981260666666648
0.10996067333333329
0.01348999333333334
0.11561758666666712
0.08805292000000015
0.05144978000000011
0.07544488666666661
0.016923766666666683
0.0
0.0
0.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
5.645285270000002
1.6904074313333333
0.9263810653333338
0.4370320833333335
0.39797797866666657
0.28862722000000013
0.22629074533333343
0.19569219933333326
0.13270113066666658
0.10723372733333328
0.09972628000000001
0.07264362066666667
0.044518431333333365
0.03183376866666667
0.030489589999999966
0.03463700266666667
0.017182866000000015
0.015359891333333285
0.01579362200000003
0.01423164266666666
0.020586996000000003
0.014314861999999992
0.008973348666666674
0.005992385333333337
0.0071721146666666735
0.007146657333333349
0.007897418000000015
0.0057847140000000016
0.0025959093333333457
0.0012809826666666713
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
4.939348263866666
1.6572227170000002
0.7872003149333332
0.4810370356
0.36477745473333345
0.27878168493333333
0.22616233793333332
0.2099558992
0.19642520439999997
0.15712115266666665
0.12593016553333333
0.1070913807333333
0.09168102113333336
0.19347256120000003
0.11306148466666667
0.08162048706666664
0.0764149794
0.06007008086666664
0.05242588039999996
0.04578363913333332
0.04629082739999999
0.03410292979999999
0.02816360140000001
0.034109343333333327
0.033494895933333324
0.030269106199999975
0.038871695733333336
0.02855877279999999
0.020326400799999998
0.01500175386666663
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
9.0
3.1261482838222223
4.3682849121244445
5.1820917596400005
3.8623944053600003
2.50975239176
1.5570160078355553
1.247574280368889
0.9092361642088889
0.7950118472666666
0.7113166025822223
0.6681508065644445
0.6282323818222223
0.5997006516666668
0.5780737460666667
0.5687115042844445
0.5678879282444446
0.6156066168222223
0.702904820928889
1.0588786864977777
1.543481472688889
1.9451486884444444
1.7423315385022227
1.958833291431111
1.4821014585333336
1.2706474055199999
1.0135373111866668
0.6514125476133332
0.5100631547244444
0.42876093184888886
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
(10,)
None
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
(1500,)
None
>>> np
<module 'numpy' from '/usr/local/lib/python3.5/site-packages/numpy/__init__.py'>
>>> np.array([1, 2, 3]) == np.array([1, 0, 3])
array([ True, False,  True])
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 52, in _wrapfunc
    return getattr(obj, method)(*args, **kwds)
AttributeError: 'list' object has no attribute 'argmax'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 79, in <module>
    print(accuracy(w, b, x, y))
  File "/Users/Finn/Documents/MNIST/mnist.py", line 56, in accuracy
    actual =  np.argmax(y, axis = 1)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 1004, in argmax
    return _wrapfunc(a, 'argmax', axis=axis, out=out)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 62, in _wrapfunc
    return _wrapit(obj, method, *args, **kwds)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 42, in _wrapit
    result = getattr(asarray(obj), method)(*args, **kwds)
numpy.core._internal.AxisError: axis 1 is out of bounds for array of dimension 1
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 60, in <module>
    x, y = data(size)
NameError: name 'size' is not defined
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 40
    loss = np.sum(scores)/size
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 46
    db = np.sum(db, axis = 0)/size
RuntimeWarning: invalid value encountered in true_divide

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 47
    dw = np.sum(dw, axis = 2)/size
RuntimeWarning: invalid value encountered in true_divide
nan

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 39
    scores[scores < 0] = 0
RuntimeWarning: invalid value encountered in less

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 41
    scores[scores > 0] = 1
RuntimeWarning: invalid value encountered in greater
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
0.09333333333333334
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 40
    loss = np.sum(scores)/size
RuntimeWarning: invalid value encountered in double_scalars

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 46
    db = np.sum(db, axis = 0)/size
RuntimeWarning: invalid value encountered in true_divide

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 47
    dw = np.sum(dw, axis = 2)/size
RuntimeWarning: invalid value encountered in true_divide
nan

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 39
    scores[scores < 0] = 0
RuntimeWarning: invalid value encountered in less

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 41
    scores[scores > 0] = 1
RuntimeWarning: invalid value encountered in greater
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
nan
0.09333333333333334
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
0.8306666666666667
0.81

1.8742612
0.8733333333333333
0.848

0.7652215058666664
0.902
0.868

0.48070840293333333
0.928
0.882

0.3359608912
0.9386666666666666
0.876

0.2560401617333333
0.9533333333333334
0.876

0.19881681199999998
0.9493333333333334
0.87

0.15068950306666667
0.968
0.874

0.11490777560000003
0.9573333333333334
0.862

0.1012825856
0.972
0.868

0.09015993386666671
0.9833333333333333
0.882

0.06827836586666663
0.9773333333333334
0.878

0.05414924773333333
0.9906666666666667
0.88

0.06866163413333332
0.9913333333333333
0.874

0.04622268746666668
0.9846666666666667
0.86

0.03868536746666668
0.9713333333333334
0.844

0.031239003466666655
0.992
0.864

0.04087584733333336
0.9926666666666667
0.876

0.03308599186666666
0.9873333333333333
0.866

0.027002121333333327
0.9946666666666667
0.87

0.02708243800000003
0.996
0.882

0.014433692266666642
0.9973333333333333
0.886

0.013198588133333319
0.988
0.858

0.015343482800000014
0.9966666666666667
0.878

0.011005417866666681
0.994
0.876

0.009677278133333377
0.9926666666666667
0.876

0.010519295333333293
0.9973333333333333
0.88

0.007831076933333313
0.9986666666666667
0.878

0.007350187333333337
1.0
0.88

0.005082559200000004
1.0
0.882

>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 112, in <module>
    test_examples(w, b, x_test, y_test)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 74, in test_examples
    redraw(x_test[r], y_test[r])
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in redraw
    pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
NameError: name 'screen' is not defined
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=================== RESTART: /Users/Finn/Documents/Game.py ===================
Traceback (most recent call last):
  File "/Users/Finn/Documents/Game.py", line 120, in <module>
    image_surf = pygame.image.load("key.png")
pygame.error: Couldn't open key.png
>>> 
================ RESTART: /Users/Finn/Documents/TicTacTie.py ================
X
>>> 
================== RESTART: /Users/Finn/Documents/dawing.py ==================
Traceback (most recent call last):
  File "/Users/Finn/Documents/dawing.py", line 34, in <module>
    fractal(dancer, 4)
  File "/Users/Finn/Documents/dawing.py", line 15, in fractal
    fractal(turtle, size-1)
  File "/Users/Finn/Documents/dawing.py", line 17, in fractal
    fractal(turtle, size-1)
  File "/Users/Finn/Documents/dawing.py", line 17, in fractal
    fractal(turtle, size-1)
  File "/Users/Finn/Documents/dawing.py", line 15, in fractal
    fractal(turtle, size-1)
  File "/Users/Finn/Documents/dawing.py", line 9, in fractal
    turtle.forward(1)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/turtle.py", line 1637, in forward
    self._go(distance)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/turtle.py", line 1605, in _go
    self._goto(ende)
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/turtle.py", line 3158, in _goto
    screen._pointlist(self.currentLineItem),
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/turtle.py", line 755, in _pointlist
    cl = self.cv.coords(item)
  File "<string>", line 1, in coords
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/tkinter/__init__.py", line 2308, in coords
    self.tk.call((self._w, 'coords') + args))]
_tkinter.TclError: invalid command name ".4506542432"
>>> 
================ RESTART: /Users/Finn/Documents/CheckersAI.py ================
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 130, in <module>
    interactive(w, b)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 100, in interactive
    redraw(x, predict(w, b, x))
TypeError: redraw() missing 1 required positional argument: 'screen'
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 129, in <module>
    test_examples(w, b, x_test, y_test)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 83, in test_examples
    redraw(x_test[r], predict(w, b, x_test[r]))
TypeError: redraw() missing 1 required positional argument: 'screen'
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 132, in <module>
  File "/Users/Finn/Documents/MNIST/mnist.py", line 101, in interactive
    for x in range(c[0]-1, c[0]+2):
TypeError: 'int' object does not support item assignment
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 134, in <module>
    interactive(w, b)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 103, in interactive
    x[28*yy+xx] = 255
IndexError: index 784 is out of bounds for axis 0 with size 784
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 112
    x = w[i]/np.max(w[i])
RuntimeWarning: invalid value encountered in true_divide

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 156, in <module>
    weight_display(w)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 125, in weight_display
    redraw(x, i, screen)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 66, in redraw
    pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
IndexError: index 10 is out of bounds for axis 0 with size 10
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 158, in <module>
    weight_display(w)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 124, in weight_display
    x = w[i]
IndexError: index 10 is out of bounds for axis 0 with size 10
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
[[0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 ...
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]
 [0. 0. 0. ... 0. 0. 0.]]

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
[0.003167  0.0032352 0.004146  0.0032954 0.0042888 0.0033092 0.002495
 0.0041544 0.0035114 0.0036778]

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============================== RESTART: Shell ===============================
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

============= RESTART: /Users/Finn/Documents/MNIST/mnist_disp.py =============
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 155, in <module>
    test_examples(w, b, x_test, y_test)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 105, in interactive
    redraw(x, predict(w, b, x), screen)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 67, in redraw
    pygame.display.flip()
KeyboardInterrupt
>>> np.minimum([1, 3, 4, 5, 1, -9])
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    np.minimum([1, 3, 4, 5, 1, -9])
ValueError: invalid number of arguments
>>> np.minimum(np.array([1, 3, 4, 5, 1, -9]))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    np.minimum(np.array([1, 3, 4, 5, 1, -9]))
ValueError: invalid number of arguments
>>> np.min(np.array([1, 3, 4, 5, 1, -9]))
-9
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 159, in <module>
    weight_display(w)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 115, in weight_display
    x[j] = w[j]
ValueError: setting an array element with a sequence.
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
(784,)

=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist.py", line 160, in <module>
    weight_display(w)
  File "/Users/Finn/Documents/MNIST/mnist.py", line 111, in weight_display
    print(a.shape)
NameError: name 'a' is not defined
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
3.7191966565333336
1.8742612
0.7652215058666664
0.48070840293333333
0.3359608912
0.2560401617333333
0.19881681199999998
0.15068950306666667
0.11490777560000003
0.1012825856
0.09015993386666671
0.06827836586666663
0.05414924773333333
0.06866163413333332
0.04622268746666668
0.03868536746666668
0.031239003466666655
0.04087584733333336
0.03308599186666666
0.027002121333333327
0.02708243800000003
0.014433692266666642
0.013198588133333319
0.015343482800000014
0.011005417866666681
0.009677278133333377
0.010519295333333293
0.007831076933333313
0.007350187333333337
0.005082559200000004
1.0
0.882

=============================== RESTART: Shell ===============================
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 155, in <module>
    w, b, l = step(w, b, batch_x, batch_y, rate)
TypeError: step() missing 2 required positional arguments: 'y' and 'rate'
>>> 
================= RESTART: /Users/Finn/Documents/MNIST/h.py =================
>>> 
================= RESTART: /Users/Finn/Documents/MNIST/h.py =================
>>> 
================= RESTART: /Users/Finn/Documents/MNIST/h.py =================
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 134, in <module>
    w1 = np.random.randn([784, 500]) *.01
  File "mtrand.pyx", line 1420, in mtrand.RandomState.randn
  File "mtrand.pyx", line 1550, in mtrand.RandomState.standard_normal
  File "mtrand.pyx", line 167, in mtrand.cont0_array
TypeError: 'list' object cannot be interpreted as an integer
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 38, in step
    scores1[scores > 0] = 1
NameError: name 'scores' is not defined
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 45, in step
    scores[scores2 > 0] = 1
NameError: name 'scores' is not defined
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 47, in step
    scores[np.arange(size), y] = -correct_grads
NameError: name 'scores' is not defined
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 48, in step
    db2 = scores
NameError: name 'scores' is not defined
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 50, in step
    db1 = (db2[:, :, np.newaxis]*w2[:, np.newaxis]).transpose()
ValueError: operands could not be broadcast together with shapes (50,10,1) (500,1,10) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 50, in step
    db1 = np.dot(db2[:, :, np.newaxis]*w2[:, np.newaxis])
ValueError: operands could not be broadcast together with shapes (50,10,1) (500,1,10) 
>>> 
>>> np.zeros([50, 10, 1]) * np.zeros([500, 1, 10])
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    np.zeros([50, 10, 1]) * np.zeros([500, 1, 10])
ValueError: operands could not be broadcast together with shapes (50,10,1) (500,1,10) 
>>> np.zeros([50, 10, 1]) * np.zeros([500, 10])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    np.zeros([50, 10, 1]) * np.zeros([500, 10])
ValueError: operands could not be broadcast together with shapes (50,10,1) (500,10) 
>>> np.zeros([50, 10]) * np.zeros([500, 10])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    np.zeros([50, 10]) * np.zeros([500, 10])
ValueError: operands could not be broadcast together with shapes (50,10) (500,10) 
>>> np.zeros([50, 1, 10]) * np.zeros([500, 10])
array([[[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       ...,

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]],

       [[0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        ...,
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.],
        [0., 0., 0., ..., 0., 0., 0.]]])
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 50, in step
    db1 = np.dot(db2[:, np.newaxis, :]*w2).transpose()
TypeError: Required argument 'b' (pos 2) not found
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 51, in step
    dw1 = (db1[:, :, np.newaxis]*x[:, np.newaxis]).transpose()
ValueError: operands could not be broadcast together with shapes (10,500,1,50) (50,1,784) 
>>> 
>>> (np.zeros([10, 500, 1, 50]) * np.zeros([50, 1, 784])).shape
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    (np.zeros([10, 500, 1, 50]) * np.zeros([50, 1, 784])).shape
ValueError: operands could not be broadcast together with shapes (10,500,1,50) (50,1,784) 
>>> (np.zeros([10, 500, 50]) * np.zeros([50, 1, 784])).shape
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    (np.zeros([10, 500, 50]) * np.zeros([50, 1, 784])).shape
ValueError: operands could not be broadcast together with shapes (10,500,50) (50,1,784) 
>>> 
>>> (np.zeros([10, 500, 50]) * np.zeros([50, 784])).shape
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    (np.zeros([10, 500, 50]) * np.zeros([50, 784])).shape
ValueError: operands could not be broadcast together with shapes (10,500,50) (50,784) 
>>> (np.zeros([10, 500, 50, 1]) * np.zeros([50, 1, 784])).shape
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    (np.zeros([10, 500, 50, 1]) * np.zeros([50, 1, 784])).shape
ValueError: operands could not be broadcast together with shapes (10,500,50,1) (50,1,784) 
>>> 
>>> (np.zeros([10, 500, 50]) * np.zeros([784, 50])).shape
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    (np.zeros([10, 500, 50]) * np.zeros([784, 50])).shape
ValueError: operands could not be broadcast together with shapes (10,500,50) (784,50) 
>>> (np.zeros([10, 500, 1, 50]) * np.zeros([784, 50])).shape
(10, 500, 784, 50)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(10, 500, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1[:, :, np.newaxis]*x[:, np.newaxis]).transpose()
ValueError: operands could not be broadcast together with shapes (10,500,1,50) (50,1,784) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(10, 500, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = np.dot(db1[:, :, np.newaxis], x[:, np.newaxis]).transpose()
ValueError: shapes (10,500,1,50) and (50,1,784) not aligned: 50 (dim 3) != 1 (dim 1)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 50, in step
    db1 = np.dot(db2[:, np.newaxis, :], w2).transpose()
ValueError: shapes (50,1,10) and (500,10) not aligned: 10 (dim 2) != 500 (dim 0)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1[:, :, np.newaxis]*x[:, np.newaxis]).transpose()
ValueError: operands could not be broadcast together with shapes (500,1,1,50) (50,1,784) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1[:, :, np.newaxis]*x[:, np.newaxis]).transpose()
ValueError: operands could not be broadcast together with shapes (500,1,1,50) (50,1,784) 
>>> 
>>> (np.zeros([500, 50])*np.zeros([50, 784])).shape
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    (np.zeros([500, 50])*np.zeros([50, 784])).shape
ValueError: operands could not be broadcast together with shapes (500,50) (50,784) 
>>> (np.zeros([500, 50])*np.zeros([784, 50])).shape
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    (np.zeros([500, 50])*np.zeros([784, 50])).shape
ValueError: operands could not be broadcast together with shapes (500,50) (784,50) 
>>> (np.zeros([500, 1, 50])*np.zeros([784, 50, 1])).shape
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    (np.zeros([500, 1, 50])*np.zeros([784, 50, 1])).shape
ValueError: operands could not be broadcast together with shapes (500,1,50) (784,50,1) 
>>> (np.zeros([500, 50, 1])*np.zeros([784, 1, 50])).shape
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    (np.zeros([500, 50, 1])*np.zeros([784, 1, 50])).shape
ValueError: operands could not be broadcast together with shapes (500,50,1) (784,1,50) 
>>> (np.zeros([500, 1, 50])*np.zeros([784, 50])).shape
(500, 784, 50)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1[:, :, np.newaxis]*x[:, np.newaxis]).transpose()
ValueError: operands could not be broadcast together with shapes (500,1,1,50) (50,1,784) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1*x).transpose()
ValueError: operands could not be broadcast together with shapes (500,1,50) (50,784) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(50, 784, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50) (50, 784, 500) (50, 10) (500, 10, 50)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 50, in step
    db1 = np.dot(db2[:, np.newaxis, :], w2).transpose()
ValueError: shapes (50,1,10) and (500,10) not aligned: 10 (dim 2) != 500 (dim 0)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50) (50, 784, 500) (50, 10) (50, 10, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50) (50, 784, 500) (50, 10) (50, 10, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50) (50, 784, 500) (50, 10) (50, 10, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50) (50, 784, 500) (50, 10) (50, 10, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 57, in step
    w1 -= dw1*rate
ValueError: operands could not be broadcast together with shapes (784,500) (50,784) (784,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 50) (50, 784, 500) (50, 10) (50, 10, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 58, in step
    b1 -= db1*rate
ValueError: non-broadcastable output operand with shape (500,) doesn't match the broadcast shape (500,500)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1) (784, 500) (10,) (50, 10)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 58, in step
    b1 -= db1*rate
ValueError: non-broadcastable output operand with shape (500,) doesn't match the broadcast shape (500,500)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1) (784, 500) (10,) (50, 10)
(500,)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 146, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 59, in step
    b1 -= db1*rate
ValueError: non-broadcastable output operand with shape (500,) doesn't match the broadcast shape (500,500)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 144, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 58, in step
    w2 -= dw2*rate
ValueError: operands could not be broadcast together with shapes (500,10) (50,10) (500,10) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500,) (784, 500) (10,) (50, 10)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 59, in step
    w2 -= dw2*rate
ValueError: operands could not be broadcast together with shapes (500,10) (50,10) (500,10) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500,) (784, 500) (10,) (50, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 59, in step
    w2 -= dw2*rate
ValueError: operands could not be broadcast together with shapes (500,10) (50,500) (500,10) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500,) (784, 500) (10,) (10, 500)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 145, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 59, in step
    w2 -= dw2*rate
ValueError: operands could not be broadcast together with shapes (500,10) (10,500) (500,10) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
(500,) (784, 500) (10,) (500, 10)
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
8.25515982376857
6.691046857345484

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
7.955205013254341
6.253645622220358
4.865890034979467
3.8807598563521295
3.265451826112993
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 148, in <module>
    print(accuracy(w, b, x_train, y_train))
NameError: name 'w' is not defined
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
8.145452053479818
6.462655094463392
5.110463447594076
4.13828795461576
3.5053625839106095
0.7633333333333333
0.752

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
8.374728637702272
7.460438835752398
6.5879242399386335
5.781583786056613
5.114977348370382
0.6946666666666667
0.658

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
8.489630345769246

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
5.82160545214521
2.624464033295929
1.941222756576656
1.6612426854341662
1.5035725336205383
1.3930576442661824
1.3128311312524528
1.2474524642074067
1.1914027120094592
1.1486842903796062
1.1112827218575205
1.0773867463716946
1.0486119073503677
1.0194326310093742
0.9950297481993491
0.8786666666666667
0.878
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 153, in <module>
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 120, in interactive
    redraw(x, predict(w1, b1, w2, b2, x), screen)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 63, in predict
    scores = np.dot(x, w1) + b1
ValueError: shapes (784,) and (500,10) not aligned: 784 (dim 0) != 500 (dim 0)
>>> a,b = 1, 2
>>> a
1
>>> a, b
(1, 2)
>>> a, b *= 2
SyntaxError: illegal expression for augmented assignment
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
5.850821133819042
2.713612339761705

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
0.09933333333333333
0.116
(784, 500)
(784, 500)
(784, 500)
(784, 500)
(784, 500)
(784, 500)
(784, 500)
(784, 500)
(784, 500)

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
0.11133333333333334
0.124
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 154, in <module>
    interactive(w1, b1, w2, b2)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 120, in interactive
    redraw(x, predict(w1, b1, w2, b2, x), screen)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 63, in predict
    scores = np.dot(x, w1) + b1
ValueError: shapes (784,) and (500,10) not aligned: 784 (dim 0) != 500 (dim 0)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
0.11933333333333333
0.112
(500, 10)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 155, in <module>
    interactive(w1, b1, w2, b2)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 121, in interactive
    redraw(x, predict(w1, b1, w2, b2, x), screen)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 64, in predict
    scores = np.dot(x, w1) + b1
ValueError: shapes (784,) and (500,10) not aligned: 784 (dim 0) != 500 (dim 0)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
0.076
0.056
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 155, in <module>
    interactive(w1, b1, w2, b2)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 121, in interactive
    redraw(x, predict(w1, b1, w2, b2, x), screen)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 63, in predict
    scores = np.dot(x, w1) + b1
ValueError: shapes (784,) and (500,10) not aligned: 784 (dim 0) != 500 (dim 0)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
0.09533333333333334
0.092

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
5.6320319553349805
2.55487157292376
1.918534839620798
1.6481891378130367
1.4903421994556882
1.3747415774010547
1.2916090139347376
1.2237816274998157
1.1768198989502043
1.1344921071936063
1.095373101791889
1.0623183951527415
1.0315188261930726
1.0054605805627577
0.9807895120692469
0.8753333333333333
0.856
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
5.827049909821732
2.557390204508522
1.8964529701768156
1.6182276329520633
1.468521663612855
1.3600090885209222
1.2816954458873184
1.2215936627009516
1.1685555980050273
1.1242698324735054
1.0843858422649408
1.0522698922687812
1.0234246397687616
0.9974268699703468
0.9713766351332649
0.8853333333333333
0.866

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
9.1648439391554
8.599295951713932

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
5.883130112658646
2.636250374471889
1.9516110928759167
1.6606905466530135

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.0468813042564387
1.1882322609712976
0.9750025157692522
0.8577873383413862
0.783515936353931
0.7268591730298894
0.6798759861024274
0.6451138479972527
0.6106125991393292
0.5845665421363221
0.5621708997502569
0.5437981647417758
0.5230643348698856
0.5077730644859423
0.4943459467550499
0.9166666666666666
0.906

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.1332667764217903
1.463971001705614
1.385814169124374
1.3944510551293616
1.4195653113589954
1.4350585304102366
1.4414095676626304
1.440644830881998
1.4359984411208133

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.0897964261082285
1.1901416645578242
0.9839556918186722
0.8765839766211883
0.8068816090793482
0.7554357563587871
0.7171435089408249
0.6835006064632873
0.6592549441827403
0.637032254175798
0.6161152997797064
0.597148309536584
0.5853364864147107
0.5709968598046437
0.5610120304613427
0.9166666666666666
0.898

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.118343597791753
1.2253515323411128
1.0118917998458277
0.894353928725777
0.8229643209760302
0.7655082079851184
0.7241375467584976
0.6813075137896197
0.6482607845835187
0.6197609991088983
0.5989360508259546
0.5731469933027139
0.5521614434324853
0.5364835961785298
0.5225367118652536
0.914
0.902

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 51, in step
    db1 = relu_grad*scores1
ValueError: operands could not be broadcast together with shapes (500,1,100) (100,500) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (500,500,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (500,500,100) (784,100) 
>>> def step (w1, b1, w2, b2, x, y, rate):
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

>>> (np.zeros([500, 10]) * np.zeros([500, 10])).shape
(500, 10)
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 500, 100)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 175, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (500,500,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 100) (500, 100)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 176, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 54, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (500,500,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 1, 100) (500, 100)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 176, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 54, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (500,500,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 51, in step
    db1 = relu_grad.squeeze*scores1.transpose()
TypeError: unsupported operand type(s) for *: 'builtin_function_or_method' and 'float'
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (500,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (100,500) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1.transpose()[:, np.newaxis]*x.transpose).transpose()
TypeError: unsupported operand type(s) for *: 'float' and 'builtin_function_or_method'
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 52, in step
    dw1 = (db1.transpose()[:, np.newaxis]*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (100,1,500) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 174, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    db1 = np.sum(db1, axis = 2).squeeze()/size
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 1882, in sum
    out=out, **kwargs)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/_methods.py", line 32, in _sum
    return umr_sum(a, axis, dtype, out, keepdims)
numpy.core._internal.AxisError: axis 2 is out of bounds for array of dimension 2
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
(500, 100)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 175, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 54, in step
    db1 = np.sum(db1, axis = 2).squeeze()/size
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 1882, in sum
    out=out, **kwargs)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/_methods.py", line 32, in _sum
    return umr_sum(a, axis, dtype, out, keepdims)
numpy.core._internal.AxisError: axis 2 is out of bounds for array of dimension 2
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
20.257829585392024
0.41838766133013205
0.16373090194546322
0.08009101490092882
0.04507691455276652
0.025588752307044542
0.01616315229285835
0.007481124719184458
0.003578337178972629
0.0027179815497329093
0.0019779648611585265
0.000511170046464282
0.0004933010632778181
0.000426449862326852
0.0006612309892681622
0.8966666666666666
0.822

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
7.268915687001505
1.3341019264059155
0.8417144039293107
0.6180714674706832
0.47782046765517255
0.3827530621794715
0.3106188534171782
0.2623572742402
0.220348848509313
0.1838760342887976
0.15198221928591485
0.13061694028143142
0.11004905921152136
0.09736321777493143
0.08377766940714118
0.5386666666666666
0.502

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
5.888808814759568
1.3547936121731425
0.8722265510866075
0.6232991032052041
0.4779729535756889
0.3781970909537934
0.31050004063460857
0.2648898530175182
0.22498994008793
0.19034527221667327
0.1650166789163942
0.13919396372863968
0.12046669556286797
0.10633770686401135
0.0939692515114726
0.9746666666666667
0.824

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
21.184947907335
0.42180646111441983
0.1486221605770148
0.0777591939212651
0.03981694804752986
0.027733661930998306
0.01420799773216968
0.009459939304133979
0.003704242707944291
0.001846208986920103
0.0019010062097641713
0.0006228390202991964
0.00021654317976371667
0.00016348778376310103
2.9979070125421297e-05
1.0
0.886

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
20.311511134679524
0.47832386986488784
0.19453093765745513
0.09412714830918523
0.05056092424927028
0.02838992486892226
0.017025732724641068
0.007859435251260934
0.0065078280672969295
0.0026806909623197537
0.0025032986034428713
0.0010817278744276982
0.0005847489653125162
0.0001640456117163366
0.00010363654677347167
1.0
0.882

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.078727644703131
1.2467558003313806
1.0220120428468442
0.8979145572805703
0.8272014699817097
0.7664359775316057
0.721381130726333
0.6802636187477552
0.6454880774261297
0.6174212703249259
0.589550480407264
0.5669993323950266
0.545214430274503
0.5285418645558277
0.5161523066846911
0.916
0.91

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.0617636226444733
1.206742619174379
0.9822194568505548

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
17.312170160863193
0.3963160047543284
0.1548772909950465
0.07627166279281934
0.03928920863785987
0.02075457019713686
0.01837254452331722
0.008609114462894179
0.004833136718377053
0.0034492664689380983
0.002056436485346258
0.00045385786466148955
0.00014891619169777232
0.00033003642957707814
0.0002153822809325095
1.0
0.866

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
24.70780162477879
0.4661869363256551
0.2102690397248881
0.16308608009821773
0.16722905888942877
0.1506221762593775
0.15311525670693507
0.10877780816416685

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
22.033411931873125
0.4438991513981121
0.17950340814569243
0.0961250493105765
0.05973082001845232
0.03834538012703639
0.026654120595391233
0.02648233147630504
0.022094327446181027
0.014129962030364493
0.011130850462912931
0.012714935472451734
0.01975455344656564
0.018463614442451776
0.011534390704658152
1.0
0.896

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
19.11975512725127
0.499695658925555
0.19075426910568422
0.09807355240606576
0.059440507060498936
0.039069988437545076
0.025537655156110693
0.01861778556204722
0.010154157895034654
0.008187927249791956
0.006901333266091469
0.008147741576594113
0.00699857209856949
0.0053519456844051015
0.005296597646100828
1.0
0.9

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
19.522621742911955
0.4247537865382365
0.16666033941681058
0.08143087525700432
0.043180258869464534
0.025446041802590545
0.01967493444705598
0.0104902308692276
0.008332570362439397
0.010446498499134867
0.008772230298049306
0.003788359518397196
0.007096803484713756
0.0077152090919351286
0.008410506640543564
1.0
0.902

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
15.47947007214766
0.41317319036982997
0.15686227777900544
0.08137957250126883
0.05277959352279562
0.03364425063654438
0.023719740732833942
0.018532375711747467
0.012975309938517572
0.013877011424755916
0.011531773862040792
0.00852710408327817
0.008680364323690517
0.010237186973507282
0.010249622891149748
1.0
0.898

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.1040620993301236
1.2071790427057218
1.0120858550768628
0.9181296401896425
0.8585417865806887
0.8168700129425301
0.7839577000878641
0.7630661165948888
0.7407309498960537
0.727715847151085
0.7131232897332201
0.7015748330344951
0.6912706335459414
0.6837368896485613
0.6768637918284177
0.908
0.9

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2.7874836387463517
0.826892098081036
0.6451957796525332
0.5608876170176434
0.5032087696299024
0.46714213463279525
0.440989777883824
0.4222283535996048
0.41213440345729496
0.40075823332372945
0.39148230107700704
0.38302157235530937
0.37883655404265787
0.3746915554645152
0.3732030866232389
0.9313333333333333
0.896

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2.9397926912526486
0.842703066541961
0.6771167444882675
0.5850168254325344
0.5348975682845405
0.5028219642823032
0.4728615204443625
0.45866542902894614
0.44403057285939196
0.43229240384166817
0.4236357524852826
0.4185179141477379
0.417499334206112
0.4119160740505225
0.4153342404460722
0.9373333333333334
0.9

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
1.6292464392859385
0.6093314094930384
0.5216271073281062
0.47544548173959045
0.44684740187384503
0.4277567716061716
0.4170276777144629
0.41102361790345493
0.40868939000043514
0.4071130182422218
0.4075009279343055
0.408802685711025

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
1.9802064942301871
0.6182961777379962
0.49176058565365294
0.4342243145959407
0.39260306862935607
0.36680609012925375
0.34741055043946817
0.33262345694964723
0.32297792871663616
0.309828305539375
0.3030774622319974
0.29429795676858256
0.2864250709401288
0.28179119925155416
0.27895172781140193
0.27417059459480847
0.2720765470390403
0.26717533138809685
0.26568475996021845
0.2634563995159109
0.26465054785278214
0.26419584485369507
0.263902698930795
0.26341271387596293
0.2632032965168573
0.26502107890762827
0.26668767579310565
0.2690877951888109
0.2702094014120339
0.2743110085842738
0.9405333333333333
0.9056

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
1.1928761601354436
0.4551797481715333
0.39234030837624895
0.35375259452106905
0.3311872420033598
0.3138531881844871
0.30479667882990497
0.29720430550066523
0.2916851091985036
0.2882549983252246
0.28471761075152513
0.2837048812841818
0.2821362341651758
0.2809321277694563
0.2814868284311592
0.28219678643458423
0.28363879858189195
0.28522010953965005
0.9396
0.9044

=============================== RESTART: Shell ===============================
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
1.165424373859393

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.1505377291002006
1.2417910227705662
1.0227267208743995
0.922602047264435
0.8533140959773443
0.8062578455758661
0.7688867221013557
0.7388603065163669
0.7171636985182169
0.6971669297399454
0.681607299291053
0.6659587919717358
0.6557666026236307
0.6464307967717063
0.6362656589675558
0.6306947984166487
0.6266952675961036
0.6213217302755846
0.9093333333333333
0.894
>>> 
=============================== RESTART: Shell ===============================
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.0602870002119684
1.155365542525248
0.9535100381846143
0.8525202021054736
0.7803895529950216
0.7323341426423795
0.6923206695571348
0.6595669574716249
0.6279915756782669
0.6054770444205887
0.5891020071132085
0.5703703471085222
0.5565612563304835
0.5430157874469896
0.5302825349915623
0.5223098417694192
0.5096992328449491
0.501241785899318
0.9193333333333333
0.904

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
3.1153578452321335
1.2226646943020083
1.0064517267898092
0.8963594652922094
0.8238324428776692
0.7720447380317023
0.7320340003120819
0.7019365495733486
0.6749186605104049
0.6476958470056682
0.626003556707291
0.6046273921246147
0.5875136329004095
0.5754216912566761
0.5619157165491656
0.5496966159556368
0.5409271939804631
0.5322737225962453
0.9153333333333333
0.894

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2.723896738498548
0.7968812976391176
0.6280317270887201
0.5295897334415092
0.46924611964276913
0.4248933731508542
0.3942304242661227
0.3695007067557962
0.34953633015711977
0.33267861249415875
0.31914119858605816

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.001 0.95 1 1000 18
2.8170091790939313
0.7884566965852652
0.6145639489939858
0.5279491217990251
0.4667841694945238
0.42552555707526435
0.3947728523388315
0.37413770035034294
0.352727205408995
0.33370984694226646
0.3197469714204622
0.3057624047812003
0.2940498436871023
0.2840378261086268
0.27794909822329983
0.2704504001556129
0.26507975558821395
0.2603441156361999
0.9413333333333334
0.912

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.001 0.92 1 1000 18
2.743575039742279
0.7793245977813065
0.6186843526164371
0.5289564638271125
0.48130157952021946
0.4385106013083013
0.40775108482071787
0.38551312990701364
0.3670058097518561
0.3538510051073305
0.34269336316899857
0.33342150856675656
0.32261940840861475
0.31279138249759453
0.3065299021964455
0.2993267218458003
0.2932843831177043
0.2887547382761103
0.94
0.902

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
2.9329377036593156
0.7787281367802337
0.6005367718992568
0.5100206614966135
0.45305262171250515
0.4095632676474253
0.38010568690295354
0.3558445771932794
0.3378266572556898
0.32180924267529054
0.3101867362933949
0.299358986867733
0.2898509553720664
0.28075324623247633
0.27298102902991556
0.2669087482336308
0.26211969681357095
0.2577412904018664
0.9413333333333334
0.906

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
2.8550012018205075

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 0
0.11066666666666666
0.104
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 165, in <module>
    interactive(w1, b1, w2, b2)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 121, in interactive
    x[28*b+a] = 255
IndexError: index 979 is out of bounds for axis 0 with size 784
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 0
0.04733333333333333
0.052

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
2.8981687432614294
0.8134896931463906
0.5905723041090656
0.49796105009194463
0.44569818256189186
0.4059525591227837
0.3743441902308248
0.3509902208848284
0.334011205243169
0.32003487990249274
0.30698549678181636
0.29612333306743494
0.2885785747102748
0.27935154958254027
0.2713118982156411
0.26513012592969465
0.25839498714708015
0.253806968375015
0.94
0.908

=============================== RESTART: Shell ===============================
>>> 
=============== RESTART: /Users/Finn/Documents/MNIST/mnist.py ===============
1.583010584906667
0.9104505883466664
0.7023985433600001
0.5235421097066664
0.4693313579733335
0.42268583930666653
0.4233823841333333
0.35593143693333334
0.4526896394399997
0.3391583900799998
0.30224014856
0.3711956995200001
0.2845153861066667
0.2662110728799999
0.24292121631999994
0.25055907677333344
0.2209854271199999
0.2252115423999999
0.20783711165333338
0.27067163207999995
0.21336393791999986
0.1926730340533333
0.19044868285333347
0.18732389882666672
0.18395339906666686
0.18092021413333334
0.17442082053333324
0.25195485917333327
0.16669952712000005
0.1597553350133333
0.9396
0.8676

============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
2.9239275261414237
0.7727290428582304
0.5942445321574953
0.5038996823916964
0.442032959837837
0.40227194002990285
0.37512831405928326
0.34987192936022865
0.3320483123350323
0.3149873734810464
0.3022834319597671
0.2911247897847981
0.27939869826556946
0.2709772551799643
0.2640905270289129
0.25589994927624676
0.25138141802543734
0.24629216438861573
0.944
0.904
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 165, in <module>
    interactive(w1, b1, w2, b2)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 122, in interactive
    redraw(x, predict(w1, b1, w2, b2, x), screen)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 82, in redraw
    pygame.display.flip()
KeyboardInterrupt
>>> a = np.array([1, 2, 3])
>>> b = a
>>> b[b < 2] = 2
>>> b
array([2, 2, 3])
>>> a
array([2, 2, 3])
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 51, in step
    relu_grads *= scores1
ValueError: operands could not be broadcast together with shapes (1000,1,100) (100,1000) (1000,1,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 51, in step
    relu_grads= relu_grads.squeeze()*scores1
ValueError: operands could not be broadcast together with shapes (1000,100) (100,1000) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (1000,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (100,1000) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (100,1,1000) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 51, in step
    relu_grads= relu_grads.squeeze()*scores1
ValueError: operands could not be broadcast together with shapes (1000,100) (100,1000) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (1000,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 51, in step
    relu_grads= relu_grads.squeeze().transpose()*scores1.transpose()
ValueError: operands could not be broadcast together with shapes (100,1000) (1000,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (100,1000) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 180, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnist2layer.py", line 53, in step
    dw1 = (db1*x.transpose()).transpose()
ValueError: operands could not be broadcast together with shapes (1000,100) (784,100) 
>>> 
============ RESTART: /Users/Finn/Documents/MNIST/mnist2layer.py ============
2000 1500 100 0.002 0.92 1 1000 18
144.60803898471846
3.633374006862241
0.4458575918546391
0.20412249776345456
0.09921331149908422
0.07081826179276894
0.03888764475904778
0.024788933499296582
0.017228854681224707
0.011425469157971371
0.007118033044618855
0.0034961759890531478
0.0022340850241715942
0.001210798978091806
0.0007114748045510169
0.000654392659785545
0.0005132522594180432
0.0004623892771795613
0.858
0.802

========== RESTART: /Users/Finn/Documents/MNIST/mnist2layerrelu.py ==========
2000 1500 100 0.002 0.92 0.99 1000 18
127.88030638667692
1.563226031666391
0.34331460500362054
0.14331784824568572
0.06244084045108076
0.04298920616307887
0.02428339115250723
0.014714880669565803
0.010364901457914326
0.005679131227357596
0.003260037168257781
0.0019083443694195117
0.0016801083316062748
0.0009702704771676762
0.0004874599780340687
0.00022755638831764411
0.0005787817208674246
0.0002700818622760111
1.0
0.886

========== RESTART: /Users/Finn/Documents/MNIST/mnist2layerrelu.py ==========
2000 1500 100 0.002 0.91 0.98 1000 18
153.12532880305986
5.743798292484487
0.5168476513799196
0.3051900843831313
0.27457371389305

========== RESTART: /Users/Finn/Documents/MNIST/mnist2layerrelu.py ==========
2000 1500 100 0.002 0.91 0.99 1000 18
97.82736784417081
6.295500113320666
0.4197859735668332
0.16656806364304844
0.0693260211139779
0.03993049880268273
0.024197414856175874
0.017262198031082764
0.009760578283505484
0.008522352698978913
0.005319472971168969
0.003351886782458171
0.0027899138076540797
0.0019588810438272096
0.0015338492318081617
0.0014764028542214272
0.000958953533828289
0.0010979927118736485
1.0
0.902

========== RESTART: /Users/Finn/Documents/MNIST/mnist2layerrelu.py ==========
2 layer fully connected relu activation
2000 1500 100 0.002 0.9 0.99 1000 18
117.7310460433324
0.9489793199769567
0.3124603698086774
0.1264416334032827
0.06683776553246637
0.03877375852363296
0.02493490762925741
0.01726854890429823
0.011517874496396205
0.008428697874400152
0.007108184603209496
0.0054871376587797135
0.004388623397944364
0.0039140153369321366
0.003368569989495049
0.0031466449414245807
0.002803030958503545
0.00302012339857789
0.9993333333333333
0.914

============= RESTART: /Users/Finn/Documents/MNIST/mnistconv.py =============
1 conv layer 3x3x5 finn activation 1 fully connected layer
2000 1500 100 0.0025 0.92 1 1000 18
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistconv.py", line 152, in <module>
    w1, b1, w2, b2, l = step(w1, b1, w2, b2, batch_x, batch_y, rate)
  File "/Users/Finn/Documents/MNIST/mnistconv.py", line 36, in step
    conv_scores = conv(c, cb, x)
NameError: name 'conv' is not defined
>>> 
========== RESTART: /Users/Finn/Documents/MNIST/mnist2layerrelu.py ==========
2 layer fully connected relu activation
2000 1500 100 0.002 0.9 0.99 1000 18
125.6390813758758

========== RESTART: /Users/Finn/Documents/MNIST/mnist2layerrelu.py ==========
2 layer fully connected relu activation
2000 1500 100 0.0025 0.9 0.99 1000 18
276.29893399742366
40.613150341522655
2.1263710100721
1.066475810115205
0.4189980072676352
0.23325305856012404
0.1534749389521031
0.10630663069250944
0.08315788648480635
0.06685368318166614
0.05405852994282319
0.04580359248718505
0.040203611427846016
0.03531564468281211
0.0316713795311889
0.02862306245603991
0.026377523229781305
0.024717780957340903
0.996
0.888

========== RESTART: /Users/Finn/Documents/MNIST/mnist2layerrelu.py ==========
2 layer fully connected relu activation
2000 1500 100 0.002 0.9 0.99 1000 18
116.67758852503852
3.65083943878462
0.5405143462652848
0.22021065636442924
0.11507669013404141
0.06859514238605904
0.04599231070509984
0.030174501905308477
0.023373509991356414
0.018847961342759522
0.014741656980074852
0.010848725565002134
0.008918867488142938
0.007292046972773764
0.006074075689985331
0.006306649284810407
0.0055487504719896105
0.004992471314088842
0.9986666666666667
0.9

=============================== RESTART: Shell ===============================
>>> 
