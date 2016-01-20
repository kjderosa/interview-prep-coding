__author__ = 'Kyle DeRosa'

# Arrays are similar to lists, but all items must be of the same primitive type.

'''
https://docs.python.org/3/library/array.html
Type code	C Type  	        Python Type	        Minimum size in bytes   (combinatorics)
'b'	        signed char	        int	                1                       pow(2,1*8) = 128
'B'	        unsigned char	    int	                1
'u' 	    Py_UNICODE	        Unicode character	2                       pow(2,2*8) = 65536
'h'	        signed short	    int	                2
'H'	        unsigned short	    int	                2
'i'	        signed int	        int	                2
'I'	        unsigned int	    int	                2
'l'	        signed long	        int	                4                       pow(2,4*8) = 4294967296
'L'	        unsigned long	    int	                4
'q'	        signed long long    int	                8                       pow(2,8*8) = 18446744073709551616
'Q'	        unsigned long long	int	                8
'f'	        float	            float	            4
'd'	        double	            float	            8
'''
from array import array

b = array('b', range(0, 63))  # 0-127
B = array('B')
u = array('u')
h = array('h')
H = array('H')
i = array('i')
I = array('I')
l = array('l')
L = array('L')
q = array('q')
Q = array('Q')
f = array('f')
d = array('d')


# return typecode of the array
typecode = b.typecode

# return itemsize of the array
itemsize = b.itemsize

# append new values
b.append(127)

# returns memory address and length (# of elements) used to hold contents
# "The size of the memory buffer (in bytes) can be computed as
#   array.buffer_info()[1] * array.itemsize"
b.buffer_info()
buffersize = b.buffer_info()[1] * b.itemsize

# “Byteswap” all items of the array. useful when reading data from a file written
#   on a machine with different byte order
b.byteswap()

# count of occurances of x
b.count(42)

# appends items from the string
b.fromstring('test')

# Big O test
# insert (worst case, n+1); insert into 0-th index, and increment each ith value to i+1
# delete (worst case, n+1); delete from 0-th index, and decrement each ith value to i-1
# search (worst case, n); look at each value
# sorted search (worst case, log-n); binary search
# sort (n lg n), merge sort


# space
# n elements
