#!/usr/bin/python
# encoding: utf-8

'''
Using the tensorflow library to create a neural network with 3 nodes. The third node
is using for accept add of the second e first nodes.
'''

import tensorflow as tf

# Declaring two inputs for nodes
# The placeholer is for external date...
inputA = tf.placeholder(dtype=tf.float32) 
inputB = tf.placeholder(dtype=tf.float32)
 
# Creating two nodes, this nodes will be the add of inputA and inputB...
Node1 = tf.add(inputA,inputB)
Node2 = tf.add(inputA,inputB)

# Creting two weights for input of Node3 with constants method...
weight1 = tf.constant(3.0,dtype=tf.float32)
weight2 = tf.constant(3.7,dtype=tf.float32)
 
# Creating one node, this node accept the result of the nodes (Node1 and Node2) and
# the inputs are added to weights ()
Node3 = tf.add(Node1*weight1,Node2*weight2)
 
# Need Session for compile and run the method...
sess = tf.Session()
 
# Execute the test... 
result = sess.run(Node3,{inputA:8,inputB:9})

# Print the result...
print("Result: " + str(result))