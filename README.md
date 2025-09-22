# Data Project Template

<a target="_blank" href="https://datalumina.com/">
    <img src="https://img.shields.io/badge/Datalumina-Project%20Template-2856f7" alt="Datalumina Project" />
</a>


## Project Organization

```

├── README.md          <- The top-level README for developers using this project
|
├── requirements.txt   <- The requirements file for reproducing the analysis environment
|
├── test_video.mp4     <- The plain unpredicted video used to test the model
|
├── yolov8n.pt         <- The yolov8 nano pre-trained weights file
│
├── runs               <- this fiolder holds all the training and test files
|   |
|   └── detect
|       |
|       ├── predict             <- predicted videos/images
|       |   |
|       |   └── test_video.avi  <- video used to test the model
|       |
|       ├── train3              <- model train data
|       |
|       └── val                 <- model validation data
|
├── dataset            <- storing all training datasets
|   |
|   ├── boxes          <- training image frames that have been boxed
|   |
|   ├── images         <- plain training image frames
|   |
|   ├── yolo-dataset            <- stores the dataset needed for training
|   |   |
|   |   ├── images              <- splits plain training image frames into train and val 
|   |   |
|   |   ├── labels              <- converts the train and val image frames into yolo-forman .txt
|   |   |
|   |   └── yolo-dataset.yaml   <- the config file that tells yolo where our train and test data are
|   |   
|   └── annotations.xml <- contains bounding box information for objects in the train data
|
├── .venv           <- contains the virtual environment for this project
|
├── .vscode         <- folder created by vscode to store workspace specific settings
|       
└── src                         <- Source code for this project
    │
    └── xml_conv.py             <- converts the annotation.xml into readable yolov8 dataset
```

--------