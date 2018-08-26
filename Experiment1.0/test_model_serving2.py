import tensorflow as tf
from model_load import load_graph
import pickle
import numpy as np

import json, time
import numpy as np
from flask import Flask, request

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    start = time.time()
    message = request.get_data()
    data = json.loads(message)
    input_data = np.array(data["data"]).astype('float32')
    for i in range(0, input_data.shape[0]):
        if input_data[i]>bound_high[i]:
            input_data[i] = bound_high[i]
        if input_data[i]<bound_low[i]:
            input_data[i] = bound_low[i]
            
    input_data -= input_mean
    input_data /= input_std
    #print(input_data)
    ret = serving_sess.run(y, feed_dict={x:input_data.reshape(1,21)})
    ret *= output_std
    ret += output_mean
    json_data = json.dumps({'y': ret.tolist()})
    print("Time spent handling the request: %f" % (time.time() - start))
    return json_data

if __name__=='__main__':
    #prepare tensorflow neural network
    print('Loading the model')
    graph = load_graph('./frozen_model.pb')
    x = graph.get_tensor_by_name('prefix/placeholder/x_inputs:0')
    y = graph.get_tensor_by_name('prefix/output_layer/y_output:0')

    print('Starting Session')
    gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.33)
    sess_config = tf.ConfigProto(gpu_options=gpu_options)
    serving_sess = tf.Session(graph=graph, config=sess_config)

    with open('X_mean.txt', 'rb') as handle:
        X_mean = pickle.load(handle, encoding='latin1')
    with open('X_std.txt', 'rb') as handle:
        X_std = pickle.load(handle, encoding='latin1')
    print(X_mean.shape)
    print(X_std.shape)
    input_mean = X_mean[0:21]
    input_std = X_std[0:21]
    output_mean = X_mean[21:25]
    output_std = X_std[21:25]
    print(type(input_mean))
    print(input_std)
    print(output_mean)
    print(output_std)

    with open('bound_low.txt','rb') as handle:
	    bound_low = pickle.load(handle)

    with open('bound_high.txt','rb') as handle:
	    bound_high = pickle.load(handle)

    print('Starting Api')
    app.run()
