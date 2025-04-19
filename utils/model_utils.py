import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("model/Trained_model.h5")

class_labels = [
    "Blues", "Classical", "Country", "Disco", "Hip-Hop",
    "Jazz", "Metal", "Pop", "Reggae", "Rock"
]

def predict_genre(audio_input):
    prediction = model.predict(audio_input)[0]
    predicted_index = np.argmax(prediction)
    predicted_genre = class_labels[predicted_index]
    return predicted_genre, prediction
