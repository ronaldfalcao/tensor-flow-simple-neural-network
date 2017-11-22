#!/usr/bin/python
# encoding: utf-8

'''
Using the tensorflow library for to create a simple node, the node is a component
of the neural networks
'''

import tensorflow as tf

# Declaring two inputs for the node
# The placeholer is for external date...
x1 = tf.placeholder(dtype=tf.float32)
x2 = tf.placeholder(dtype=tf.float32)
 
# Output for the node, a simple add (x1 + x2)
output = tf.add(x1,x2)
 
# Need Session for compile and run the method...
sess = tf.Session()

# Execute the test, using a dic for this...
result = sess.run(output,{x1:1,x2:2})

# Print the result...
print("Result: " + str(result))