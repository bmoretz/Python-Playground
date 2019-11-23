import tensorflow as tf

const1 = tf.constant([[1,2,3], [1,2,3]])
const2 = tf.constant([[3,4,5], [3,4,5]])

result = tf.add(const1, const2)
print(result)