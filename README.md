
# Steel Defect Detection



## Objective
Defect detection is one of the critical parts of manufacturing of a product in an industry. Manually inspecting the bulk production of steel sheets for defect detection is a tiresome task and could be prone to human errors. When steel sheets are manufactured it came in contact with many heavy machines for the purpose of drying, cutting, rolling, heating due to this some defects occur on the surface. So, this technical report aims at developing a deep learning model which can identify the surface defects in steel sheets and classify those defects into various classes. Automating this task can improve the manufacturing standards of organization. For this purpose, I have used a CNN model and a pre trained model(Xception).The pre trained model Xception has given a better accuracy,precision and recall score.

## Data Description

The dataset set consists of 12,568 images and the size of the image is 1600x256. All the images are of high quality

## Screenshots:
Homepage:
![Homepage](https://user-images.githubusercontent.com/24864663/158668868-7757d829-572b-438c-8749-f058450babea.PNG)

Prediction:
![Predictionpage](https://user-images.githubusercontent.com/24864663/158668877-119aa7ce-2d15-4d6a-b109-7c77004c6186.PNG)


## Final Model :

We have created a Streamlit Application based on Xception pretrained model and our model will identify the type of defect based on images that were captured by a camera. 
