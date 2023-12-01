# model.py
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

class SentimentAnalysisModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Embedding(input_dim=10000, output_dim=16, input_length=100),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss=tf.compat.v1.losses.sparse_softmax_cross_entropy, metrics=['accuracy'])
        return model

    def train(self, X_train, y_train, epochs=5):
        self.model.fit(X_train, y_train, epochs=epochs)

    def predict(self, text):
        sequence = self.tokenizer.texts_to_sequences([text])
        padded_sequence = pad_sequences(sequence, maxlen=100)
        return self.model.predict(padded_sequence)
