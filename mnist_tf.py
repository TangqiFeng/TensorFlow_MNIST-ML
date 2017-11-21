# import tensorflow
import tensorflow as tf
# import mnist data from tensorflow
from tensorflow.examples.tutorials.mnist import input_data

# get mnist data set & store in current folder, rename it 'MNIST_data'
# A one-hot vector is a vector which is 0 in most dimensions, and 1 in a single dimension. 
# In this case, the nth digit will be represented as a vector which is 1 in the nth dimension.
# For example, 3 would be [0,0,0,1,0,0,0,0,0,0]
mnist = input_data.read_data_sets('MNIST_data',one_hot=True)

# set batch_size, every time put 100 images for training
batch_size = 100
# calculate number of batches from data set
n_batch = mnist.train.num_examples // batch_size

# define two placehoder
x = tf.placeholder(tf.float32,[None,784]) #images  784 = 28 * 28 pixels
y = tf.placeholder(tf.float32,[None,10])  #labels  10 stands for 0~9
LearningRate = tf.Variable(0.001, dtype=tf.float32)
# define a nural network              
# tf.zeros -> initial value is 0
# W has a shape of [784, 10] because we want to multiply the 784-dimensional image vectors by it 
# to produce 10-dimensional vectors of evidence for the difference classes. 
# b:bisa, has a shape of [10] so we can add it to the output.
W1 = tf.Variable(tf.truncated_normal([784,500],stddev=0.1)) 
b1 = tf.Variable(tf.zeros([500])+0.1)           # changed a initial method
L1 = tf.nn.tanh(tf.matmul(x,W1)+b1)

W2 = tf.Variable(tf.truncated_normal([500,300],stddev=0.1)) 
b2 = tf.Variable(tf.zeros([300])+0.1)           
L2 = tf.nn.tanh(tf.matmul(L1,W2)+b2)

W3 = tf.Variable(tf.truncated_normal([300,10],stddev=0.1)) 
b3 = tf.Variable(tf.zeros([10])+0.1)         
prediction = tf.nn.tanh(tf.matmul(L2,W3)+b3)

# calculate cost(loss), and minimize loss
# use cross_entropy method: tf.nn.softmax_cross_entropy_with_logits method
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=prediction))
# use AdamOptimizer to train
train_step = tf.train.AdamOptimizer(LearningRate).minimize(loss)

# initial glabal variables
init = tf.global_variables_initializer()

# calculate accuracy
correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(prediction,1)) # correct return true, otherwise return false
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) # true->1.0   false->0

# create loop to train
sess = tf.Session()
sess.run(init)
for eposh in range(1):
    sess.run(tf.assign(LearningRate, 0.001*(0.95**eposh)))   # dynamic set LearningRate
    for batch in range(n_batch):
        batch_xs,batch_ys = mnist.train.next_batch(batch_size)
        sess.run(train_step,{x:batch_xs, y:batch_ys})
# calculate accuracy
    LR = sess.run(LearningRate)
    test_acc = sess.run(accuracy,{x:mnist.test.images, y:mnist.test.labels})
print("Iter " + str(eposh) + ",Testing Accuracy " + str(test_acc) + ", LearningRate " +str(LR))

def predict(in_data):
    num = sess.run(prediction,{x:in_data})
    n = tf.argmax(prediction,1)
    return n

