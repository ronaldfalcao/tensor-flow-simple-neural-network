#!/usr/bin/python
# encoding: utf-8

'''
Simple test with vectors using tensorflow library
'''

import tensorflow as tf

# Creating two vetors...
vector1 = tf.constant([2.0,3.0,7.0],dtype=tf.float32)
vector2 = tf.constant([5.0,2.0,6.0],dtype=tf.float32)

# First using the tensorflow's multply() method for multiply element by element
# of arrays... 
multiply_array = tf.multiply(vector1,vector2)
 
# Secondly using the tensorflow method for add array elements...
sum_array_elements = tf.reduce_sum(multiply_array)
 
# Finaly, using a tradicional method for add the vetors
sum_vectors = vector1 + vector2
 
# Need Session for compile and run the method...
sess = tf.Session()

# Print the results...
print("Array Multiply for tensorflow method: ")
print(sess.run(multiply_array))

print("\nArray add tradicional method: ")
print(sess.run(sum_vectors))

print("\nArray sum of array elements: ")
print(sess.run(sum_array_elements))
