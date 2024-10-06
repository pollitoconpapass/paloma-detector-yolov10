import cv2
import typer
import threading 
import supervision as sv
from playsound import playsound 
from ultralytics import YOLOv10
from categories import category_dict


model = YOLOv10("yolov10n.pt")
app = typer.Typer()

SOUND_FILE = "./audio/dog-bark-179915.mp3"
def play_sound():
    threading.Thread(target=lambda: playsound(SOUND_FILE)).start()


def process_webcam():
    cap = cv2.VideoCapture(0) # -> change for your webcam

    if not cap.isOpened():
        print("Error: No se pudo abrir la webcam.")
        return

    sv.BoundingBoxAnnotator()
    sv.LabelAnnotator()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        detections = sv.Detections.from_ultralytics(results)

        for box, class_id, confidence in zip(detections.xyxy, detections.class_id, detections.confidence):
            class_name = category_dict[class_id]
            
            # If a Bird is detected, play the sound (bird : 14 | dog : 16)
            if class_id == 67:  
                play_sound() 
            
            cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (255, 0, 0), 2)
            cv2.putText(frame, f"{class_name}: {confidence:.2f}", (int(box[0]), int(box[1] - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow("Webcam", frame)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

@app.command()
def webcam():
    typer.echo("Iniciando el procesamiento de la webcam...")
    process_webcam()

if __name__ == "__main__":
    app()
