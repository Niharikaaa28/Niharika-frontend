from model import predict_from_file

label, confidence = predict_from_file("test_images/malignant.jpg")
print("Label:", label)
print("Confidence:", int(confidence * 100), "%")