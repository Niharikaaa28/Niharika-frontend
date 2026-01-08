import tflite_runtime.interpreter as tflite
import numpy as np
import cv2

IMG_SIZE = 224

print("Loading model...")
interpreter = tflite.Interpreter(model_path="model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess(image):
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def predict(image):
    image = preprocess(image)
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()

    score = interpreter.get_tensor(output_details[0]['index'])[0][0]
    label = "MALIGNANT" if score > 0.5 else "BENIGN"
    confidence = score if label == "MALIGNANT" else (1 - score)

    return label, confidence