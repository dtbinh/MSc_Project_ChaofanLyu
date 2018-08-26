import tensorflow as tf
import numpy as np
import pandas as pd

def load_graph(frozen_graph_filename):
    # We load the protobuf file from the disk and parse it to retrieve the 
    # unserialized graph_def
    with tf.gfile.GFile(frozen_graph_filename, "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # Then, we import the graph_def into a new Graph and returns it 
    with tf.Graph().as_default() as graph:
        # The name var will prefix every op/nodes in your graph
        # Since we load everything in a new graph, this is not needed
        tf.import_graph_def(graph_def, name="prefix")
    return graph

if __name__=='__main__':
    set_train = pd.read_csv('Input_train.csv').values
    set_test  = pd.read_csv('Input_test.csv').values

    x_train = set_train[:,0:21]
    y_train = set_train[:,21:25]
    x_test  = set_test[:,0:21]
    y_test  = set_test[:,21:25]

    graph = load_graph('./Model/frozen_model.pb')
    for op in graph.get_operations():
        print(op.name)
    x = graph.get_tensor_by_name('prefix/placeholder/x_inputs:0')
    y = graph.get_tensor_by_name('prefix/output_layer/y_output:0')

    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.33)
    sess_config = tf.ConfigProto(gpu_options=gpu_options)
    with tf.Session(graph=graph, config=sess_config) as sess :
        ret = sess.run(y, feed_dict={x:x_test[100].reshape(1,21)})
        print(ret)
        print(y_test[100])