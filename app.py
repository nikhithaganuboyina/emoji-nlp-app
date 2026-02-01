from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
# Load model, tokenizer, and max_len
model = load_model("emoji_model.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)
with open("max_len.pkl", "rb") as f:
    max_len = pickle.load(f)

# Emoji list
emojis = ["😄","😢","🎉","😠","❤️","😱","😂","😞"]

def predict_emoji(sentence):
    seq = tokenizer.texts_to_sequences([sentence])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')
    pred = model.predict(padded, verbose=0)[0]
    top_index = pred.argmax()          # only the top prediction
    return emojis[top_index]


# Interactive prediction
while True:
    sentence = input("Type a sentence (or 'exit' to quit): ")
    if sentence.lower() == "exit":
        break
    print("Emoji predicted:", predict_emoji(sentence))
