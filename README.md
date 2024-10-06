# Paloma Detector - A funny little Computer Vision project

Made this to scare the pigeons out of my balcony reproducing dog bark sounds.

Based on YOLOv10 model.

## Video Demonstration
TODO

## Steps 2 follow

1. Create a conda environment

        conda create --name yolo python=3.12
        conda activate yolo

2. Install all the dependencies

        pip3 install -r requirements.txt

3. Clone YOLO original repo inside and install all its dependencies

        git clone https://github.com/THU-MIG/yolov10.git
        cd yolov10
        pip install .


    Warning: In case you got something like `ImportError: cannot import name 'YOLOv10' from 'ultralytics`. Check the solution [here](https://github.com/ultralytics/ultralytics/issues/13295)

4. Install a `yolov10` model from [this page](https://docs.ultralytics.com/models/yolov10/#comparisons) and append it to the project root
![alt text](imgs/image.png)

    I use `YOLOv10-N`, you can choose any but be sure to change it in the `app.py` if you choose a different version


5. Execute the program

        python3 app.py


## Considerations
- You can change the audio file to any you'd prefer. Be sure to change it in ln.13  of `app.py`
- Change the object to any present in the `categories.py`. Just be sure to change the `class_id` in ln.40 of `app.py`


## References
I made this project guiding from [this video](https://www.youtube.com/watch?v=e4c_lslXT4g)

Special thanks to the people involved! 😄
