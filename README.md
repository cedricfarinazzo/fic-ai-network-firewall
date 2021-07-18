# S2 - AI

## Url path classfication
Playbooks:
- [Logistic regression](./url_path_classification/logistic_regression.ipynb)
- [Keras](./url_path_classification/keras.ipynb)


## Improvements

- dataset:
    - use ethernet frame instead of url path and query string
    - transform ethernet frame into images (ideas from [this article](https://www.01net.com/actualites/ces-chercheurs-transforment-les-malwares-en-images-pour-mieux-les-detecter-grace-a-une-ia-1912576.html))
- neural net:
    - add CNN layer
    - continuous learning ?
- live mode with pyshark ?
- ban ip if the ethernet frame is suspicious ?
