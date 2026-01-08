# model.py
import tflite_runtime.interpreter as tflite
import numpy as np
import cv2

interpreter = tflite.Interpreter(model_path="mobilenet_stable.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

IMG_SIZE = 224

def preprocess(image):
    # Resize
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))

    # Convert BGR (OpenCV) → RGB (model expects this)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Normalize
    image = image.astype("float32") / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    return image

def predict(image):
    image = preprocess(image)

    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])[0][0]
    print("Raw model output:", output)

    return "MALIGNANT" if output > 0.5 else "BENIGN"