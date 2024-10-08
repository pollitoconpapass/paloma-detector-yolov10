import cv2
import typer
import threading 
import supervision as sv
from playsound import playsound 
from ultralytics import YOLOv10
from categories import category_dict


model = YOLOv10("yolov10n.pt")
app = typer.Typer()

SOUND_FILE = "./audio/barks.mp3"
def play_sound():
    threading.Thread(target=lambda: playsound(SOUND_FILE)).start() # -> using threads to not interrumpt the video processing while playing the sound

def process_webcam():
    cap = cv2.VideoCapture(0) # -> change for your webcam

    if not cap.isOpened():
        print("Error: Webcam not found.")
        return

    sv.BoundingBoxAnnotator()
    sv.LabelAnnotator()

    while True:
        ret, frame = cap.read() # -> ret: boolean variable that checks if the frame is available | frame: image array vector captured based on the default frames per second
        if not ret:
            break

        # Apply object detection using the model
        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)

        for box, class_id, confidence in zip(detections.xyxy, detections.class_id, detections.confidence):
            class_name = category_dict[class_id] # -> assign the object based on the class_id using the category_dict
            
            # If a Bird is detected, play the sound (bird : 14 | dog : 16)
            if class_id == 14:
                play_sound() 
            
            # Draw the bounding box and label on the frame
            cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 2)
            cv2.putText(frame, f"{class_name}: {confidence:.2f}", (int(box[0]), int(box[1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        # Display video, use 'q' key to exit
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Start the webcam processing
@app.command()
def webcam():
    typer.echo("Starting webcam processing...")
    process_webcam()

if __name__ == "__main__":
    app()
