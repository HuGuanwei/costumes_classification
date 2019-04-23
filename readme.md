# Costumes Classification

### Abstract

Image classification have been an active research area of computer vision for years. Greater speed and larger accuracy have been achieved with the power of deep learning.  Furthermore, one can reuse a pre-trained model as a starting point to a second task. This technique is called *transfer learning*, utilizing feature map from pre-trained model to extract and process information for final classification. In this repository,  the vgg16 model with batch normalization pre-trained on ImageNet dataset is used to classify costumes data from The Metropolitan Museum of Art<sup>[1]</sup> into three categories.

### Data Description

This repository leverages the pre-trained `vgg16_bn` model and the costumes collection data at The Metropolitan Museum of Art and metadata from Google BigQuery<sup>[2]</sup>. The image data contains three categories: China, Japan, American or European.

**sample data**:

![data_sample](png/data_sample.png)



### Architecture

![vgg16](png/vgg16.png)

### Prediction

**model prediction**:

![predict_1](png/predict_1.png)



![predict_2](png/predict_2.png)

**model performance**:

![confusion](png/confusion.png)



[1]: <https://www.metmuseum.org/>
[2]: https://bigquery.cloud.google.com/dataset/bigquery-public-data:the_met?pli=1