# Paloma Detector - A funny little Computer Vision project 

Made this to scare the pigeons out of my balcony reproducing dog bark sounds.

Based on YOLOv10 model.

## 🎥 Video Demonstration 

https://github.com/user-attachments/assets/f73d7d30-9e07-407b-9c4f-39b5af850dbc


 Better quality videos [here](https://vimeo.com/1017689109?share=copy) and [here](https://vimeo.com/1017688445?share=copy) as well.

## 📋 Steps 2 follow 

1. Install all the dependencies

        pip3 install -r requirements.txt

2. Clone YOLO original repo inside and install all its dependencies

        git clone https://github.com/THU-MIG/yolov10.git
        cd yolov10
        pip install .


    Warning: In case you got something like `ImportError: cannot import name 'YOLOv10' from 'ultralytics`. Check the solution [here](https://github.com/ultralytics/ultralytics/issues/13295)

3. Install a `yolov10` model from [this page](https://docs.ultralytics.com/models/yolov10/#comparisons) and append it to the project root
![alt text](imgs/image.png)

    I use `YOLOv10-N`, you can choose any but be sure to change it in the `app.py` if you choose a different version


4. Execute the program

        python3 app.py


## 🤓 Considerations 
- You can change the audio file to any you'd prefer. Be sure to change it in ln.13  of `app.py`
- Change the object to any present in the `categories.py`. Just be sure to change the `class_id` in ln.40 of `app.py`


## 🐋 Dockerfile 

THIS ONLY WORKS FOR LINUX ENVIRONMENTS 🐧

According to ChatGPT: MacOS and Windows uses a different architecture and device management system, which makes direct mapping of `/dev/video0` or similar paths unavailable. This issue isn’t easy to resolve natively because Docker for macOS/Windows doesn’t have access to your host hardware devices like webcams, or microphones.

1. Build the image:

        docker build -t paloma-detector . 

2. Start the container:

        docker run --rm -it --privileged paloma-detector


 ## 🧠 References
I made this project inspired by [this video](https://www.youtube.com/watch?v=e4c_lslXT4g)

Special thanks to the people involved! 😄
