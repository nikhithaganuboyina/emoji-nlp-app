import pandas as pd
import numpy as np
import pickle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.preprocessing import LabelEncoder

# ----------------- Load dataset -----------------
df = pd.read_csv("data.csv")
sentences = df['sentence'].values
labels = df['emoji'].values

# ----------------- Encode labels -----------------
le = LabelEncoder()
labels_encoded = le.fit_transform(labels)

# Save label encoder to map predictions later
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

# ----------------- Tokenize text -----------------
max_words = 2000  # maximum number of words in tokenizer
tokenizer = Tokenizer(num_words=max_words, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)
max_len = max([len(seq) for seq in sequences])  # maximum sequence length

padded_sequences = pad_sequences(sequences, maxlen=max_len, padding='post')

# Save tokenizer and max_len for UI
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)
with open("max_len.pkl", "wb") as f:
    pickle.dump(max_len, f)

# ----------------- Build LSTM model -----------------
model = Sequential([
    Embedding(input_dim=max_words, output_dim=64, input_length=max_len),
    LSTM(128),
    Dropout(0.3),
    Dense(len(le.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# ----------------- Train model -----------------
model.fit(padded_sequences, labels_encoded, epochs=50, batch_size=64, verbose=1)

# ----------------- Save trained model -----------------
model.save("emoji_model.h5")
print("Model trained and saved as emoji_model.h5")
