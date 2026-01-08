import tflite_runtime.interpreter as tflite
import numpy as np

interpreter = tflite.Interpreter(model_path="mobilenet_stable.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def predict(image):
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)

    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])[0][0]

    if output > 0.5:
        return "MALIGNANT"
    else:
        return "BENIGN"