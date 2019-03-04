Python 3.5.1 (default, Dec 27 2015, 02:23:23) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 6000
training size: 5000
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 0.8597492718755957
epoch 0 time: 67.05105400085449
epoch 1 loss: 0.1637446792792139
epoch 1 time: 67.2454309463501
epoch 2 loss: 0.07173549844247205
epoch 2 time: 65.8423011302948
epoch 3 loss: 0.03394711544957865
epoch 3 time: 68.55126881599426
epoch 4 loss: 0.01611439722012165
epoch 4 time: 67.62682890892029
epoch 5 loss: 0.008462544018181443
epoch 5 time: 66.25348496437073
epoch 6 loss: 0.005727577980496588
epoch 6 time: 65.56966876983643
epoch 7 loss: 0.0029520803603307957
epoch 7 time: 65.67696499824524
epoch 8 loss: 0.002245130311126109
epoch 8 time: 65.79700088500977
epoch 9 loss: 0.0007373085719427682
epoch 9 time: 66.11801099777222
training accuracy: 0.9998
test accuracy: 0.948
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 222, in <module>
    print(net(x, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True))
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 200, in net
    interactive(w, b)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 143, in interactive
    redraw(x, predict(w, b, x), screen)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 103, in redraw
    pygame.display.flip()
KeyboardInterrupt
>>> np.convolve([1, 2, 3], [1, 1, 1])
array([1, 3, 6, 5, 3])
>>> import scipy as sp
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import scipy as sp
ImportError: No module named 'scipy'
>>> a
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a = np.array([1, 2, 3])
>>> a.strides
(8,)
>>> a = np.array([1, 2, 3], [4, 5, 6])
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a = np.array([1, 2, 3], [4, 5, 6])
TypeError: data type not understood
>>> a = np.array([[1, 2, 3], [4, 5, 6]])
>>> a.strides
(24, 8)
>>> a.strides+a.strides
(24, 8, 24, 8)
>>> 
>>> 



>>> 



}
>>> }}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
SyntaxError: invalid syntax
>>> 


>>> }
SyntaxError: invalid syntax
>>> 

>>> 



>>> 
>>> 


>>> 

>>> 


>>> 


>>> 





























}
>>> 

>>> 


>>> 
















>>> 
>>> 
>>> 



>>> 
>>> 
>>> 
>>> 
>>> }}}}}}    }
SyntaxError: invalid syntax
>>> a
array([[1, 2, 3],
       [4, 5, 6]])
>>> a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
>>> a = np.arange(5, 5)
>>> a
array([], dtype=int64)
>>> a = np.arange([5, 5])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a = np.arange([5, 5])
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> a = np.arange((5, 5))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a = np.arange((5, 5))
TypeError: arange: scalar arguments expected instead of a tuple.
>>> a = np.arange([5, 5])
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a = np.arange([5, 5])
TypeError: unsupported operand type(s) for -: 'list' and 'int'
>>> a = np.arange(5, 5)
>>> a
array([], dtype=int64)
>>> print(a)
[]
>>> a = np.random.randn(5, 5)
>>> a
array([[-0.10582781, -0.42407934, -1.52871656, -0.98471849, -0.13007223],
       [-1.35342538,  0.52258954, -0.69823949, -1.44172388, -0.92139979],
       [-1.03773858,  1.02540966,  1.33877828, -1.33807494,  0.41177745],
       [-0.43316018,  0.40584491, -1.28484915, -0.68099194,  0.25336489],
       [ 1.47122524, -1.40309361, -0.74567743, -1.46223436,  0.4907794 ]])
>>> sub = (3, 3)
>>> view = tuple(np.subtract(a.shape, sub)+1)+sub
>>> view
(3, 3, 3, 3)
>>> strides = a.strides+a.strides
>>> strides
(40, 8, 40, 8)
>>> subs = np.lib.stride_tricks.as_strided(a, view, strides)
>>> subs
array([[[[-0.10582781, -0.42407934, -1.52871656],
         [-1.35342538,  0.52258954, -0.69823949],
         [-1.03773858,  1.02540966,  1.33877828]],

        [[-0.42407934, -1.52871656, -0.98471849],
         [ 0.52258954, -0.69823949, -1.44172388],
         [ 1.02540966,  1.33877828, -1.33807494]],

        [[-1.52871656, -0.98471849, -0.13007223],
         [-0.69823949, -1.44172388, -0.92139979],
         [ 1.33877828, -1.33807494,  0.41177745]]],


       [[[-1.35342538,  0.52258954, -0.69823949],
         [-1.03773858,  1.02540966,  1.33877828],
         [-0.43316018,  0.40584491, -1.28484915]],

        [[ 0.52258954, -0.69823949, -1.44172388],
         [ 1.02540966,  1.33877828, -1.33807494],
         [ 0.40584491, -1.28484915, -0.68099194]],

        [[-0.69823949, -1.44172388, -0.92139979],
         [ 1.33877828, -1.33807494,  0.41177745],
         [-1.28484915, -0.68099194,  0.25336489]]],


       [[[-1.03773858,  1.02540966,  1.33877828],
         [-0.43316018,  0.40584491, -1.28484915],
         [ 1.47122524, -1.40309361, -0.74567743]],

        [[ 1.02540966,  1.33877828, -1.33807494],
         [ 0.40584491, -1.28484915, -0.68099194],
         [-1.40309361, -0.74567743, -1.46223436]],

        [[ 1.33877828, -1.33807494,  0.41177745],
         [-1.28484915, -0.68099194,  0.25336489],
         [-0.74567743, -1.46223436,  0.4907794 ]]]])
>>> a.strides
(40, 8)
>>> a.strides*2
(40, 8, 40, 8)
>>> subs.shape
(3, 3, 3, 3)
>>> np.dot(subs, np.ones([3, 3]))
array([[[[-2.05862372, -2.05862372, -2.05862372],
         [-1.52907533, -1.52907533, -1.52907533],
         [ 1.32644935,  1.32644935,  1.32644935]],

        [[-2.9375144 , -2.9375144 , -2.9375144 ],
         [-1.61737383, -1.61737383, -1.61737383],
         [ 1.02611299,  1.02611299,  1.02611299]],

        [[-2.64350729, -2.64350729, -2.64350729],
         [-3.06136316, -3.06136316, -3.06136316],
         [ 0.41248078,  0.41248078,  0.41248078]]],


       [[[-1.52907533, -1.52907533, -1.52907533],
         [ 1.32644935,  1.32644935,  1.32644935],
         [-1.31216442, -1.31216442, -1.31216442]],

        [[-1.61737383, -1.61737383, -1.61737383],
         [ 1.02611299,  1.02611299,  1.02611299],
         [-1.55999618, -1.55999618, -1.55999618]],

        [[-3.06136316, -3.06136316, -3.06136316],
         [ 0.41248078,  0.41248078,  0.41248078],
         [-1.7124762 , -1.7124762 , -1.7124762 ]]],


       [[[ 1.32644935,  1.32644935,  1.32644935],
         [-1.31216442, -1.31216442, -1.31216442],
         [-0.67754581, -0.67754581, -0.67754581]],

        [[ 1.02611299,  1.02611299,  1.02611299],
         [-1.55999618, -1.55999618, -1.55999618],
         [-3.61100541, -3.61100541, -3.61100541]],

        [[ 0.41248078,  0.41248078,  0.41248078],
         [-1.7124762 , -1.7124762 , -1.7124762 ],
         [-1.7171324 , -1.7171324 , -1.7171324 ]]]])
>>> np.random.randn(2, 2, 2, 2)
array([[[[-0.40999904, -2.47845991],
         [ 0.25078843,  1.90586928]],

        [[-0.98284176, -1.00092447],
         [-0.53979973, -1.49319363]]],


       [[[ 0.2696283 , -1.60672138],
         [-0.57336135, -0.01185459]],

        [[-0.03827209, -0.67128396],
         [-0.67198677,  0.06934013]]]])
>>> a = np.random.randn(2, 2, 2, 2)
>>> a*np.ones(2, 2)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a*np.ones(2, 2)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/numeric.py", line 188, in ones
    a = empty(shape, dtype, order)
TypeError: data type not understood
>>> a*np.ones([2, 2])
array([[[[-0.42408747, -1.63092228],
         [-0.02947991, -1.55171713]],

        [[-0.24375019, -0.11328142],
         [ 0.17909961,  0.78555776]]],


       [[[ 0.6191657 ,  0.2078083 ],
         [-1.42415164, -0.10901419]],

        [[ 1.301491  ,  0.3735204 ],
         [-0.18006181, -2.39083679]]]])
>>> np.dot(np.ones([3, 3]), np.ones([3, 3]))
array([[3., 3., 3.],
       [3., 3., 3.],
       [3., 3., 3.]])
>>> a
array([[[[-0.42408747, -1.63092228],
         [-0.02947991, -1.55171713]],

        [[-0.24375019, -0.11328142],
         [ 0.17909961,  0.78555776]]],


       [[[ 0.6191657 ,  0.2078083 ],
         [-1.42415164, -0.10901419]],

        [[ 1.301491  ,  0.3735204 ],
         [-0.18006181, -2.39083679]]]])
>>> a>1
array([[[[False, False],
         [False, False]],

        [[False, False],
         [False, False]]],


       [[[False, False],
         [False, False]],

        [[ True, False],
         [False, False]]]])
>>> if a>1:
	print("!!")

	
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    if a>1:
ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
>>> np.stretch(np.zeros([5, 5]))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    np.stretch(np.zeros([5, 5]))
AttributeError: module 'numpy' has no attribute 'stretch'
>>> np.flatten(np.zeros([5, 5]))
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    np.flatten(np.zeros([5, 5]))
AttributeError: module 'numpy' has no attribute 'flatten'
>>> np.reshape(np.zeros([5, 5]), -1)
array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0.])
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 222, in <module>
    x = process(x)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 209, in process
    subs = np.lib.stride_tricks.as_strided(image, view, strides)
  File "/usr/local/lib/python3.5/site-packages/numpy/lib/stride_tricks.py", line 102, in as_strided
    array = np.asarray(DummyArray(interface, base=x))
  File "/usr/local/lib/python3.5/site-packages/numpy/core/numeric.py", line 492, in asarray
    return array(a, dtype, copy=False, order=order)
ValueError: mismatch in length of strides and shape
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
(784,) (8, 8) (782, 782, 3, 3)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 223, in <module>
    x = process(x)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 210, in process
    subs = np.lib.stride_tricks.as_strided(image, view, strides)
  File "/usr/local/lib/python3.5/site-packages/numpy/lib/stride_tricks.py", line 102, in as_strided
    array = np.asarray(DummyArray(interface, base=x))
  File "/usr/local/lib/python3.5/site-packages/numpy/core/numeric.py", line 492, in asarray
    return array(a, dtype, copy=False, order=order)
ValueError: mismatch in length of strides and shape
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
(784,) (8, 8) (782, 782, 3, 3)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 223, in <module>
    x = process(x)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 210, in process
    subs = np.lib.stride_tricks.as_strided(image, view, strides)
  File "/usr/local/lib/python3.5/site-packages/numpy/lib/stride_tricks.py", line 102, in as_strided
    array = np.asarray(DummyArray(interface, base=x))
  File "/usr/local/lib/python3.5/site-packages/numpy/core/numeric.py", line 492, in asarray
    return array(a, dtype, copy=False, order=order)
ValueError: mismatch in length of strides and shape
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
(784,) (8,) (782, 782, 3, 3)
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 223, in <module>
    x = process(x)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 210, in process
    subs = np.lib.stride_tricks.as_strided(image, view, strides)
  File "/usr/local/lib/python3.5/site-packages/numpy/lib/stride_tricks.py", line 102, in as_strided
    array = np.asarray(DummyArray(interface, base=x))
  File "/usr/local/lib/python3.5/site-packages/numpy/core/numeric.py", line 492, in asarray
    return array(a, dtype, copy=False, order=order)
ValueError: mismatch in length of strides and shape
d
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 223, in <module>
    x = process(x)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 206, in process
    image = np.reshape(x, [32, 32])
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 257, in reshape
    return _wrapfunc(a, 'reshape', newshape, order=order)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 52, in _wrapfunc
    return getattr(obj, method)(*args, **kwds)
ValueError: cannot reshape array of size 1568000 into shape (32,32)
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 223, in <module>
    x = process(x)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 206, in process
    image = np.reshape(image, [32, 32])
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 257, in reshape
    return _wrapfunc(a, 'reshape', newshape, order=order)
  File "/usr/local/lib/python3.5/site-packages/numpy/core/fromnumeric.py", line 52, in _wrapfunc
    return getattr(obj, method)(*args, **kwds)
ValueError: cannot reshape array of size 784 into shape (32,32)
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 223, in <module>
    x = process(x)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 212, in process
    new += [np.reshape(np.einsum("ij,ijkl->kl", conv, subs), -1)]
  File "/usr/local/lib/python3.5/site-packages/numpy/core/einsumfunc.py", line 1069, in einsum
    return c_einsum(*operands, **kwargs)
ValueError: operands could not be broadcast together with remapped shapes [original->remapped]: (3,3)->(3,3) (26,26,3,3)->(3,3,26,26) 
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)
(676,)

===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 235, in <module>
    print(net(x, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True))
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 177, in net
    w, b, l = step(w, b, batch_x, batch_y, rate, margin)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 41, in step
    scores = np.dot(scores, w[i]) + b[i]
ValueError: shapes (15,676) and (784,1000) not aligned: 676 (dim 1) != 784 (dim 0)
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 47
    final_grad = (final.transpose() - correct_vals + 1).transpose()
RuntimeWarning: invalid value encountered in subtract

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 50
    final_grad[final_grad < 0] = 0
RuntimeWarning: invalid value encountered in less

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 53
    final_grad[final_grad > 0] = 1
RuntimeWarning: invalid value encountered in greater

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 42
    scores[scores < 0] = 0
RuntimeWarning: invalid value encountered in less

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 67
    relu[i-1][relu[i-1] > 0] = 1
RuntimeWarning: invalid value encountered in greater
epoch 0 loss: nan
epoch 0 time: 20.441817045211792
epoch 1 loss: nan
epoch 1 time: 19.98494791984558
epoch 2 loss: nan
epoch 2 time: 19.527820110321045
epoch 3 loss: nan
epoch 3 time: 19.766153812408447
epoch 4 loss: nan
epoch 4 time: 19.77734398841858

===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 42
    scores[scores < 0] = 0
RuntimeWarning: invalid value encountered in less

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 50
    final_grad[final_grad < 0] = 0
RuntimeWarning: invalid value encountered in less

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 53
    final_grad[final_grad > 0] = 1
RuntimeWarning: invalid value encountered in greater

Warning (from warnings module):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 67
    relu[i-1][relu[i-1] > 0] = 1
RuntimeWarning: invalid value encountered in greater

===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 8.999431111111111
epoch 0 time: 19.270107984542847
epoch 1 loss: 8.985972622222217
epoch 1 time: 19.07401394844055
epoch 2 loss: 8.972917888000001
epoch 2 time: 19.136831998825073
epoch 3 loss: 8.960254795804447
epoch 3 time: 19.111626863479614

===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 1.8172257687567919
epoch 0 time: 19.77990698814392
epoch 1 loss: 0.3235134135712788
epoch 1 time: 20.083651781082153
epoch 2 loss: 0.10464112210900833
epoch 2 time: 19.827780961990356
epoch 3 loss: 0.04569308478209584
epoch 3 time: 19.507355213165283
epoch 4 loss: 0.024448395518967093
epoch 4 time: 19.385459184646606
epoch 5 loss: 0.010951427913687499
epoch 5 time: 19.34713912010193
epoch 6 loss: 0.009975437674521935
epoch 6 time: 19.424405813217163
epoch 7 loss: 0.003886022037263984
epoch 7 time: 19.39398193359375
epoch 8 loss: 0.002293269509931334
epoch 8 time: 19.291350841522217
epoch 9 loss: 0.0013415060762382571
epoch 9 time: 19.389384984970093
training accuracy: 1.0
test accuracy: 0.93
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 235, in <module>
    print(net(x, x_conv, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True))
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 199, in net
    test_examples(w, b, x_test, y_test)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 110, in test_examples
    redraw(x[r], predict(w, b, x[r]), screen)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 102, in redraw
    pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
IndexError: index 676 is out of bounds for axis 0 with size 676
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 1.6845885204785243
epoch 0 time: 20.322509050369263
epoch 1 loss: 0.2892846853000017
epoch 1 time: 20.09763813018799
epoch 2 loss: 0.0951627917965636
epoch 2 time: 19.996581077575684
epoch 3 loss: 0.03387811458377389
epoch 3 time: 19.97623109817505
epoch 4 loss: 0.013223066193349375
epoch 4 time: 20.31117010116577
epoch 5 loss: 0.006484577917306004
epoch 5 time: 19.934569835662842
epoch 6 loss: 0.0025532036535061303
epoch 6 time: 19.927276849746704
epoch 7 loss: 0.00148162266796863
epoch 7 time: 19.90648889541626
epoch 8 loss: 0.0005518156720800525
epoch 8 time: 19.902462005615234
epoch 9 loss: 0.0009620469447149635
epoch 9 time: 19.929391145706177
training accuracy: 1.0
test accuracy: 0.916

===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 2.844013310209954
epoch 0 time: 19.58306384086609
epoch 1 loss: 0.17271044548847558
epoch 1 time: 19.308884859085083
epoch 2 loss: 0.028623040743283253
epoch 2 time: 19.21108078956604
epoch 3 loss: 0.001367199948397854
epoch 3 time: 19.329790830612183
epoch 4 loss: 0.0015268718832820766
epoch 4 time: 19.291523933410645
epoch 5 loss: 0.0007699642318609016
epoch 5 time: 19.590265035629272
epoch 6 loss: 0.0
epoch 6 time: 19.649595022201538
epoch 7 loss: 0.0
epoch 7 time: 19.28550887107849
epoch 8 loss: 0.0
epoch 8 time: 19.21392297744751
epoch 9 loss: 0.0
epoch 9 time: 19.267940044403076
training accuracy: 1.0
test accuracy: 0.89
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 235, in <module>
    margin = 0
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 199, in net
    test_examples(w, b, x_test, y_test)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 110, in test_examples
    redraw(x[r], predict(w, b, x[r]), screen)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 102, in redraw
    pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
TypeError: invalid color argument
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 2000
training size: 1500
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 2.7303715244229356
epoch 0 time: 20.03201389312744
epoch 1 loss: 0.2871732100021142
epoch 1 time: 21.611845016479492
epoch 2 loss: 0.05328749375607411
epoch 2 time: 21.376753091812134
epoch 3 loss: 0.018275919515435057
epoch 3 time: 19.809391021728516
epoch 4 loss: 0.007132929619591191
epoch 4 time: 19.287471055984497
epoch 5 loss: 0.004962915409131264
epoch 5 time: 19.312310934066772
epoch 6 loss: 0.002767119262441327
epoch 6 time: 19.19108486175537
epoch 7 loss: 0.0005239393256997585
epoch 7 time: 19.232244968414307
epoch 8 loss: 0.0007836078895085108
epoch 8 time: 19.317646026611328
epoch 9 loss: 0.0003138859960653105
epoch 9 time: 19.226404905319214
training accuracy: 1.0
test accuracy: 0.886
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 237, in <module>
    print(net(x, x_conv, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True))
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 199, in net
    test_examples(w, b, x_test, y_test)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 110, in test_examples
    redraw(x[r], predict(w, b, x[r]), screen)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 102, in redraw
    pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
TypeError: invalid color argument
>>> 
===== RESTART: /Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py =====
hardwired convolution deep layer fully connected relu activation
data size: 6000
training size: 5000
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 1.3270030577413672
epoch 0 time: 64.6942720413208
epoch 1 loss: 0.19446477227156217
epoch 1 time: 63.50932192802429
epoch 2 loss: 0.06357037533910058
epoch 2 time: 63.03464889526367
epoch 3 loss: 0.02165901778117124
epoch 3 time: 63.79129195213318
epoch 4 loss: 0.01284797145583457
epoch 4 time: 63.122859954833984
epoch 5 loss: 0.004901305769152295
epoch 5 time: 63.790265798568726
epoch 6 loss: 0.0031322712725509344
epoch 6 time: 63.425987005233765
epoch 7 loss: 0.0016733420265029816
epoch 7 time: 63.4436559677124
epoch 8 loss: 0.0013669256039686047
epoch 8 time: 63.53889298439026
epoch 9 loss: 0.0006200402893642562
epoch 9 time: 63.212316036224365
training accuracy: 0.9998
test accuracy: 0.929
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 237, in <module>
    print(net(x, x_conv, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True))
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 199, in net
    test_examples(w, b, x_test, y_test)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 110, in test_examples
    redraw(x[r], predict(w, b, x[r]), screen)
  File "/Users/Finn/Documents/MNIST/mnisthardwiredconvolution.py", line 102, in redraw
    pygame.draw.rect(screen, (255-x[i], 255-x[i], 255-x[i]), [10*(i%28), 10*int(i/28), 10, 10], 0)
TypeError: invalid color argument
>>> a = 1
>>> print(a+)
SyntaxError: invalid syntax
>>> print(a+1)
2
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 9.869350498248302
epoch 0 time: 0.9061481952667236
epoch 1 loss: 2.794767499620779
epoch 1 time: 0.7499511241912842
epoch 2 loss: 0.14588664315768976
epoch 2 time: 0.7508611679077148
epoch 3 loss: 0.021382331302070002
epoch 3 time: 0.7496187686920166
epoch 4 loss: 0.0
epoch 4 time: 0.7500200271606445
epoch 5 loss: 0.0
epoch 5 time: 0.74969482421875
epoch 6 loss: 0.0
epoch 6 time: 0.7496440410614014
epoch 7 loss: 0.0
epoch 7 time: 0.748272180557251
epoch 8 loss: 0.0
epoch 8 time: 0.7490010261535645
epoch 9 loss: 0.0
epoch 9 time: 0.750452995300293
training accuracy: 1.0
test accuracy: 0.6666666666666666

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [2]
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 9.109773049627924
epoch 0 time: 0.16631507873535156
epoch 1 loss: 8.824899131714313
epoch 1 time: 0.16644787788391113
epoch 2 loss: 10.086676373356395
epoch 2 time: 0.1492929458618164
epoch 3 loss: 8.790074620953936
epoch 3 time: 0.16615509986877441
epoch 4 loss: 8.767597391951128
epoch 4 time: 0.14710211753845215
training accuracy: 0.2
test accuracy: 0.0

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 9027.495592734742
epoch 0 time: 0.16623902320861816
epoch 1 loss: 633.3847006270908
epoch 1 time: 0.1663651466369629
epoch 2 loss: 2.9961911371564436
epoch 2 time: 0.1492919921875
epoch 3 loss: 0.0
epoch 3 time: 0.16685009002685547
epoch 4 loss: 0.0
epoch 4 time: 0.167449951171875
training accuracy: 1.0
test accuracy: 0.5333333333333333

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 11505.779644471657
epoch 0 time: 0.16678690910339355
epoch 1 loss: 1596.4702917442748
epoch 1 time: 0.1513538360595703
epoch 2 loss: 6.164062953125833
epoch 2 time: 0.14995789527893066
epoch 3 loss: 0.0
epoch 3 time: 0.14971685409545898
epoch 4 loss: 0.0
epoch 4 time: 0.14849495887756348
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 242, in <module>
    print(net(x, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True, save=True))
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 195, in net
    saveNet(layers, w, b)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 206, in saveNet
    read = open("number.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'number.txt'
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 7202.658792380021
epoch 0 time: 0.164963960647583
epoch 1 loss: 929.9317327440641
epoch 1 time: 0.14982295036315918
epoch 2 loss: 197.59074910567688
epoch 2 time: 0.1511220932006836
epoch 3 loss: 0.0
epoch 3 time: 0.16509795188903809
epoch 4 loss: 0.0
epoch 4 time: 0.15355300903320312
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 242, in <module>
    print(net(x, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True, save=True))
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 195, in net
    saveNet(layers, w, b)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 211, in saveNet
    write.write(int(n)+1)
TypeError: write() argument must be str, not int
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 6066.114794042908
epoch 0 time: 0.16237616539001465
epoch 1 loss: 656.0365752883017
epoch 1 time: 0.14846515655517578
epoch 2 loss: 33.44213386389726
epoch 2 time: 0.1499490737915039
epoch 3 loss: 0.0
epoch 3 time: 0.16642308235168457
epoch 4 loss: 0.0
epoch 4 time: 0.1678779125213623
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 242, in <module>
    print(net(x, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True, save=True))
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 195, in net
    saveNet(layers, w, b)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 211, in saveNet
    write.write(str(int(n)+1))
UnboundLocalError: local variable 'n' referenced before assignment
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 9297.838891653477
epoch 0 time: 0.16533803939819336
epoch 1 loss: 1288.000495583917
epoch 1 time: 0.16571593284606934
epoch 2 loss: 0.0
epoch 2 time: 0.15011906623840332
epoch 3 loss: 0.0
epoch 3 time: 0.1656038761138916
epoch 4 loss: 0.0
epoch 4 time: 0.16606497764587402
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 242, in <module>
    print(net(x, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True, save=True))
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 195, in net
    saveNet(layers, w, b)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 215, in saveNet
    new.write(layer)
TypeError: write() argument must be str, not int
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 10872.787143972453
epoch 0 time: 0.16704010963439941
epoch 1 loss: 985.3916873816719
epoch 1 time: 0.16587400436401367
epoch 2 loss: 3.487697527662496
epoch 2 time: 0.1498560905456543
epoch 3 loss: 4.88307615767915
epoch 3 time: 0.16648507118225098
epoch 4 loss: 0.0
epoch 4 time: 0.1667320728302002
[-0.01448871  0.000359   -0.0038891   0.00099478  0.03026267  0.00894485
  0.00531277  0.00543829  0.00443051 -0.00291995]
[ 0.01290027  0.00877635  0.00193761  0.01805457 -0.00231693 -0.01401418
  0.01425389  0.01668856 -0.0103693   0.0104631 ]
[-0.01485767  0.01068928 -0.00917811 -0.01582562  0.00087901  0.01608746
 -0.00420318  0.00496832  0.00284426 -0.01051593]
[-0.00198864 -0.00714508  0.00209951  0.01099296 -0.00161887  0.00816189
  0.00809359  0.01078516  0.00878003  0.00427801]
[-0.0002546   0.01898753 -0.00397394 -0.00897577 -0.0038994   0.00252043
 -0.0053188  -0.00531886 -0.00343212 -0.00672046]
[ 0.00199672 -0.00987686 -0.00154424 -0.0086779  -0.0068759   0.00313973
 -0.00429805 -0.0222524  -0.0102004   0.00054426]
[ 0.02565634 -0.01230669 -0.01255401 -0.01051902  0.00896044  0.02134732
 -0.00728214 -0.00268266  0.01988353 -0.01480682]
[-0.00263445  0.01599171  0.00939552 -0.00796273 -0.02090917 -0.01167915
 -0.00096797 -0.01131702 -0.00076529  0.00611814]
[-0.02839452  0.00822378  0.00526918  0.00603194  0.0129002  -0.00608364
 -0.00686511 -0.0081102  -0.00144782  0.0028264 ]
[-0.00922565 -0.00459729  0.00666821  0.0138302  -0.00087131 -0.00806061
 -0.01040173  0.00147254 -0.01337967 -0.00116799]
[ 0.00150674  0.00555114  0.00047665 -0.006461    0.01046566  0.01421441
 -0.00861182  0.01634491 -0.0108219  -0.00628291]
[ 0.00302705  0.0097772   0.02136791  0.00357109 -0.00379281 -0.00092794
  0.01134263  0.01824105  0.00276663  0.00694873]
[ 0.00156217  0.00855854  0.00101261  0.01122446  0.00302923  0.00519851
  0.0005232   0.00167411 -0.01715019 -0.0018853 ]
[ 5.10848958e-04 -9.95416154e-03  1.01919938e-02 -6.46934421e-05
 -1.75424108e-02  6.90516275e-03 -6.42554739e-04  1.01188690e-02
  1.23091989e-03  8.02702184e-04]
[ 0.01259087 -0.01163044  0.00394357 -0.00611472 -0.00556626  0.00624698
 -0.00749962 -0.00126195 -0.00680585  0.00311535]
[-0.01290429 -0.01917766  0.00852075 -0.01756332  0.00419098  0.00218332
 -0.00042242  0.00584929 -0.01755882 -0.01229609]
[-0.01124369 -0.01426142 -0.00981029  0.00508016  0.01171547  0.00032439
  0.00846172 -0.00383349 -0.01380658  0.01262135]
[ 1.26882803e-02  6.74379811e-03 -6.98941520e-03  7.39555478e-03
  3.30869356e-03 -1.04573767e-02  5.00652185e-05  1.03031742e-05
  1.17068217e-02 -2.98167215e-03]
[-1.47944977e-02  1.79909027e-02 -4.99438966e-05  4.69458054e-03
 -5.51567767e-03  1.23214795e-02 -7.54294260e-03  7.98077572e-03
  1.42309268e-02  1.89729277e-02]
[-0.00057226  0.00239454 -0.01038294  0.01318937  0.00351405 -0.00193162
  0.00996658  0.00804774 -0.00357163 -0.01054412]
[-5.06848680e-03  7.09920958e-03  6.95639348e-04 -3.32486685e-05
  1.42909099e-03 -2.74305169e-03 -5.87597106e-03 -6.57694943e-03
 -8.23879396e-03 -7.78562808e-03]
[-0.00301482 -0.01866188 -0.00201688  0.01330896  0.00888096 -0.00387627
 -0.00193124  0.01492805 -0.02199825  0.02041367]
[-0.00437111  0.01709467  0.00014663 -0.00519662 -0.00185993 -0.00282928
 -0.00213009  0.01723768  0.01235191 -0.0141772 ]
[ 0.00274657 -0.00500584 -0.00366333  0.00345058  0.00640357 -0.00682908
 -0.00858515  0.00455087  0.00961763 -0.00203424]
[ 0.00098282  0.00738782 -0.00361342 -0.00013843  0.00291975  0.00654506
  0.00070425 -0.02313182  0.01228    -0.00589   ]
[-8.14317179e-04 -1.21187806e-02 -8.94114409e-03 -1.34541304e-02
  6.38758644e-03 -4.19990421e-03 -3.23158603e-05 -1.22669125e-02
  1.99547220e-02 -8.13810543e-03]
[ 0.01377401 -0.00488651 -0.00381778 -0.00472871  0.00366837 -0.01113918
  0.00072309  0.00921172  0.0007047   0.01085133]
[ 0.01101664 -0.01293029 -0.01482885  0.011693   -0.01032063  0.0032921
  0.00725584  0.0019594   0.00030866 -0.00713907]
[-0.00818344  0.00742923  0.0136685   0.01140032 -0.0109815   0.00743475
 -0.00667355 -0.00237924  0.01238313 -0.00710807]
[-0.00717482  0.01860594  0.00169993 -0.01026985 -0.01603399  0.00670536
  0.00055963  0.00054361 -0.01164531 -0.01673021]
[ 0.00945773 -0.00071582  0.00287586 -0.00134294 -0.00305812 -0.01090059
 -0.01479296  0.00912898  0.02050544 -0.00886672]
[-0.00728751  0.00050363 -0.01091459  0.007419   -0.00139885 -0.01064015
 -0.0024465  -0.0036007  -0.00102969 -0.00295913]
[-0.00452158 -0.00360572  0.02626072  0.00772689 -0.00201264  0.01922113
  0.00791755 -0.00609762  0.01557704  0.00917477]
[ 0.00721809 -0.0048553  -0.01785567 -0.0058026   0.0134086  -0.01715197
 -0.00222574  0.00912757 -0.01957073  0.00562958]
[ 0.00896108 -0.01481813  0.01608063 -0.01257492 -0.01534496  0.00507045
 -0.01812006  0.00020098  0.00983809 -0.0353672 ]
[-0.00210875 -0.00141538  0.00956518 -0.00978875  0.00089236 -0.0109803
 -0.03617915 -0.00458833  0.00371544 -0.02024315]
[-0.0086396   0.01742743 -0.00607887  0.01040972  0.01116428  0.0041283
  0.00333218 -0.02208519 -0.0016693  -0.00067838]
[-0.00445336  0.00736259 -0.01053815  0.00243656 -0.00788323 -0.00595403
 -0.00076495 -0.0058471  -0.00152153  0.01106918]
[ 0.01286136 -0.0208689  -0.00037658  0.00936515 -0.00424964  0.0147747
 -0.00640241  0.00183431 -0.01927373 -0.00950029]
[ 0.00060741 -0.00737201  0.0082678   0.00823993  0.00613501 -0.0035151
  0.01208957  0.00956298  0.00406541 -0.00022781]
[-0.01005148  0.00696783 -0.01111572 -0.0133107  -0.00157194 -0.00243805
 -0.00875127  0.00509233 -0.00294444 -0.00766606]
[ 0.00026752  0.01086717 -0.00083017 -0.0105766  -0.01170752 -0.02088586
  0.00792138  0.00687054  0.00622925  0.01730261]
[-0.00600255  0.00148381  0.01602454 -0.0052041  -0.00114983 -0.00096687
  0.00146314  0.02199094  0.00438839  0.00426285]
[-0.01896295  0.00138885 -0.01316405  0.00473692  0.00388299  0.0064439
 -0.02009399  0.00448172  0.01513739  0.00210743]
[ 0.010485    0.01046125  0.01400944 -0.01623658  0.00521228  0.0104788
 -0.00216358 -0.00489258  0.00695072  0.00820943]
[ 0.0221166  -0.0007921  -0.02077099 -0.02313488 -0.00672588 -0.0005138
  0.01505557 -0.00600808  0.00085412 -0.00058687]
[-2.84131349e-03 -7.93873766e-03 -1.65603968e-02 -7.96830443e-03
 -9.71106194e-03  2.16264913e-02 -5.86999178e-05 -1.61476757e-02
  5.68082943e-03 -1.58735035e-02]
[-0.00322789 -0.00131395  0.00088245 -0.01259623  0.01423412 -0.00702831
 -0.0090045   0.0077622  -0.00426446 -0.00104949]
[ 0.00010514 -0.00787702 -0.01367456 -0.00010113 -0.00056394 -0.00999373
 -0.00062642  0.00450115 -0.01995221 -0.00578937]
[-0.00924433 -0.00174428 -0.00355715 -0.00353553  0.03204894  0.00880755
 -0.0036372  -0.00202909  0.01041883  0.00077682]
[ 0.00359526 -0.00832828  0.00645325 -0.01024941 -0.00197735  0.00974309
 -0.01767451  0.00541001  0.00906961  0.01536286]
[ 0.00480124  0.01538859  0.00696983  0.00211594 -0.00745417  0.01317878
  0.0170648  -0.00012713 -0.01422041  0.00917362]
[ 0.00492179  0.00755819  0.0193563  -0.00123911  0.01631043 -0.0041365
 -0.00059591  0.00627461  0.00618107 -0.00197662]
[-0.00984259 -0.00400511 -0.02666791  0.0225532  -0.00213051 -0.00365416
 -0.01327162  0.01394106 -0.00579711 -0.00609541]
[-0.00739614  0.00166974  0.01473692  0.00263158  0.00234071 -0.00289126
  0.00981249 -0.00985943  0.01232637  0.00906257]
[ 0.02356795 -0.00800769 -0.01679893 -0.00042465 -0.01283794 -0.00780673
 -0.01247117 -0.00546841  0.01335629 -0.00205816]
[-0.00125891 -0.00736396  0.00705151 -0.00821898 -0.00967284 -0.01110609
  0.00311149 -0.00616809 -0.00970849 -0.0026981 ]
[ 0.01030966  0.00592516  0.00263532  0.00209944  0.00816153 -0.0046642
 -0.00033253 -0.00622988 -0.01067341 -0.0060023 ]
[ 2.31480402e-02 -5.96948277e-03 -9.04853266e-03 -1.08903071e-03
  8.57516851e-03 -5.53184988e-05  5.39029418e-03  1.05078659e-02
 -9.62985670e-04 -2.13416876e-03]
[-0.01470345 -0.00926057  0.00293449 -0.00342196  0.01141643  0.01148953
  0.0004646   0.00513784  0.01303944 -0.00430674]
[-0.00021528 -0.00198675  0.00894888  0.0069347   0.01179257  0.01379611
  0.00464895  0.00686667 -0.02399574 -0.00596744]
[ 0.01133436 -0.0052957  -0.00413949 -0.0227712  -0.02049699  0.00791334
  0.00662197 -0.01606915  0.01259431 -0.01797366]
[-0.00781865  0.00264508  0.00761821 -0.00920621  0.00521053  0.0111748
 -0.01677934  0.00026139  0.00341616 -0.00742545]
[-0.00605283  0.00182605 -0.00167521  0.01092701 -0.00908561  0.00296768
  0.01413254  0.01067305 -0.01117178 -0.00235768]
[-0.00919502 -0.00122644  0.01122703 -0.0120956   0.01042967 -0.0070965
  0.00354901  0.00158999  0.00476559  0.00888219]
[ 0.00118066  0.00972076  0.00965354  0.00091656  0.00396393 -0.00165622
  0.00725907  0.00823875 -0.00033959  0.00022184]
[ 0.01401396 -0.01154653 -0.01059196  0.00255855  0.00319758 -0.00145865
  0.00197724  0.00941423 -0.00288225 -0.00073176]
[-0.00492435 -0.00848585  0.00412824 -0.00162307 -0.00694102  0.00991948
  0.00495283 -0.00414879 -0.01078579  0.01007104]
[-0.00196778  0.00493792  0.00841873  0.00670124  0.00171394  0.02467364
 -0.00402265  0.00219939 -0.00755652  0.00286721]
[ 1.20449871e-03 -1.28161628e-03 -1.50064010e-02 -2.60281666e-03
  8.90805825e-03  3.35523972e-05  7.82867763e-03 -1.96577920e-03
 -5.07572577e-04 -2.26585237e-04]
[ 0.00780514 -0.00985417  0.00607191 -0.0075297   0.00538686  0.00052004
 -0.00949902  0.00805121  0.01382162 -0.00046843]
[-0.00147052 -0.0094199  -0.00993    -0.01059385 -0.00535787 -0.0063932
 -0.0109246  -0.01462885  0.01554396 -0.00459141]
[-0.03320232 -0.02143973 -0.00348007 -0.02202047 -0.00077076 -0.04148303
  0.16879956 -0.02127929 -0.02279908 -0.00790012]
[-0.05602146 -0.03655749 -0.02925722 -0.04186933 -0.03421609 -0.05535679
  0.33371166 -0.03764402 -0.04566117 -0.06432328]
[-0.06964548 -0.04245552 -0.06546466 -0.05378667 -0.07387598 -0.07229602
  0.53416043 -0.06096159 -0.06167239 -0.07385633]
[-0.03035125 -0.02893716 -0.02846353 -0.02845102 -0.02495133 -0.04044988
  0.27755362 -0.03001306 -0.01241681 -0.02013292]
[-0.00592379 -0.01844687  0.00354487  0.00460144  0.01118459 -0.00169115
 -0.00192247  0.01340623 -0.00214454  0.0116431 ]
[ 0.0008872  -0.00768055  0.00215073 -0.00720681  0.00366777  0.00739437
 -0.01274529  0.00496167  0.017792    0.00607237]
[ 0.01824798 -0.00761347  0.01954831 -0.00218473  0.01350004  0.01133051
 -0.00062745  0.00059214 -0.00247672  0.00462667]
[-0.00791354  0.01578711 -0.00725049 -0.02043623  0.00225527 -0.0027083
  0.01269477  0.00600677  0.00288476  0.00388929]
[ 0.00044095  0.01406416 -0.01271575  0.00573531  0.00103636  0.00869565
 -0.00583357 -0.00629241 -0.01071585  0.00062973]
[ 0.00444325  0.01352239 -0.00240945 -0.00375996 -0.00039301 -0.00790776
  0.00076485  0.01862456  0.00759781 -0.00399087]
[ 0.00041389  0.01797871  0.02164587  0.0216275   0.00207772  0.01339002
  0.00377273  0.01265104 -0.00466178  0.00074878]
[ 0.00041034 -0.00538451 -0.01415455  0.02442417 -0.00307053 -0.0091717
 -0.01074797 -0.00280142 -0.0085704  -0.00315692]
[-0.0064143   0.00630772 -0.00641886 -0.00368699 -0.00373999  0.00039266
  0.00941792 -0.00110973  0.00447588 -0.00274335]
[ 0.00917081 -0.00652533  0.00319487  0.00519023  0.00013526 -0.00098413
  0.01188535  0.00902635  0.00394295  0.00067871]
[-0.00364391  0.00182627 -0.01250145  0.00894441  0.00496239 -0.00086212
  0.00902762  0.00896661 -0.00866242 -0.00690891]
[ 5.44370508e-05  2.65453002e-03  3.69488648e-03  6.12313829e-03
 -1.40867294e-02  5.65243792e-03  1.17913266e-02 -1.11761138e-02
 -1.24741206e-02 -5.03507406e-04]
[ 0.01256996 -0.0038709   0.000739    0.01309672 -0.0041414   0.01208303
 -0.00244213 -0.0019326  -0.0098406  -0.01189659]
[ 0.0168505   0.00128752  0.01134275 -0.01692043  0.00886345 -0.0176389
 -0.01482401  0.0064788   0.01248713 -0.01563795]
[-0.00054387  0.00553692 -0.00682928 -0.00039411  0.00674805  0.01524404
  0.0152345  -0.03109125  0.00123552  0.00726296]
[ 0.00938121 -0.0157193   0.0088745   0.00824036  0.00685914  0.00014993
  0.00862947 -0.00372582  0.0220307  -0.02363678]
[ 0.01446596  0.0015835   0.00593472  0.0091244   0.00217516  0.00255344
 -0.01711313 -0.01257896  0.00650052  0.0023746 ]
[-0.01109969  0.01045066 -0.00101282 -0.00109252 -0.00774688  0.0068188
  0.00729866 -0.00151477 -0.00468082 -0.0002528 ]
[ 0.0055211  -0.00415243  0.00470204  0.00481707  0.00886838 -0.01432356
 -0.01660531 -0.00066967 -0.02368833  0.01530469]
[-0.01214307 -0.0094371   0.00315499 -0.00819494  0.01322628 -0.0122471
  0.00942583  0.01489268 -0.00345277 -0.00069126]
[ 0.01692402 -0.01113985 -0.00186777 -0.00295583 -0.00372273 -0.0107989
 -0.01120252 -0.01926231 -0.00591157 -0.00755048]
[ 0.00494272  0.0269589   0.00976363 -0.00252003 -0.00451575 -0.00965246
 -0.00874862  0.00052015 -0.01351925  0.00910296]
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 242, in <module>
    print(net(x, y, train_size, batch_size, rate, decay, norm, layers, epochs, w_init, margin, display=True, timing=True, save=True))
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 195, in net
    saveNet(layers, w, b)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 218, in saveNet
    print(str(www))
  File "/usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/lib/python3.5/idlelib/PyShell.py", line 1344, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 11118.054925740928
epoch 0 time: 0.16549015045166016
epoch 1 loss: 1406.1587361364088
epoch 1 time: 0.16656494140625
epoch 2 loss: 84.51772083527621
epoch 2 time: 0.15003204345703125
epoch 3 loss: 40.35628374052158
epoch 3 time: 0.16828203201293945
epoch 4 loss: 10.528448077985276
epoch 4 time: 0.16682100296020508
training accuracy: 0.9777777777777777
test accuracy: 0.5333333333333333

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 10750.558527125826
epoch 0 time: 0.16615986824035645
epoch 1 loss: 3295.85515778039
epoch 1 time: 0.16800904273986816
epoch 2 loss: 48.36403901552984
epoch 2 time: 0.1501929759979248
epoch 3 loss: 0.0
epoch 3 time: 0.16684412956237793
epoch 4 loss: 0.0
epoch 4 time: 0.16670012474060059
training accuracy: 1.0
test accuracy: 0.6

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 6188.802841503305
epoch 0 time: 0.16608619689941406
epoch 1 loss: 826.3375552718885
epoch 1 time: 0.1668260097503662
epoch 2 loss: 57.46897228277506
epoch 2 time: 0.1501150131225586
epoch 3 loss: 0.0
epoch 3 time: 0.16641497611999512
epoch 4 loss: 0.0
epoch 4 time: 0.16637921333312988
training accuracy: 1.0
test accuracy: 0.4666666666666667

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 7643.196953994892
epoch 0 time: 0.15077900886535645
epoch 1 loss: 829.703585506827
epoch 1 time: 0.15119504928588867
epoch 2 loss: 54.61313169757381
epoch 2 time: 0.15044188499450684
epoch 3 loss: 0.0
epoch 3 time: 0.16649508476257324
epoch 4 loss: 0.0
epoch 4 time: 0.15032386779785156
training accuracy: 1.0
test accuracy: 0.6

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60
training size: 45
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: []
epochs: 5
weight initialization: 0.01
loss margin: 0
epoch 0 loss: 6476.702378958352
epoch 0 time: 0.14697694778442383
epoch 1 loss: 638.4403817329531
epoch 1 time: 0.14895296096801758
epoch 2 loss: 0.0
epoch 2 time: 0.14922094345092773
epoch 3 loss: 0.0
epoch 3 time: 0.14996886253356934
epoch 4 loss: 0.0
epoch 4 time: 0.15122485160827637
training accuracy: 1.0
test accuracy: 0.7333333333333333

=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
Traceback (most recent call last):
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 231, in <module>
    x, y = data(size)
  File "/Users/Finn/Documents/MNIST/mnistdeeprelu.py", line 29, in data
    x[i], yn = convert(line[:-1])
KeyboardInterrupt
>>> 
=========== RESTART: /Users/Finn/Documents/MNIST/mnistdeeprelu.py ===========
deep layer fully connected relu activation
data size: 60000
training size: 50000
batch size: 15
learning rate: 0.002
learning rate decay: 0.97
decay normalization: 1
hidden layers: [1000, 1000, 1000]
epochs: 10
weight initialization: 0.01
loss margin: 0
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 0 loss: 0.2935781033053388
epoch 0 time: 670.5168170928955
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 1 loss: 0.08021518059490945
epoch 1 time: 744.0328130722046
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 2 loss: 0.039845061681858814
epoch 2 time: 692.745414018631
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 3 loss: 0.02234993026428572
epoch 3 time: 759.1590611934662
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 4 loss: 0.013462175589988702
epoch 4 time: 833.9889841079712
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 5 loss: 0.008977227645787823
epoch 5 time: 763.3470058441162
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 6 loss: 0.005622584594788901
epoch 6 time: 669.2766780853271
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 7 loss: 0.0043818597065867024
epoch 7 time: 619.1757681369781
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 8 loss: 0.002580434966323565
epoch 8 time: 618.8159070014954
batch 0
batch 300
batch 600
batch 900
batch 1200
batch 1500
batch 1800
batch 2100
batch 2400
batch 2700
batch 3000
batch 3300
epoch 9 loss: 0.0021649271547654757
epoch 9 time: 619.4732229709625
training accuracy: 0.9994
test accuracy: 0.9804
