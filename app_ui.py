import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

# ---------------- Load model and tokenizer ----------------
model = load_model("emoji_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

with open("max_len.pkl", "rb") as f:
    max_len = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

# ---------------- Prediction function ----------------
def predict_emoji(sentence):
    seq = tokenizer.texts_to_sequences([sentence])
    padded = pad_sequences(seq, maxlen=max_len, padding='post')
    pred = model.predict(padded, verbose=0)
    top_index = pred.argmax()
    top_emoji = le.inverse_transform([top_index])[0]
    return top_emoji

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Emoji Predictor", page_icon="😄")

# Custom CSS + JS for emoji rain
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(120deg, #FFDEE9, #B5FFFC);
        overflow-x: hidden;
    }
    .title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        background: -webkit-linear-gradient(#ff6a00, #ee0979);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .emoji {
        text-align: center;
        font-size: 120px;
        animation: bounce 0.5s ease;
    }
    @keyframes bounce {
        0% { transform: scale(0.5); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    .input-box {
        width: 50%;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
        font-size: 24px;
        padding: 10px;
    }
    .button {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    /* Emoji rain container */
    .emoji-rain {
        pointer-events: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 9999;
    }
    @keyframes fall {
        0% { transform: translateY(-50px); opacity: 1; }
        100% { transform: translateY(100vh); opacity: 0; }
    }
    .falling-emoji {
        position: fixed;
        font-size: 24px;
        animation: fall linear forwards;
    }
    </style>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

    <script>
    function emojiRain(mainEmoji){
        // Create container
        let container = document.createElement('div');
        container.className = 'emoji-rain';
        document.body.appendChild(container);

        // Add multiple emojis
        for(let i=0; i<50; i++){
            let span = document.createElement('span');
            span.innerText = mainEmoji;
            span.className = 'falling-emoji';
            span.style.left = Math.random()*window.innerWidth + 'px';
            span.style.fontSize = (Math.random()*30 + 20) + 'px';
            span.style.animationDuration = (Math.random()*3 + 2) + 's';
            container.appendChild(span);

            // Remove after falling
            setTimeout(()=>{
                span.remove();
            }, 4000);
        }

        // Remove container after animation
        setTimeout(()=>{ container.remove(); }, 4000);

        // Also pop confetti
        confetti({
            particleCount: 50,
            spread: 100,
            origin: { y: 0.6 }
        });
    }
    </script>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">Emoji Predictor NLP App 😄</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;">Type a sentence below and see the predicted emoji!</p>', unsafe_allow_html=True)

# Input box + button
user_input = st.text_input("", placeholder="Type your sentence here...", key="sentence", label_visibility="collapsed")
predict_button = st.button("Predict Emoji")

# Show big emoji and trigger emoji rain
if predict_button and user_input:
    emoji = predict_emoji(user_input)
    st.markdown(f'<div class="emoji">{emoji}</div>', unsafe_allow_html=True)
    st.markdown(f"<script>emojiRain('{emoji}');</script>", unsafe_allow_html=True)
