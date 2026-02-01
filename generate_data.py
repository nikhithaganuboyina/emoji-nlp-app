import pandas as pd
import random

# List of 50+ emojis
emojis = [
    "😄","😢","🎉","😠","❤️","😱","😂","😞","😎","🥳","🤔","🤩","🤯",
    "😇","🙁","😤","🥰","😏","😜","🤪","😌","😋","😛","😝","🤤","😖",
    "😣","😔","😓","😒","🙄","😪","😴","🤐","😷","🤒","🤕","🤢","🤮",
    "🤧","🥶","🥵","🥴","😵","😲","😳","😡","🤬","😶","😐"
]

# Create sample templates for each emoji (5 per emoji for simplicity)
templates = {
    "😄": ["I am so happy today", "Feeling great", "Life is amazing", "I feel fantastic", "Yay, so happy!"],
    "😢": ["This is so sad", "I feel miserable", "I am heartbroken", "Tears are falling", "Feeling terrible", "Feeling depressed", "I am feeling down"],
    "🎉": ["Let's party tonight", "Celebration time", "We won!", "Time to celebrate", "I am excited!"],
    "😠": ["I am feeling angry", "This makes me mad", "So frustrating!", "I am furious", "That annoyed me"],
    "❤️": ["I love this", "So much love", "Adore it!", "Feeling affectionate", "I am in love"],
    "😱": ["I am scared", "Feeling terrified", "This is shocking!", "I am terrified", "This is scary!"],
    "😂": ["That was funny", "LOL", "Hilarious!", "I can't stop laughing", "So funny!,laugh,i am laughing"],
    "😞": ["I am disappointed", "So sad", "Feeling low", "This is unfortunate", "I am upset", "Feeling depressed", "I feel hopeless"],
    "😎": ["I am feeling cool", "Looking stylish", "Feeling confident", "I am chill", "So relaxed"],
    "🥳": ["Party time!", "Let's celebrate", "Birthday vibes", "Feeling festive", "Yay!"],
    "🤔": ["I am thinking", "Hmm, I wonder", "Curious about this", "I need to figure it out", "Thinking..."],
    "🤩": ["I am amazed", "Wow, incredible!", "This is awesome", "Feeling starstruck", "So cool!"],
    "🤯": ["Mind blown", "I can't believe it", "Shocking!", "This is crazy", "Overwhelmed"],
    "😇": ["Feeling blessed", "So innocent", "Peaceful day", "Feeling good", "I am calm"],
    "🙁": ["I feel sad", "Not happy today", "This is disappointing", "Feeling down", "Unhappy with this", "Feeling depressed"],
    "😤": ["I am frustrated", "So annoyed", "Feeling angry", "This is irritating", "Upset!"],
    "🥰": ["I feel loved", "So affectionate", "Feeling romantic", "Sending love", "I adore this"],
    "😏": ["Feeling smug", "I know something", "Feeling cheeky", "Sly smile", "I got this"],
    "😜": ["Being playful", "Just kidding", "Silly me", "Feeling fun", "Playful mood"],
    "🤪": ["Feeling crazy", "Silly and weird", "Wacky mood", "Funny mood", "I am goofy"],
    "😌": ["Feeling relaxed", "Peaceful mind", "Calm day", "So soothing", "Feeling relieved"],
    "😋": ["Delicious!", "Yummy food", "So tasty", "Feeling satisfied", "I love this meal"],
    "😛": ["Playful", "Just joking", "Cheeky mood", "Silly face", "Fun time"],
    "😝": ["Being goofy", "Silly mood", "Funny face", "Feeling wild", "Crazy fun"],
    "🤤": ["Hungry", "I want that", "So tempting", "Delicious food", "Mouth watering", "I am starving", "I need food,i am hungry"],
    "😖": ["Frustrated", "So stressed", "Feeling bad", "Annoyed", "Uncomfortable"],
    "😣": ["Struggling", "This is hard", "I can't", "Feeling stressed", "Difficult situation"],
    "😔": ["Feeling down", "Sad day", "I feel bad", "Disappointed", "Not happy", "Feeling depressed,i am in depression"],
    "😓": ["Exhausted", "Tired", "Feeling stressed", "Overworked", "Sweating from stress"],
    "😒": ["Annoyed", "Not impressed", "Feeling bored", "Ugh...", "Frustrated mood"],
    "🙄": ["Eye roll", "So annoying", "Not impressed", "Ugh", "Seriously?"],
    "😪": ["Sleepy", "So tired", "I want to nap", "Feeling drowsy", "Almost asleep"],
    "😴": ["Sleeping", "Good night", "Dreaming", "Feeling relaxed", "ZZZ...,i am sleeping"],
    "🤐": ["Silent", "Keeping quiet", "Can't say", "Sealed lips", "Shhh!"],
    "😷": ["Sick", "Not feeling well", "Flu symptoms", "Feeling ill", "Health issues"],
    "🤒": ["Fever", "Feeling sick", "Temperature high", "Unwell", "Need rest"],
    "🤕": ["Injured", "Feeling pain", "Ouch!", "Bandaged up", "Hurt myself", "Recovery time"],
    "🤢": ["Feeling nauseous", "Sick to stomach", "I can't eat", "Yuck!", "Gross feeling"],
    "🤮": ["Vomiting", "Feeling sick", "Gross", "Cannot handle this", "Yucky!"],
    "🤧": ["Sneezing", "Cold symptoms", "Allergies!", "Feeling ill", "Sniff sniff"],
    "🥶": ["Freezing", "So cold", "Winter mood", "Shivering", "I need warmth"],
    "🥵": ["Hot", "Feeling overheated", "Summer sun", "Sweaty", "So warm!"],
    "🥴": ["Dizzy", "Feeling weird", "Out of it", "I am woozy", "Confused mood"],
    "😵": ["Dazed", "Feeling faint", "Mind spinning", "Overwhelmed", "I am dizzy"],
    "😲": ["Surprised", "I can't believe it", "Shocked!", "Wow!", "Unbelievable!"],
    "😳": ["Embarrassed", "Feeling shy", "Blushing", "Oh no!", "Caught off guard"],
    "😡": ["Angry", "So mad", "Fuming", "Frustrated", "Upset!"],
    "🤬": ["Cursing", "Extreme anger", "Furious", "Mad!", "Outraged"],
    "😶": ["Speechless", "No words", "Silent", "Nothing to say", "Shocked silently"],
    "😐": ["Neutral", "Feeling meh", "Indifferent", "No reaction", "Meh..."]
}

# Generate balanced dataset
samples_per_emoji = 100  # 100 sentences per emoji → 50*100=5000 samples
data = []

for emoji in emojis:
    for _ in range(samples_per_emoji):
        sentence = random.choice(templates[emoji])
        suffixes = ["", "!", "!!", " :)", " :("]
        sentence += random.choice(suffixes)
        data.append([sentence, emoji])

# Shuffle and save
random.shuffle(data)
df = pd.DataFrame(data, columns=["sentence","emoji"])
df.to_csv("data.csv", index=False)
print("data.csv with 50+ emojis (including hungry & depression) generated!")
