from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def preprocess_sentences(sentences, tokenizer=None, max_len=None):
    """
    Tokenize and pad sentences.
    """
    if tokenizer is None:
        tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
        tokenizer.fit_on_texts(sentences)
    sequences = tokenizer.texts_to_sequences(sentences)
    padded = pad_sequences(sequences, padding='post', maxlen=max_len)
    return padded, tokenizer
