import tensorflow as tf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle

#data1 = pd.read_csv('test_Input_IC_plus_5000_s1_t1.csv').values
#data2 = pd.read_csv('test_Input_IC_plus_95_hover_s1_t1.csv').values
#data3 = pd.read_csv('test_Input_IC_plus_195_hover_s1_t1.csv').values

#data_set =  np.vstack((data1, data2))
#data_set =  np.vstack((data_set, data3)) 
data_set = pd.read_csv('test_s1_t1.csv').values.astype('float32')
#np.random.shuffle(data_set)
#print(data_set.shape)
#print(data_set[20,:])
np.random.shuffle(data_set)
print(data_set.shape)
#print(data_set[20,:])
X_mean = np.mean(data_set, axis=0)
print(X_mean)
data_set -= X_mean
X_std = np.std(data_set, axis=0)
print(X_std)
data_set /= X_std

with open("X_mean.txt", "wb") as Variable_mean:
    pickle.dump(X_mean, Variable_mean)
with open("X_std.txt", "wb") as Variable_std:
    pickle.dump(X_std, Variable_std)


split_point = int(data_set.shape[0]*0.7)
print(split_point)

set_train = data_set[0:split_point,:]
set_test  = data_set[split_point:data_set.shape[0],:]

print(set_train.shape)
print(set_test.shape)
x_train = set_train[:,0:15]
y_train = set_train[:,15:19]
x_test  = set_test[:,0:15]
y_test  = set_test[:,15:19]

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

input_size = 15
output_size = 4
hid_size = [input_size, 90, 32, output_size]

with tf.variable_scope("placeholder"):
    x = tf.placeholder(tf.float32, [None, hid_size[0]], name='x_inputs')
    y_targets = tf.placeholder(tf.float32, [None, hid_size[3]], name='y_targets')

with tf.variable_scope("layer1"):
    w1 = tf.Variable(tf.random_normal([hid_size[0],hid_size[1]], stddev=1, seed=1), name='layer1_weights')
    b1 = tf.Variable(tf.zeros([hid_size[1]]), name='layer1_bias')
    layer1 = tf.nn.tanh(tf.add(tf.matmul(x,w1), b1), name='layer1_nodes')

with tf.variable_scope("layer2"):
    w2 = tf.Variable(tf.random_normal([hid_size[0]+hid_size[1],hid_size[2]], stddev=1, seed=1), name='layer2_weights')
    b2 = tf.Variable(tf.zeros([hid_size[2]]), name='layer2_bias')
    layer2 = tf.nn.tanh(tf.add(tf.matmul(tf.concat([x, layer1], axis=1),w2), b2), name='layer2_nodes')

with tf.variable_scope("output_layer"):
    w3 = tf.Variable(tf.random_normal([hid_size[1]+hid_size[2],hid_size[3]], stddev=1, seed=1), name='output_layer_weights')
    b3 = tf.Variable(tf.zeros([hid_size[3]]), name='output_layer_bias')
    y = tf.add(tf.matmul(tf.concat([layer1, layer2],axis=1), w3), b3,name='y_output')

with tf.variable_scope("loss_function"):
    mean_squared_error = tf.reduce_mean(tf.squared_difference(y_targets,y),name='mean_squared_error')

with tf.variable_scope("Optimization"):
    optimizer = tf.train.GradientDescentOptimizer(0.1)
    update = optimizer.minimize(mean_squared_error, name='update')

loss_train_log = []
loss_test_log = []
saved_model_filename = "./Model_test2/test_3HL_model.ckpt"
saver = tf.train.Saver()

nodes = [n.name for n in tf.get_default_graph().as_graph_def().node]
#print(nodes)
with open("nodes.txt", "wb") as Variable_nodes:
    pickle.dump(nodes, Variable_nodes)
#for op in nodes:
#    print(op.name)

print(x_train[100], y_train[100])
gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.333)
sess_config = tf.ConfigProto(gpu_options=gpu_options)
with tf.Session(config=sess_config) as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(4000000):
        #batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(update, feed_dict={x: x_train, y_targets: y_train})
        loss_train=sess.run(mean_squared_error, feed_dict={x: x_train, y_targets: y_train})
        loss_test=sess.run(mean_squared_error, feed_dict={x: x_test, y_targets: y_test})
        loss_train_log.append(loss_train)
        loss_test_log.append(loss_test)
        if (i%1000)==0:
            print("Iteration: ",i, "loss:", loss_train,  "testLoss", loss_test)
    save_path = saver.save(sess, saved_model_filename)
    print(save_path)

plotdata = pd.DataFrame(np.vstack((np.vstack((np.arange(np.array(loss_train_log).shape[0]), loss_train_log)),loss_test_log)).T,columns=['iterations', 'Train_MSE','test_MSE'])
plt.figure()
plt.plot('iterations', 'Train_MSE', data=plotdata, color='green', label='training loss')
plt.plot('iterations', 'test_MSE', data=plotdata, color='red', label='testing loss')
plt.grid(True)
plt.legend()
plt.xlabel('iteration times')
plt.ylabel('rate')
plt.savefig('loss.png')

with open("loss_train_log.txt", "wb") as loss_train_logs:
    pickle.dump(loss_train_log, loss_train_logs)
with open("loss_test_log.txt", "wb") as loss_test_logs:
    pickle.dump(loss_test_log, loss_test_logs)
