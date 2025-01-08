num_parallel_calls = 4
input_shape = 416
max_boxes = 20
jitter = 0.3
hue = 0.1
sat = 1.0
cont = 0.8
bri = 0.1
norm_decay = 0.99
norm_epsilon = 1e-3
pre_train = True
num_anchors = 9
num_classes = 80
training = True
ignore_thresh = .5
learning_rate = 0.001
train_batch_size = 10
val_batch_size = 10
train_num = 2800
val_num = 5000
Epoch = 50
obj_threshold = 0.5
nms_threshold = 0.5
gpu_index = "0"
log_dir = './logs'
data_dir = './model_data'
model_dir = './test_model/model.ckpt-192192'
pre_train_yolo3 = True
yolo3_weights_path = './model_data/yolov3.weights'
darknet53_weights_path = './model_data/darknet53.weights'
anchors_path = './model_data/yolo_anchors.txt'
classes_path = './model_data/coco_classes.txt'

image_file = "./img/test.jpg"
