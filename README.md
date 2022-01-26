# S2 - AI

## Url path classfication

Detecting malicious queries

The dataset is composed of 44713 malicious queries and 1265994 good queries.

### Playbooks

#### Logistic regression
[Here](./url_path_classification/logistic_regression.ipynb)

Results with a logistic regression:
```
Accuracy: 0.999371
```

### Keras 
[Here](./url_path_classification/keras.ipynb)

In this playbook, we use a keras model.

Models:
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 197)               39006     
_________________________________________________________________
dense_1 (Dense)              (None, 128)               25344     
_________________________________________________________________
dense_2 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_3 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_4 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_5 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_6 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_7 (Dense)              (None, 1)                 129       
=================================================================
Total params: 147,039
Trainable params: 147,039
Non-trainable params: 0
```

Results:
```
Accuracy:  0.994346559047699
```

## Ethernet frame classfication

Detecting malicious ethernet frames

The dataset is composed of ethernet frames of HTTP requests. The url can be malicious or not. We used the dataset of the previous part to generate this one.

### Playbooks

#### Preprocessing
[Here](./ethernet_frame_classification/ethernet_frame_preprocessing.ipynb)

This playbook is a POC to convert ethernet frames to images and vice versa.

#### Keras CNN Sigmoid
[Here](./ethernet_frame_classification/Keras-cnn-sigmoid.ipynb)

In this playbook, we convert ethernet frames to images and use a keras model based on CNN and sigmoid activation function to determine their badness.

Models:
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 73, 18, 32)        896       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 36, 9, 32)         0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 34, 7, 64)         18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 17, 3, 64)         0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 15, 1, 64)         36928     
_________________________________________________________________
flatten (Flatten)            (None, 960)               0         
_________________________________________________________________
dense (Dense)                (None, 128)               123008    
_________________________________________________________________
dense_1 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_2 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_3 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_4 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_5 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_6 (Dense)              (None, 1)                 129       
=================================================================
Total params: 262,017
Trainable params: 262,017
Non-trainable params: 0
```

Results: 
```
Accuracy:  0.5096271634101868
```

#### Keras CNN Binary
[Here](./ethernet_frame_classification/Keras-cnn-binary.ipynb)

In this playbook, we convert ethernet frames to images and use a keras model based on CNN and binary activation function to determine their badness.

Models:
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 73, 18, 32)        896       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 36, 9, 32)         0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 34, 7, 64)         18496     
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 17, 3, 64)         0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 15, 1, 64)         36928     
_________________________________________________________________
flatten (Flatten)            (None, 960)               0         
_________________________________________________________________
dense (Dense)                (None, 150)               144150    
_________________________________________________________________
dense_1 (Dense)              (None, 150)               22650     
_________________________________________________________________
dense_2 (Dense)              (None, 150)               22650     
_________________________________________________________________
dense_3 (Dense)              (None, 150)               22650     
_________________________________________________________________
dense_4 (Dense)              (None, 150)               22650     
_________________________________________________________________
dense_5 (Dense)              (None, 150)               22650     
_________________________________________________________________
dense_6 (Dense)              (None, 1)                 151       
=================================================================
Total params: 313,871
Trainable params: 313,871
Non-trainable params: 0
```

Results:
```
Accuracy:  0.99707717
```

We saved the model data [here](./ethernet_frame_classification/models/cnn-binary.h5)

#### Keras CNN Flatten
[Here](./ethernet_frame_classification/Keras-dense-flatten.ipynb)

This time, we didn't convert ethernet frames into images.

Models:
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 1500)              2251500   
_________________________________________________________________
dense_1 (Dense)              (None, 128)               192128    
_________________________________________________________________
dense_2 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_3 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_4 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_5 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_6 (Dense)              (None, 128)               16512     
_________________________________________________________________
dense_7 (Dense)              (None, 1)                 129       
=================================================================
Total params: 2,526,317
Trainable params: 2,526,317
Non-trainable params: 0
```

Results:
```
Accuracy:  0.5116087198257446
```

#### Classification
[Here](./ethernet_frame_classification/Classification.ipynb)

In this playbook, we used some classification algorithms.

Results:
| Algorithm | Training duration | Accuracy |
|:----------|:------------------|:---------|
| KNeighborsClassifier(ball_tree) | 73.117s | 0.55 |
| KNeighborsClassifier(kd_tree) | 92.289s | 0.55 |
| Decision Tree | 5.69s | 1.00 |
| Random Forest | 249.879s | 1.00 |
| Gradient Boosting | 646.379s | 1.00 |
| Bagging | 31.88s | 1.00 |
| Extra Tree | 275.184s | 1.00 |

The best algorithm is Decision Tree (Dtree)


#### Dtree
[Here](./ethernet_frame_classification/dtree.ipynb)

In this playbook, we used the Decision Tree algorithm.
Same results as before.


## Ethernet frame classfication V2

In this folder, we change the way how we loaded data: instead of loading everything at the beginning what required ~28Go of RAM, we tried to only load data chunks.
Additionally, we increase the dataset size by adding good ethernet frame (not only HTTP requests).

In order to only load data chunks, we preprocessed our dataset by storing every ethernet frame in a specific file. [Here](./ethernet_frame_classification_v2/preprocessing.ipynb)

Unfortunately, our new loading method cannot work with Dtree... [Here](./ethernet_frame_classification_v2/dtree.ipynb)

With Random Forest algorithm, we had an accuracy of 0.51 [Here](./ethernet_frame_classification_v2/random-forest.ipynb)

With Keras, we were stuck with an accuracy of 0.4944140613079071 [Here](./ethernet_frame_classification_v2/keras.ipynb)

In conclusion, it is very difficult to classify malicious and good Ethernet frames without filters on them.

## Malware Detection

This folder contains a script to download malwares from [https://abuse.ch/](https://abuse.ch/)
