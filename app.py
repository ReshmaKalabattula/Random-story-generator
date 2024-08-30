from flask import Flask, render_template, jsonify # type: ignore
import random

app = Flask(__name__)

# Expanded lists of story elements
characters = {
    "hero": [
        "a brave knight", "a clever scientist", "a daring pirate captain", "a young princess", 
        "a resourceful superhero", "a skilled archer", "a fearless space explorer", "a wise old wizard",
        "a charming rogue", "a determined engineer"
    ],
    "companion": [
        "a loyal squire", "a wise old sage", "a mischievous elf", "a talking animal", 
        "a helpful robot", "a mystical healer", "a quick-witted bard", "a noble steed",
        "a resourceful mechanic", "a courageous sidekick"
    ],
    "villain": [
        "an evil sorcerer", "a fierce dragon", "a rogue AI", "a treacherous pirate", 
        "a wicked queen", "a corrupt official", "a malevolent alien overlord", "a cunning warlord",
        "a sinister scientist", "a dark enchantress"
    ]
}

settings = [
    "in a dark forest", "in a mystical land", "on a distant planet", "in a haunted castle", 
    "in a small village", "in a floating castle above the clouds", "in a mysterious cave filled with glowing crystals", 
    "on a mountain peak that touches the stars", "in an ancient ruin beneath the ocean", 
    "on a futuristic space station", "in a deserted desert town", "in a bustling magical city"
]

conflicts = [
    "searching for a lost treasure", "fighting to save the kingdom", "trying to break an ancient curse", 
    "preventing a powerful artifact from falling into the wrong hands", "rescuing a kidnapped ally", 
    "defeating an evil sorcerer", "discovering a hidden truth that could alter history", 
    "surviving a deadly trial set by the gods", "escaping from a perilous trap", "uncovering a secret conspiracy"
]

resolutions = [
    "found the treasure and restored peace", "defeated the villain and saved the kingdom", 
    "broke the curse and brought prosperity", "secured the artifact and protected the world", 
    "rescued the ally and strengthened their bond", "outwitted the villain and restored order", 
    "revealed the hidden truth and changed the course of history", "survived the trial and gained divine favor", 
    "escaped the trap and lived to tell the tale", "exposed the conspiracy and brought justice"
]

def generate_story():
    hero = random.choice(characters["hero"])
    companion = random.choice(characters["companion"])
    villain = random.choice(characters["villain"])
    setting = random.choice(settings)
    conflict = random.choice(conflicts)
    resolution = random.choice(resolutions)

    stories = [
        f"Once upon a time, there was {hero} {setting}. Alongside {companion}, they faced {villain} who was {conflict}. Through bravery and determination, they {resolution}.",
        f"In the heart of {setting}, {hero} found themselves facing {villain}. With the aid of {companion}, they embarked on a quest to {conflict}. Their journey ended with them {resolution}.",
        f"{hero} was living peacefully {setting} when {villain} arrived with a plan to {conflict}. Joined by {companion}, they fought through challenges and {resolution}.",
        f"Amidst the chaos of {setting}, {hero} and {companion} confronted {villain} who was {conflict}. Their courage led to a climactic battle, and in the end, they {resolution}.",
        f"On a strange {setting}, {hero} and their loyal companion, {companion}, discovered that {villain} was {conflict}. Through cunning and bravery, they {resolution}."
    ]

    return random.choice(stories)

@app.route('/')
def index():
    story = generate_story()
    return render_template('story.html', story=story)

@app.route('/new_story')
def new_story():
    story = generate_story()
    return jsonify({'story': story})

if __name__ == '__main__':
    app.run(debug=True)
