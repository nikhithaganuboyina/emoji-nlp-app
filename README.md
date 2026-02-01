# Emoji NLP Project

## Setup

1. Create virtual environment and activate:
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate

2. Install dependencies:
   pip install tensorflow pandas numpy

3. Generate dataset:
   python generate_data.py

4. Train the model:
   python train_model.py

5. Predict emojis interactively:
   python app.py
